

def print_LZ():
    i = 1
    while True:
        yield (f'_____________________________,\n  '
               f'      LESSON 13           \n'
               f'      Exercise Nr.{i}          \n'
               f'______________________________')
        i += 1

lesson = print_LZ()



print(next(lesson))


def fibonacci_generator(n):
    """Генератор чисел Фибоначчи до n-го числа."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Запрашиваем у пользователя номер до которого нужно вывести последовательность
num = int(input("Введите номер числа, до которого нужно вывести последовательность Фибоначчи: "))

# Выводим последовательность чисел Фибоначчи
print("Последовательность Фибоначчи:")
print(", ".join(map(str, fibonacci_generator(num))))




print(next(lesson))

def cyclic_sequence_1():
    """Генератор, выдающий бесконечную циклическую последовательность 1-2-3."""
    sequence = [1, 2, 3]
    while True:
        for number in sequence:
            yield number

# Запрашиваем у пользователя количество чисел для вывода
num = int(input("Введите количество чисел для вывода: "))

# Выводим нужное количество чисел из циклической последовательности
count = 0
for number in cyclic_sequence_1():
    if count >= num:
        break
    print(number, end=' ')
    count += 1
print('\n++++++++++++++++++++++++++++++++')

def cyclic_sequence(symbols, cycles):
    """Генератор, создающий бесконечную циклическую последовательность заданных символов."""
    while True:
        for symbol in symbols:
            yield symbol


while True:
    # Запрашиваем количество символов для зацикливания
    num_symbols = int(input("Какое количество символов вы хотите зациклить? "))

    # Запрашиваем сами символы и добавляем их в список
    symbols = []
    for i in range(num_symbols):
        symbol = input(f"Введите символ {i + 1}: ")
        symbols.append(symbol)

    # Запрашиваем количество циклов
    num_cycles = int(input("Сколько циклов вы хотите выполнить? "))

    # Выводим циклическую последовательность
    print("Результат циклической последовательности:")
    generator = cyclic_sequence(symbols, num_cycles)
    count = 0
    for symbol in generator:
        if count >= num_cycles * num_symbols:
            break
        print(symbol, end=' ')
        count += 1
    print()  # Переход на новую строку после вывода последовательности

    # Спрашиваем, хочет ли пользователь повторить
    repeat = input("Хотите ещё что-нибудь ввести в цикл? (да/нет): ").strip().lower()
    if repeat != "да":
        print("Спасибо за игру!")
        break

if __name__ == "__main__":
    print(next(lesson))
    fibonacci_generator(num)