# 9 Lesson 1 Задание

import json
import csv
import os
import shutil
import psutil
from platform import uname
import platform
import re
from collections import Counter




def print_LZ(i):
    print("_____________________________")
    print('          LESSON 9           ')
    print(f'      Exercise Nr.{i}        ')
    print('______________________________')
    return print_LZ

print_LZ(1)

# my_system = platform.uname()
# print(f"System: {my_system.system}")
# print(os.getcwd())
# print(os.listdir())
# main_path = '/home/krokodilena/Lesson3/pythonProject'
#
# # ключи для создания названий папок
# extensions = {
#
#     'python': ['py'],
#
#     'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'text', 'wpd', 'odt'],
#
#     'exel': ['xlsx', 'xls', 'csv'],
#
# }
#
#
# # создаем папки из ключей словаря
# def create_folders_from_list(folder_path, folder_names):
#     for folder in folder_names:
#         if not os.path.exists(f'{folder_path}/{folder}'):
#             os.mkdir(f'{folder_path}/{folder}')
#
#
# def get_subfolder_paths(folder_path) -> list:
#     subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]
#
#     return subfolder_paths
#
#
# def get_file_paths(folder_path) -> list:
#     file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]
#
#     return file_paths
#
#
# def sort_files(folder_path):
#     file_paths = get_file_paths(folder_path)
#     ext_list = list(extensions.items())
#
#     for file_path in file_paths:
#         extension = file_path.split('.')[-1]
#         file_name = file_path.split('/')[-1]
#
#         for dict_key_int in range(len(ext_list)):
#             if extension in ext_list[dict_key_int][1]:
#                 print(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
#                 os.rename(file_path, f'{main_path}/{ext_list[dict_key_int][0]}/{file_name}')
#
#
# def remove_empty_folders(folder_path):
#     subfolder_paths = get_subfolder_paths(folder_path)
#
#     for p in subfolder_paths:
#         if not os.listdir(p):
#             print('Deleting empty folder:', p.split('/')[-1], '\n')
#             os.rmdir(p)
#
#
# if __name__ == "__main__":
#     create_folders_from_list(main_path, extensions)
#     sort_files(main_path)
#     remove_empty_folders(main_path)
#
# files = os.listdir(path=".")
# print('В папку "python" перемещено ',len(files),' файлов')
# directory_path = "/home/krokodilena/Lesson3/pythonProject/python"
# total_size = 0
# for dirpath, dirnames, filenames in os.walk(directory_path):
#     for filename in filenames:
#         file_path = os.path.join(dirpath, filename)
#         total_size += os.path.getsize(file_path)
# print(f"Общий размер файлов в папке python: {total_size} байт")


# for otpuska_sotrudnikov in os.listdir(path = "."):
#     file_name = 'people_data_vacation.xlsx'
#     new_name = 'otpuska_sotrudnikov.xlsx'
#     try:
#         os.rename(f'{main_path}/{'exel'}/{file_name}', f'{main_path}/{'exel'}/{new_name}')
#     except FileNotFoundError:
#         print('Файл не найден')
#         break
# print('Переименован файл  people_data_vacation.xlsx в otpuska_sotrudnikov.xlsx')

# 9 Lesson 2 Задание (шпаргалка для себя)

print_LZ(2)

def datu_ievade (promt):
    alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    data = input(promt)
    for i in range(len(data)):
        for j in range(len(alphabet_ru)):
            if data[i] == alphabet_ru[j]:
               corect_data = True
               return data
            else:
                corect_data = False
        print("Неправильный ввод данных. Попробуйте ещё раз")
        data = input(promt)


def ievade():
    uzvards = datu_ievade('Введите фамилию подсудимого (ой): ').title()
    vards = datu_ievade('Введите имя подсудимого (ой): ').title()
    teva_vards = datu_ievade('Введите отчество подсудимого (ой): ').title()

    print(f'\nПодсудимая:\n{uzvards} {vards} {teva_vards}\nв судебном заседании вину инкриминируемого '
               f'правонарушения\nпризнала в полном объёме\nи суду показала,\nчто 14 сентября 1976 года, будучи в состоянии '
               f'алкогольного опьянения от безысходности,\nв связи с состоянием здоровья позвонила со своего стационарного '
               f'телефона в полицию,\nсообщив о том, что у неё в квартире якобы заложена бомба.\nПосле чего приехали '
               f'сотрудники полиции, скорая и пожарные, которым она сообщила,\nчто бомба — это она.')

ievade()
while True:
    turp = (input('Заполняем дела дальше? Ответ (да или нет) ')).lower()
    if turp == 'да':
        ievade()
    else:
        break


print_LZ(2)


def replace_name(text):
    # Шаблон для поиска ФИО с возможной двойной фамилией
    pattern = r'([А-ЯЁ][а-яё]+(-[А-ЯЁ][а-яё]+)?\s[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+)'

    # Заменим найденное ФИО на "N"
    result = re.sub(pattern, 'N', text)

    return result


# Текст для обработки
text = '''
Подсудимая Эверт-Колокольцева Елизавета Александровна
в судебном заседании вину инкриминируемого правонарушения
признала в полном объёме и суду показала, что 14 сентября
1876 года, будучи в состоянии алкогольного опьянения
от безысходности, в связи с состоянием здоровья позвонила
со своего стационарного телефона в полицию, сообщив о том, что
у неё в квартире якобы заложена бомба. После чего приехали сотрудники полиции, 
скорая и пожарные, которым она сообщила,
что бомба — это она.
'''

# Обработка текста
new_text = replace_name(text)
print(new_text)

print_LZ(3)

from collections import Counter


def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        print("Содержимое входного файла:")
        for line in infile:
            print(line.strip())  # Выводим каждую строку в консоль
        infile.seek(0)  # Возвращаем указатель в начало файла для последующей обработки

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                # Убираем знаки препинания и приводим строку к нижнему регистру
                clean_line = re.sub(r'[^\w\s]', '', line).lower()
                words = clean_line.split()  # Разбиваем строку на слова
                if words:  # Проверяем, что строка не пуста
                    word_counts = Counter(words)  # Считаем частоту слов
                    max_count = max(word_counts.values())  # Находим максимальное количество повторений
                    most_common_words = [word for word, count in word_counts.items() if
                                         count == max_count]  # Находим все слова с максимальным количеством повторений
                    outfile.write(f"{', '.join(most_common_words)} {max_count}\n")  # Записываем в файл результат

    # Открываем выходной файл в режиме чтения и выводим его содержимое в консоль
    with open(output_file, 'r', encoding='utf-8') as outfile:
        print("\nСодержимое выходного файла:")
        print(outfile.read())


# Пример использования программы
input_filename = 'lesson_9_3.txt'  # Имя входного файла
output_filename = 'ex_output.txt'  # Имя выходного файла

process_file(input_filename, output_filename)

print_LZ(4)