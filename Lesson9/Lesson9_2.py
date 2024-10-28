import re
from collections import Counter
import json
import csv


def print_LZ(i):
    print("_____________________________")
    print('          LESSON 9           ')
    print(f'      Exercise Nr.{i}        ')
    print('______________________________')
    return print_LZ

print_LZ(4)

input_file = 'lesson_9_4.txt'

with open(input_file, 'r', encoding='utf-8') as infile:
    print("\nСодержимое входного файла:")
    print(infile.read())

stop_word_file = 'stop_words.txt'

with open(stop_word_file, 'r', encoding='utf-8') as file:
    print("\nСодержимое файла с условием:")
    print(file.read())


def censor_text(input_file, stop_word_file):
    # Читаем список запрещённых слов
    with open(stop_word_file, 'r', encoding='utf-8') as file:
        stop_word = file.read().split()  # Получаем список запрещённых слов

    # Читаем содержимое текстового файла
    with open(input_file, 'r', encoding='utf-8') as infile:
        text = infile.read()

    # Проходим по каждому слову из списка запрещённых
    for word in stop_word:
        # Создаём шаблон регулярного выражения для поиска слова независимо от регистра
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        # Заменяем все вхождения слова на звездочки
        text = pattern.sub('*' * len(word), text)

    # Выводим результат на экран
    print(text)

censor_text(input_file, stop_word_file)



print_LZ(5)


def find_shoolboy_with_low_grades(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:  # Пропускаем пустые строки
                continue

            # Удаляем возможные номера перед фамилиями (например, "1.", "2.")
            line = re.sub(r'^\d+\.\s*', '', line)

            # Разбиваем строку на составляющие (фамилия, имя, оценка)
            data = line.split()
            # Проверяем, что строка состоит хотя бы из трех элементов (фамилия, имя и оценка)
            if len(data) >= 3 and data[-1].isdigit():
                last_name = data[0]
                first_name = data[1]
                grade = data[-1]  # Оценка находится в последнем элементе

                try:
                    grade = int(grade)
                    # Проверяем, если оценка меньше 3
                    if grade < 3:
                        print(f"{last_name} {first_name} — оценка: {grade}")
                except ValueError:
                    print(f"Ошибка в строке: {line.strip()} — неверный формат оценки.")
            else:

                print(f" {line}")


# Пример использования программы
input_filename = 'lesson_9_5.txt'  # Название файла с фамилиями, именами и оценками

find_shoolboy_with_low_grades(input_filename)



print_LZ(6)



def sum_of_numbers_in_file(file_name):
    # Читаем содержимое файла
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()  # Чтение всего содержимого файла
    print("\nСодержимое входного файла:")
    print(content)
    print("\nОкончание входного файла:")
    # Используем регулярное выражение для поиска всех чисел в тексте
    numbers = re.findall(r'\d+', content)  # Находим все последовательности цифр

    # Преобразуем найденные строки с числами в целые числа и суммируем их
    total_sum = sum(int(number) for number in numbers)

    # Открываем файл для добавления результата в конец файла
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"\nСумма всех чисел: {total_sum}\n")
        print(f'Добавлена запись в {file_name} ')

    return total_sum

# Пример использования программы
input_filename = 'lesson_9_6.txt'  # Название файла с содержимым

result = sum_of_numbers_in_file(input_filename)
print(f"Сумма всех чисел: {result}")



print_LZ(7)


def caesar_cipher(text, shift):
    """Функция для шифрования строки с использованием кириллицы."""
    encrypted_text = []

    for char in text:
        if 'А' <= char <= 'Я':  # Шифруем заглавные буквы кириллицы
            shift_base = ord('А')
            encrypted_char = chr((ord(char) - shift_base + shift) % 32 + shift_base)
            encrypted_text.append(encrypted_char)
        elif 'а' <= char <= 'я':  # Шифруем строчные буквы кириллицы
            shift_base = ord('а')
            encrypted_char = chr((ord(char) - shift_base + shift) % 32 + shift_base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Оставляем символы без изменений

    return ''.join(encrypted_text)


def encrypt_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()  # Чтение всех строк из файла

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i, line in enumerate(lines):
            shift = i + 1  # Шаг сдвига для каждой строки
            encrypted_line = caesar_cipher(line.strip(), shift)  # Шифруем строку
            outfile.write(encrypted_line + '\n')  # Записываем зашифрованную строку в файл

        print(f'Информация записана в {output_filename}')




# Пример использования программы
input_filename = 'lesson_9_7.txt'  # Название исходного файла

output_filename = 'output_9_7.txt'  # Название файла для зашифрованного текста


encrypt_file(input_filename, output_filename)


with open(input_filename, 'r', encoding='utf-8') as infile:
    print("\nСодержимое входного файла:")
    print(infile.read())



with open(output_filename, 'r', encoding='utf-8') as outfile:
    print("\nСодержимое выходного файла:")
    print(outfile.read())


def caesar_decipher(text, shift):
    """Функция для дешифрования строки с использованием кириллицы."""
    decrypted_text = []

    for char in text:
        if 'А' <= char <= 'Я':  # Дешифруем заглавные буквы кириллицы
            shift_base = ord('А')
            decrypted_char = chr((ord(char) - shift_base - shift) % 32 + shift_base)
            decrypted_text.append(decrypted_char)
        elif 'а' <= char <= 'я':  # Дешифруем строчные буквы кириллицы
            shift_base = ord('а')
            decrypted_char = chr((ord(char) - shift_base - shift) % 32 + shift_base)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)  # Оставляем символы без изменений

    return ''.join(decrypted_text)


def decrypt_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()  # Чтение всех строк из файла

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i, line in enumerate(lines):
            shift = i + 1  # Шаг сдвига для каждой строки
            decrypted_line = caesar_decipher(line.strip(), shift)  # Дешифруем строку
            outfile.write(decrypted_line + '\n')  # Записываем дешифрованную строку в файл


# Дешифровка файла
encrypted_filename = 'output_9_7.txt'
decrypted_filename = 'decrypted_output.txt'
decrypt_file(encrypted_filename, decrypted_filename)

with open(decrypted_filename, 'r', encoding='utf-8') as outfile:
    print("\nСодержимое дешифрованного файла:")
    print(outfile.read())



print_LZ(8)


def read_json(file_path):
    """Чтение данных из JSON-файла."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Ошибка при чтении JSON: {e}")
        return None


def json_to_csv(json_data, csv_file_path):
    """Преобразование данных из JSON в формат CSV и запись в файл."""
    if not json_data:
        print("Нет данных для конвертации")
        return

    # Получаем ключи для заголовков из первого элемента
    keys = json_data[0].keys()

    # Запись данных в CSV
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()  # Записываем заголовки
        writer.writerows(json_data)  # Записываем строки данных


# Пример использования:
json_file = 'employees.json'
csv_file = 'employees.csv'

json_data = read_json(json_file)

if json_data:
    json_to_csv(json_data, csv_file)

    with open('employees.json', 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)
    print(json.dumps(loaded_data, indent=4, ensure_ascii=False))

    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)


def add_employee_to_json(json_file_path):
    """Добавление нового сотрудника в JSON-файл."""
    # Вводим данные для нового сотрудника
    name = input("Введите имя сотрудника: ")
    birthday = input("Введите дату рождения (дд.мм.гггг): ")
    height = int(input("Введите рост (в см): "))
    weight = float(input("Введите вес (в кг): "))
    car = input("Есть ли машина (да/нет): ").lower() == "да"
    languages = input("Введите языки программирования через запятую: ").split(',')

    new_employee = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": [lang.strip() for lang in languages]
    }

    # Читаем существующие данные
    data = read_json(json_file_path)

    # Добавляем нового сотрудника
    data.append(new_employee)

    # Сохраняем обновленный JSON-файл
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Пример использования:
json_file = 'employees.json'
add_employee_to_json(json_file)

json_file = 'employees.json'
csv_file = 'employees.csv'

json_data = read_json(json_file)

if json_data:
    json_to_csv(json_data, csv_file)

    with open('employees.json', 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)
    print(json.dumps(loaded_data, indent=4, ensure_ascii=False))

    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)


print('+++++++++++++++++++++++++++++++++')


def add_employee_to_csv(csv_file_path):
    """Добавление нового сотрудника в CSV-файл."""
    # Вводим данные для нового сотрудника
    name = input("Введите имя сотрудника: ")
    birthday = input("Введите дату рождения (дд.мм.гггг): ")
    height = int(input("Введите рост (в см): "))
    weight = float(input("Введите вес (в кг): "))
    car = input("Есть ли машина (да/нет): ").lower() == "да"
    languages = input("Введите языки программирования через запятую: ").split(',')

    new_employee = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": ', '.join([lang.strip() for lang in languages])  # Сохраняем языки как строку для CSV
    }

    # Добавляем нового сотрудника в CSV
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=new_employee.keys())
        writer.writerow(new_employee)

# Пример использования:
csv_file = 'employees.csv'
add_employee_to_csv(csv_file)

with open('employees.json', 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)
print(json.dumps(loaded_data, indent=4, ensure_ascii=False))

with open(csv_file, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)


