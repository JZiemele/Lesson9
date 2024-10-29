from abc import ABC, abstractmethod


def print_LZ():
    i = 3
    while True:
        yield (f'_____________________________,\n  '
               f'      LESSON 13           \n'
               f'      Exercise Nr.{i}          \n'
               f'______________________________')
        i += 1

lesson = print_LZ()
print(next(lesson))




# Класс для представления пиццы с атрибутами и расчётом стоимости
class Pizza:
    BASE_PRICES = {"Small": 2.00, "Medium": 2.50, "Large": 3.00}  # Цены на основу в зависимости от размера
    INGREDIENT_PRICES = {
        "cheese": 0.40,
        "pepperoni": 0.50,
        "mushrooms": 0.30,
        "onions": 0.05,
        "bacon": 0.60
    }

    def __init__(self, size=None, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def calculate_price(self):
        price = Pizza.BASE_PRICES.get(self.size, 0)  # Цена основы пиццы
        if self.cheese:
            price += Pizza.INGREDIENT_PRICES["cheese"]
        if self.pepperoni:
            price += Pizza.INGREDIENT_PRICES["pepperoni"]
        if self.mushrooms:
            price += Pizza.INGREDIENT_PRICES["mushrooms"]
        if self.onions:
            price += Pizza.INGREDIENT_PRICES["onions"]
        if self.bacon:
            price += Pizza.INGREDIENT_PRICES["bacon"]
        return price

    def __str__(self):
        ingredients = []
        if self.cheese:
            ingredients.append("cheese")
        if self.pepperoni:
            ingredients.append("pepperoni")
        if self.mushrooms:
            ingredients.append("mushrooms")
        if self.onions:
            ingredients.append("onions")
        if self.bacon:
            ingredients.append("bacon")

        ingredients_str = ", ".join(ingredients) if ingredients else "no additional ingredients"
        return (f"Pizza(size={self.size}, ingredients=[{ingredients_str}]) - "
                f"Price: €{self.calculate_price():.2f}")


# Класс "строитель" для создания объекта Pizza
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza


# Класс для управления процессом создания пиццы
class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        return self.builder.build()


# Функция для взаимодействия с клиентом и создания заказа
def order_pizza():
    builder = PizzaBuilder()

    # Запрос размера
    size = input("Какой размер пиццы вы хотите? (Small/Medium/Large): ").capitalize()
    builder.set_size(size)

    # Запрос ингредиентов
    if input("Хотите добавить сыр? (да/нет): ").lower() == "да":
        builder.add_cheese()
    if input("Хотите добавить пепперони? (да/нет): ").lower() == "да":
        builder.add_pepperoni()
    if input("Хотите добавить грибы? (да/нет): ").lower() == "да":
        builder.add_mushrooms()
    if input("Хотите добавить лук? (да/нет): ").lower() == "да":
        builder.add_onions()
    if input("Хотите добавить бекон? (да/нет): ").lower() == "да":
        builder.add_bacon()

    # Создание пиццы и вывод стоимости
    pizza = builder.build()

    print(pizza)
    print(f"С вас €{pizza.calculate_price():.2f}")
    print("\nСпасибо за ваш заказ!")


# Пример использования функции заказа
order_pizza()


print(next(lesson))

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Класс Dog, наследующий от Animal
class Dog(Animal):
    def speak(self):
        return "ГАВ!"

# Класс Cat, наследующий от Animal
class Cat(Animal):
    def speak(self):
        return "МЯУ!"

# Класс AnimalFactory с фабричным методом create_animal
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == "собака":
            return Dog()
        elif animal_type.lower() == "кот":
            return Cat()
        else:
            raise ValueError("Неизвестный тип животного")

# Пример использования фабрики
factory = AnimalFactory()

dog = factory.create_animal("собака")
cat = factory.create_animal("кот")

print(dog.speak())  # Вывод: ГАВ!
print(cat.speak())  # Вывод: МЯУ!


# Абстрактный класс Product
class Product(ABC):
    def __init__(self, weight, price, cost, color):
        self.weight = weight
        self.price = price
        self.cost = cost
        self.color = color

    @abstractmethod
    def produce(self):
        pass

    def __str__(self):
        return (f"{self.__class__.__name__} "
                f"(Вес: {self.weight} kg, Цена: ${self.price}, "
                f"Себестоимость: ${self.cost}, Цвет: {self.color})")

# Класс Car, наследующий от Product
class Car(Product):
    def produce(self):
        return ("Изготовление автомобиля: сборка кузова, "
                "установка двигателя, покраска, контроль качества.")

# Класс Bicycle, наследующий от Product
class Bicycle(Product):
    def produce(self):
        return ("Изготовление велосипеда: сборка рамы, "
                "установка колес, покраска, контроль качества.")

# Класс ProductFactory с фабричным методом create_product
class ProductFactory:
    @staticmethod
    def create_product(product_type, weight, price, cost, color):
        if product_type.lower() == "car":
            return Car(weight, price, cost, color)
        elif product_type.lower() == "bicycle":
            return Bicycle(weight, price, cost, color)
        else:
            raise ValueError("Неизвестный тип товара")

# Пример использования фабрики
factory = ProductFactory()

# Создаем автомобиль с заданными параметрами
car = factory.create_product("car", weight=1500, price=20000,
                             cost=15000, color="Red")
# Создаем велосипед с заданными параметрами
bicycle = factory.create_product("bicycle", weight=15,
                                 price=500, cost=300, color="Blue")

print(car)       # Вывод информации о машине
print(car.produce())  # Описание процесса производства машины

print(bicycle)   # Вывод информации о велосипеде
print(bicycle.produce())  # Описание процесса производства велосипеда


print(next(lesson))


class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

# Класс Addition для сложения
class Addition(Strategy):
    def execute(self, a, b):
        return a + b

# Класс Subtraction для вычитания
class Subtraction(Strategy):
    def execute(self, a, b):
        return a - b

# Класс Multiplication для умножения
class Multiplication(Strategy):
    def execute(self, a, b):
        return a * b

# Класс Division для деления
class Division(Strategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Класс Calculator для выполнения операций с разными стратегиями
class Calculator:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        """Устанавливает текущую стратегию"""
        self.strategy = strategy

    def calculate(self, a, b):
        """Выполняет операцию с использованием текущей стратегии"""
        if not self.strategy:
            raise ValueError("Strategy not set")
        return self.strategy.execute(a, b)

# Пример использования Calculator с разными стратегиями
calculator = Calculator()

# Сложение
calculator.set_strategy(Addition())
print("Addition:", calculator.calculate(10, 5))  # Вывод: 15

# Вычитание
calculator.set_strategy(Subtraction())
print("Subtraction:", calculator.calculate(10, 5))  # Вывод: 5

# Умножение
calculator.set_strategy(Multiplication())
print("Multiplication:", calculator.calculate(10, 5))  # Вывод: 50

# Деление
calculator.set_strategy(Division())
print("Division:", calculator.calculate(10, 5))  # Вывод: 2.0