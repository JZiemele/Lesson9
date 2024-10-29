class Product:
    def __init__(self, product_name, unit_of_measure, product_weight, product_price_unit):
        self.__product_name = product_name
        self.__unit_of_measure = unit_of_measure
        self.__product_weight = max(0, min(product_weight, 100))  # Ограничиваем вес от 0 до 100
        self.__product_price_unit = product_price_unit

    def get_product_name(self):
        return self.__product_name

    def get_unit_of_measure(self):
        return self.__unit_of_measure

    def get_product_weight(self):
        return self.__product_weight

    def get_product_price_unit(self):
        return self.__product_price_unit

    # Метод для увеличения веса
    def add_weight(self, weight):
        self.__product_weight = min(self.__product_weight + weight, 100)

    # Метод для вычитания веса
    def subtract_weight(self, weight):
        if self.__product_weight >= weight:
            self.__product_weight -= weight
        else:
            raise ValueError("Недостаточно товара для вычитания.")

    # Метод для вывода информации о товаре
    def __str__(self):
        total_price = self.__product_weight * self.__product_price_unit
        return (f"Товар: {self.__product_name}, Количество: {self.__product_weight} {self.__unit_of_measure}, "
                f"Цена за единицу: {self.__product_price_unit} евро, Общая сумма: {total_price:.2f} евро")


class Structure:
    def __init__(self, company_name, structure_name, structure_address):
        self.__company_name = company_name
        self.__structure_name = structure_name
        self.__structure_address = structure_address
        self.__products = []

    def get_company_name(self):
        return self.__company_name

    def get_structure_name(self):
        return self.__structure_name

    def get_structure_address(self):
        return self.__structure_address

    def add_product(self, product):
        """Добавление товара на склад."""
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise ValueError("Можно добавлять только объекты класса Product.")

    def get_products_by_index(self, index):
        """Вывод информации о товаре по индексу."""
        if 0 <= index < len(self.__products):
            return str(self.__products[index])
        else:
            return "Товар с таким индексом не найден."

    def get_products_by_product_name(self, product_name):
        """Вывод информации о товаре по имени."""
        for product in self.__products:
            if product.get_product_name() == product_name:
                return str(product)
        return "Товар с таким именем не найден."

    def sort_by_product_name(self):
        """Сортировка товаров по названию."""
        self.__products.sort(key=lambda product: product.get_product_name())

    def sort_by_product_price(self):
        """Сортировка товаров по цене за единицу."""
        self.__products.sort(key=lambda product: product.get_product_price_unit())

    def transfer_product(self, product_name, quantity, target_structure):
        """Перемещение товара из одной структуры в другую."""
        for product in self.__products:
            if product.get_product_name() == product_name:
                if product.get_product_weight() >= quantity:
                    product.subtract_weight(quantity)
                    new_product = Product(product_name, product.get_unit_of_measure(), quantity, product.get_product_price_unit())
                    target_structure.add_product(new_product)
                    print(f"{quantity} {product.get_unit_of_measure()} товара '{product_name}' перемещено из {self.get_structure_name()} в {target_structure.get_structure_name()}.")
                else:
                    print(f"Недостаточно товара '{product_name}' для перемещения.")
                return
        print(f"Товар '{product_name}' не найден в {self.get_structure_name()}.")

    def __str__(self):
        """Вывод всех товаров на складе."""
        return f"Магазин: {self.__structure_name}\n" + "\n".join([str(product) for product in self.__products])

    @staticmethod
    def find_unique_products_with_total(structures):
        """Найти уникальные товары по всем структурам и вывести их общий вес и стоимость."""
        product_totals = {}

        # Проход по всем структурам
        for structure in structures:
            for product in structure._Structure__products:
                product_key = product.get_product_name()
                # Если товара с таким именем ещё нет в словаре, добавляем его
                if product_key not in product_totals:
                    product_totals[product_key] = {
                        "total_weight": 0,
                        "total_sum": 0,
                        "price_per_unit": product.get_product_price_unit(),
                        "unit_of_measure": product.get_unit_of_measure()
                    }
                # Суммируем вес и общую сумму, выводим среднеарифметическую цену за штуку
                product_totals[product_key]["total_weight"] += product.get_product_weight()
                product_totals[product_key][
                    "total_sum"] += product.get_product_weight() * product.get_product_price_unit()
                product_totals[product_key]["price_per_unit"] =  round(product_totals[product_key][
                    "total_sum"] / product_totals[product_key]["total_weight"], 2)
                # Выводим информацию о товаре в текущей структуре
                print(
                    f"{structure.get_structure_name()}: {product.get_product_name()} {product.get_product_weight()} "
                    f"{product.get_unit_of_measure()}, цена {product.get_product_price_unit()} евро")

        # Вывод общей информации по каждому уникальному товару
        print("\nИтоги по всем структурам:")
        for product_name, info in product_totals.items():
            print(
                f"{product_name}: {info['total_weight']} {info['unit_of_measure']}, цена {info['price_per_unit']} евро, общая сумма {info['total_sum']:.2f} евро")
    @staticmethod
    def get_total_weight_and_sum(structures):
        """Возвращает общий вес и общую сумму товаров по всем магазинам."""
        total_weight = 0
        total_sum = 0
        for structure in structures:
            for product in structure.__products:
                total_weight += product.get_product_weight()
                total_sum += product.get_product_weight() * product.get_product_price_unit()
        return total_weight, total_sum


# Пример использования:

# Создаём товары
product1 = Product('Морковь', 'кг', 5, 0.85)
product2 = Product('Картофель', 'кг', 50, 0.30)
product3 = Product('Бананы', 'кг', 30, 1.69)
product4 = Product('Свёкла', 'кг', 3, 0.61)
product5 = Product('Бананы', 'кг', 10, 1.00)

# Создаём склады
structure1 = Structure('AIBE', 'Noliktava', 'Bukaišu iela 2, Rīga, LV1004')
structure2 = Structure('AIBE', 'MAXIMA', 'Kurzemes prospekts 1, Rīga, LV1010')
structure3 = Structure('AIBE', 'RIMI', 'Kurzemes prospekts 80, Rīga, LV1010')
# Добавляем товары на склад
structure1.add_product(product1)
structure1.add_product(product2)
structure1.add_product(product3)
structure1.add_product(product5)

print(structure1)

# Перемещение товара из Noliktava в MAXIMA
print("\n")
structure1.transfer_product('Картофель', 20, structure2)
structure1.transfer_product('Бананы', 20, structure2)
structure1.transfer_product('Морковь', 6, structure3)
structure1.transfer_product('Картофель', 10, structure3)
structure1.transfer_product('Яблоки', 1, structure2)
# Проверяем после перемещения
print("\nПосле перемещения:")
print(structure1)
print(structure2)
print(structure3)

print(f"\n{structure1.get_structure_name()} Товар по индексу 1:")
print(structure1.get_products_by_index(1))


print(f"\n{structure2.get_structure_name()} Товар по индексу 0:")
print(structure2.get_products_by_index(1))

# Поиск товара по имени
print(f"\n{structure2.get_structure_name()} Товар по имени 'Картофель':")
print(structure2.get_products_by_product_name("Картофель"))

# Сортировка товаров по названию
structure1.sort_by_product_name()
print(f"\n{structure1.get_structure_name()} Товары после сортировки по названию:")
print(structure1)

# Сортировка товаров по цене
structure1.sort_by_product_price()
print(f"\n{structure1.get_structure_name()} Товары после сортировки по цене:")
print(structure1)


structures = [structure1, structure2, structure3 ]

print("\nВсе товары по всем магазинам:")
Structure.find_unique_products_with_total(structures)


total_weight, total_sum = Structure.get_total_weight_and_sum(structures)
print(f"\nОбщий вес всех товаров: {total_weight} кг")
print(f"Общая сумма всех товаров: {total_sum:.2f} евро")