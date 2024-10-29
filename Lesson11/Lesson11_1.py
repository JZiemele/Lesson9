def print_LZ(i):
    print("_____________________________")
    print('          LESSON 11           ')
    print(f'      Exercise Nr.{i}        ')
    print('______________________________')
    return print_LZ

print_LZ(1)



class Soda:
    def __init__(self, flavor=None):
        """Инициализация газировки с возможным параметром вкуса."""
        self.flavor = flavor

    def __str__(self):
        """Метод строковой репрезентации объекта."""
        if self.flavor:
            return f"У вас газировка с {self.flavor} вкусом."
        else:
            return "У вас обычная газировка."

# Придумайте и введите вкус вашей содовой:
flavor = input('Введите вкус содовой:    ')
print(Soda(flavor))

flavor = None
print(Soda(flavor))




print_LZ(2)



class Math:
    """Класс для выполнения основных математических операций."""

    def addition(self, a, b):
        """Метод для сложения двух чисел."""
        result = a + b
        print(f"{a} + {b} = {result}")

    def subtraction(self, a, b):
        """Метод для вычитания второго числа из первого."""
        result = a - b
        print(f"{a} - {b} = {result}")

    def multiplication(self, a, b):
        """Метод для умножения двух чисел."""
        result = a * b
        print(f"{a} * {b} = {result}")

    def division(self, a, b):
        """Метод для деления первого числа на второе."""
        if b != 0:
            result = a / b
            print(f"{a} / {b} = {result}")
        else:
            print("Ошибка: деление на ноль невозможно!")

# Пример использования:
math = Math()
print('Давайте выберем любые два числа и проверим, как работают методы.')
a = int(input('Введите "a": '))
b = int(input('Введите "b": '))
math.addition(a=a, b=b)       # 10 + 5 = 15
math.subtraction(a=a, b=b)    # 10 - 5 = 5
math.multiplication(a=a, b=b) # 10 * 5 = 50
math.division(a=a, b=b)       # 10 / 5 = 2.0
math.division(a=a, b=b)       # Ошибка: деление на ноль невозможно!


print_LZ(3)



class Car:
    def __init__(self, marka, color, car_type, year):
        """Инициализация атрибутов автомобиля."""
        self.marka = marka
        self.color = color
        self.car_type = car_type
        self.year = year

    def set_marka(self, marka):
        """Метод для установки марки автомобиля."""
        self.marka = marka
        print(f"Автомобиль марки {self.marka}.")

    def start(self):
        """Метод для запуска автомобиля."""
        print("Автомобиль заведён.")

    def stop(self):
        """Метод для отключения автомобиля."""
        print("Автомобиль заглушен.")

    def set_year(self, year):
        """Метод для установки года выпуска."""
        self.year = year
        print(f"Год выпуска автомобиля установлен на {self.year}.")

    def set_type(self, car_type):
        """Метод для установки типа автомобиля."""
        self.car_type = car_type
        print(f"Тип автомобиля установлен как {self.car_type}.")

    def set_color(self, color):
        """Метод для установки цвета автомобиля."""
        self.color = color
        print(f"Цвет автомобиля установлен как {self.color}.")


# Пример использования:
my_car = Car("BMW", "Красный", 'Седан', 2019)

# Вывод атрибутов объекта
print(my_car.__dict__)

# Вызов методов
my_car.start()              # Выведет: Автомобиль заведён.
my_car.stop()               # Выведет: Автомобиль заглушен.
my_car.set_year(2022)       # Выведет: Год выпуска автомобиля установлен на 2022.
my_car.set_type("Внедорожник")  # Выведет: Тип автомобиля установлен как Внедорожник.
my_car.set_color("Чёрный")   # Выведет: Цвет автомобиля установлен как Чёрный.

# Ввод данных пользователя
print('Вы находитесь в авто')
marka1 = input('Посмотрите в техпаспорт и введите марку машины: ')
car_type1 = input('Там же найдёте тип вашей машины, введите его: ')
year1 = input('Ещё в техпаспорте можно найти год выпуска машины, важно все, введите и его: ')
color1 = input('И самое главное это цвет машины (вы же знаете КРАСНОЕ ездит быстрее), здесь важно всё, пишите: ')
a = input('Посмотрите по сторонам, если за окном авто всё меняется,\nто просто поставьте "да", '
          '\nа если двигаются только прохожие, то смело ставьте "нет", '
          '\nа если темно и ничего не видно, ставим "не знаю": ')
b = input('Прислушайтесь, слышите тарахтение или звук мотора?\nМожно ответить "да" или "нет":  ')
c = input('Сейчас самое главное, в салоне горит свет? "да" или "нет":  ')

# Создание нового объекта автомобиля
my_car1 = Car(marka=marka1, color=color1, car_type=car_type1, year=year1)
print(f'Вы находитесь в машине {marka1}')
my_car.set_year(year1)
my_car.set_type(car_type1)
my_car.set_color(color1)


# Логика работы программы в зависимости от ввода пользователя
if a == 'да' and b == 'да' and c == 'нет':
    my_car1.start()
    print('Вы движетесь навстречу своей судьбе, или просто едете домой, что тоже неплохо.')
elif a == 'нет' and b == 'да' and c == 'нет':
    my_car1.start()
    print('Вы стоите и палите топливо зря, выключите мотор, ожидание станет дешевле.')
elif a == 'не знаю' and b == 'да' and c == 'нет':
    my_car1.start()
    print('Интересная ситуация: ночь, темнота, фары выключены. Можно вас спросить, чем вы там занимаетесь?')
elif (a == 'да' and b == 'нет' and c == 'нет') or (a == 'да' and b == 'нет' and c == 'да'):
    my_car1.stop()
    print('Но вы едете. Ааа, вы на эвакуаторе, уже треволнения позади и проблема решена.')
elif b == 'нет' and c == 'да':
    my_car1.stop()
    print('Машина заглушена, всё спокойно.')
else:
    print('Что-то странное происходит, пожалуйста, проверьте данные.')




print_LZ(4)


import math

class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        """Инициализация сферы с радиусом и координатами центра."""
        self.radius = radius
        self.center = (x, y, z)

    def get_volume(self):
        """Возвращает объем сферы."""
        return (4 / 3) * math.pi * self.radius ** 3

    def get_square(self):
        """Возвращает площадь поверхности сферы."""
        return 4 * math.pi * self.radius ** 2

    def get_radius(self):
        """Возвращает радиус сферы."""
        return self.radius

    def get_center(self):
        """Возвращает координаты центра сферы в виде кортежа."""
        return self.center

    def set_radius(self, radius):
        """Устанавливает новый радиус сферы."""
        self.radius = radius

    def set_center(self, x, y, z):
        """Устанавливает новые координаты центра сферы."""
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        """Проверяет, находится ли точка внутри сферы."""
        distance = math.sqrt((x - self.center[0]) ** 2 + (y - self.center[1]) ** 2 + (z - self.center[2]) ** 2)
        return distance <= self.radius


# Пример использования:
sphere = Sphere()  # Сфера с радиусом 1 и центром (0, 0, 0)
print(f"Объем сферы: {sphere.get_volume():.2f}")
print(f"Площадь поверхности сферы: {sphere.get_square():.2f}")
print(f"Радиус сферы: {sphere.get_radius()}")
print(f"Центр сферы: {sphere.get_center()}")

# Изменение радиуса и координат центра
sphere.set_radius(5)
sphere.set_center(1, 2, 3)

print(f"Новый радиус: {sphere.get_radius()}")
print(f"Новый центр: {sphere.get_center()}")

# Проверка точки внутри сферы
point_inside = sphere.is_point_inside(2, 2, 2)
print(f"Точка (2, 2, 2) внутри сферы: {point_inside}")

point_outside = sphere.is_point_inside(10, 10, 10)
print(f"Точка (10, 10, 10) внутри сферы: {point_outside}")



print_LZ(5)



class SuperStr(str):
    def is_repeatance(self, s):
        """
        Проверяет, может ли текущая строка быть получена целым количеством повторов строки s.
        Возвращает True, если может, иначе False.
        """
        if not s:  # Пустая строка не содержит повторов
            return False
        # Проверяем, может ли длина текущей строки делиться на длину строки s
        if len(self) % len(s) == 0:
            repeat_count = len(self) // len(s)
            # Проверяем, равна ли текущая строка s, повторенной нужное количество раз
            return self == s * repeat_count
        return False

    def is_palindrom(self):
        """
        Проверяет, является ли текущая строка палиндромом (игнорируя регистр).
        Возвращает True, если является, иначе False.
        """
        normalized_str = self.lower()  # Приводим к нижнему регистру
        return normalized_str == normalized_str[::-1]  # Сравниваем строку с её зеркальным отражением


# Пример использования:
super_str = SuperStr("abcabcabc")
print(super_str.is_repeatance("abc"))  # True
print(super_str.is_repeatance("ab"))   # False
print(super_str.is_palindrom())        # False

super_palindrom = SuperStr("А роза упала на лапу азора")
print(super_palindrom.is_palindrom())  # True