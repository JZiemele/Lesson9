class Prece:
    def __init__(self, name, veikals_name, price):
        """Инициализация товара с закрытыми полями."""
        self.__name = name  # Закрытое поле - название товара
        self.__veikals_name = veikals_name  # Закрытое поле - название магазина
        self.__price = price  # Закрытое поле - стоимость товара

    # Методы для получения доступа к закрытым полям

    def get_name(self):
        return self.__name

    def get_veikals_name(self):
        return self.__veikals_name

    def get_price(self):
        return self.__price

    # Перегрузка операции сложения для товаров
    def __add__(self, other):
        if isinstance(other, Prece):
            return self.__price + other.__price
        raise ValueError("Сложение возможно только между объектами класса товар.")

    # Метод для вывода информации о товаре
    def __str__(self):
        return f"Товар: {self.__name}, Магазин: {self.__veikals_name}, Цена: {self.__price} евро."


class Noliktava:
    def __init__(self):
        """Инициализация склада с пустым массивом товаров."""
        self.__preces = []

    def add_prece(self, prece):
        """Добавление товара на склад."""
        if isinstance(prece, Prece):
            self.__preces.append(prece)
        else:
            raise ValueError("Можно добавлять только объекты класса товар.")

    def get_prece_by_index(self, index):
        """Вывод информации о товаре по индексу."""
        if 0 <= index < len(self.__preces):
            return str(self.__preces[index])
        else:
            return "Товар с таким индексом не найден."

    def get_prece_by_name(self, name):
        """Вывод информации о товаре по имени."""
        for prece in self.__preces:
            if prece.get_name() == name:
                return str(prece)
        return "Товар с таким именем не найден."

    def sort_by_name(self):
        """Сортировка товаров по названию."""
        self.__preces.sort(key=lambda prece: prece.get_name())

    def sort_by_veikals(self):
        """Сортировка товаров по названию магазина."""
        self.__preces.sort(key=lambda prece: prece.get_veikals_name())

    def sort_by_price(self):
        """Сортировка товаров по цене."""
        self.__preces.sort(key=lambda prece: prece.get_price())

    def __str__(self):
        """Вывод всех товаров на складе."""
        return "\n".join([str(prece) for prece in self.__preces])


# Пример использования:

# Создаём товары
prece1 = Prece("Яблоки", "Maxima", 1.25)
prece2 = Prece("Картошка", "RIMI", 1)
prece3 = Prece("Морковь", "Mego", 0.80)

# Создаём склад
noliktava = Noliktava()

# Добавляем товары на склад
noliktava.add_prece(prece1)
noliktava.add_prece(prece2)
noliktava.add_prece(prece3)

# Вывод товаров
print("Все товары на складе:")
print(noliktava)

# Поиск товара по индексу
print("\nТовар по индексу 1:")
print(noliktava.get_prece_by_index(1))

# Поиск товара по имени
print("\nТовар по имени 'Яблоки':")
print(noliktava.get_prece_by_name("Яблоки"))

# Сортировка товаров по названию
noliktava.sort_by_name()
print("\nТовары после сортировки по названию:")
print(noliktava)

# Сортировка товаров по цене
noliktava.sort_by_price()
print("\nТовары после сортировки по цене:")
print(noliktava)

noliktava.sort_by_veikals()
print("\nТовары после сортировки по магазинам:")
print(noliktava)

# Сложение товаров по цене
total_price = prece1 + prece2
print(f"\nСумма стоимости товаров {prece1.get_name()} и {prece2.get_name()}: {total_price} евро.")


