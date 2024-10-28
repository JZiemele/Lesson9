import re
from collections import Counter
import json
import csv





with open('employees.json', 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)
print(json.dumps(loaded_data, indent=4, ensure_ascii=False))

with open('employees.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)


print('-++++++++++++++++++++++++++++++-')


def csv_to_json(csv_file_path, json_file_path):
    """Чтение данных из CSV и запись в JSON."""
    data = []

    # Чтение данных из CSV-файла
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)  # Добавляем каждую строку как объект словаря в список

    # Запись данных в JSON-файл
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)  # С отступами для удобочитаемости




# Пример использования
csv_file = 'employees.csv'
json_file = 'employees.json'

csv_to_json(csv_file, json_file)

print(f"Данные из {csv_file} успешно перенесены в {json_file}")


with open('employees.json', 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)
print(json.dumps(loaded_data, indent=4, ensure_ascii=False))

with open('employees.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)





def read_json(file_path):
    """Чтение данных из JSON-файла."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


#def find_employee_by_name(data):
#   """Функция для поиска сотрудника по имени."""
#    name = input("Введите имя сотрудника для поиска: ")
#   for employee in data:
#        if employee["name"].lower() == name.lower():
#            print(f"Найден сотрудник: {employee}")
#            return
#    print("Сотрудник не найден.")



def find_employee_by_name(data):
    """Функция для поиска сотрудника по части имени."""
    name = input("Введите часть имени сотрудника для поиска: ").lower()
    found = False
    for employee in data:
        if name in employee["name"].lower():
            print(f"Найден сотрудник: {employee}")
            found = True
    if not found:
        print("Сотрудник не найден.")


#def filter_by_language(data):
#    """Функция фильтрации по языку программирования."""
#    language = input("Введите язык программирования: ")
#    found = False
#    for employee in data:
#        if language in employee["languages"]:
#            print(f"Сотрудник, владеющий {language}: {employee['name']}")
#            found = True
#    if not found:
#        print(f"Никто не владеет языком {language}")



def filter_by_language(data):
    """Функция фильтрации по языку программирования."""
    language = input("Введите часть языка программирования: ").lower()
    found = False
    for employee in data:
        # Если employee["languages"] уже является списком, то просто проходим по нему
        if any(language in lang.lower() for lang in employee["languages"]):
            print(f"Сотрудник, владеющий языком, содержащим '{language}': {employee['name']}")
            found = True
    if not found:
        print(f"Никто не владеет языком, содержащим '{language}'")



def filter_by_year(data):
    """Функция фильтрации по году рождения и вычисления среднего роста."""
    year = int(input("Введите год для фильтрации: "))
    total_height = 0
    count = 0
    for employee in data:
        birth_year = int(employee["birthday"].split('.')[2])
        if birth_year < year:
            total_height += employee["height"]
            count += 1

    if count > 0:
        average_height = total_height / count
        print(f"Средний рост сотрудников, родившихся до {year}: {average_height:.2f} см")
    else:
        print(f"Нет сотрудников, родившихся до {year}")


def display_menu():
    """Функция для отображения меню."""
    print("\nМеню:")
    print("1. Найти сотрудника по имени")
    print("2. Фильтр по языку программирования")
    print("3. Фильтр по году рождения и средний рост")
    print("4. Выйти из программы")


def main():
    json_file = 'employees.json'
    data = read_json(json_file)

    while True:
        display_menu()
        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            find_employee_by_name(data)
        elif choice == '2':
            filter_by_language(data)
        elif choice == '3':
            filter_by_year(data)
        elif choice == '4':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main()