import re
import matplotlib.pyplot as plt

data = []

print("Введите данные в формате 'количество машин - регион'. Для окончания ввода введите пустую строку.")

while True:
    entry = input()
    if not entry:
        break

    match = re.match(r"(\d+)\s*машин\s*-\s*(.+)", entry)
    if match:
        try:
            count = int(match.group(1))
            region = match.group(2)
            data.append({'region': region, 'count': count})
        except ValueError:
            print("Некорректное количество автомобилей. Пожалуйста, проверьте ввод.")
    else:
        print("Некорректный формат данных. Пожалуйста, проверьте ввод.")

# Сортируем данные по количеству автомобилей в порядке убывания
sorted_data = sorted(data, key=lambda x: x['count'], reverse=True)

# Выводим все регионы в порядке убывания
print("Все регионы в порядке убывания:")
for entry in sorted_data:
    print(f"{entry['count']} машин - {entry['region']}")

top_regions = sorted(data, key=lambda x: x['count'], reverse=True)[:5]

# Создаем списки для осей X и Y
regions = [region['region'] for region in top_regions]
counts = [region['count'] for region in top_regions]

# Создаем график столбцов
plt.bar(regions, counts)

# Настройки графика
plt.xlabel('Регион')
plt.ylabel('Количество машин')
plt.title('Топ 5 регионов по количеству машин')

# Поворот надписей на оси X для лучшей видимости
plt.xticks(rotation=45)

# Установка подходящего макета для лучшей видимости надписей
plt.tight_layout()

# Сохранение графика в виде изображения
plt.savefig('top5_regions.png')

# Отображение графика
plt.show()