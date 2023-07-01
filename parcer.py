import time
import csv
from bs4 import BeautifulSoup
import requests

url = "https://avtogram.org/"
headers = {
    "authority": "avtogram.org",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "cloudflare=805992f9a98702c3bfc8e8356bd5a3ad; popularity=1687371239; _ym_uid=1687371240672923858; _ym_d=1687371240; _ym_isad=1; PHPSESSID=f32375e0743863efc0ede185bef41912; _ym_visorc=w",
    "referer": "https://www.google.com/",
    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "cross-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

def get_region_number(soup):
    div = soup.find('div', {'class': 'number'})
    if div:
        number = div.text
        region = ''.join(filter(str.isdigit, number[-3:]))  # оставляем только цифры
        return number[0], region
    return None, None


def main():
    last_letter = None
    regions_count = {}

    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        while True:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            letter, region = get_region_number(soup)

            if letter is not None and region is not None:
                if last_letter is not None and letter != last_letter:
                    regions_count[region] = regions_count.get(region, 0) + 1
                    writer.writerow([regions_count[region], region])
                    file.flush()

                last_letter = letter

            time.sleep(0.2)

if __name__ == "__main__":
    main()
