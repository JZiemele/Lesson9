class Bus:
    def __init__(self, max_seats, max_speed):
        """Инициализация автобуса с максимальным количеством мест и максимальной скоростью."""
        self.speed = 0  # Начальная скорость автобуса
        self.max_seats = max_seats  # Максимальное количество посадочных мест
        self.max_speed = max_speed  # Максимальная скорость автобуса
        self.passengers = []  # Список фамилий пассажиров
        self.free_seats_flag = True  # Флаг наличия свободных мест
        self.seats = {i: None for i in range(1, max_seats + 1)}  # Словарь мест в автобусе (место -> фамилия)

    def check_free_seats(self):
        """Проверяет наличие свободных мест."""
        self.free_seats_flag = None in self.seats.values()

    def board_passenger(self, passenger_name):
        """Посадка одного пассажира."""
        if self.free_seats_flag:
            for seat, occupant in self.seats.items():
                if occupant is None:
                    self.seats[seat] = passenger_name
                    self.passengers.append(passenger_name)
                    break
            self.check_free_seats()
        else:
            print(f"Нет свободных мест для пассажира {passenger_name}.")

    def disembark_passenger(self, passenger_name):
        """Высадка одного пассажира."""
        if passenger_name in self.passengers:
            for seat, occupant in self.seats.items():
                if occupant == passenger_name:
                    self.seats[seat] = None
                    break
            self.passengers.remove(passenger_name)
            self.check_free_seats()
        else:
            print(f"Пассажира с фамилией {passenger_name} нет в автобусе.")

    def change_speed(self, value):
        """Увеличение или уменьшение скорости автобуса."""
        self.speed = max(0, min(self.speed + value, self.max_speed))  # Скорость не может быть меньше 0 или больше максимальной
        print(f"Текущая скорость автобуса: {self.speed} км/ч")

    # Оператор in для проверки, находится ли пассажир в автобусе
    def __contains__(self, passenger_name):
        return passenger_name in self.passengers

    # Оператор += для посадки пассажира
    def __iadd__(self, passenger_name):
        self.board_passenger(passenger_name)
        return self

    # Оператор -= для высадки пассажира
    def __isub__(self, passenger_name):
        self.disembark_passenger(passenger_name)
        return self

    def __str__(self):
        """Строковое представление автобуса."""
        return f"Автобус движется со скоростью {self.speed} км/ч. Пассажиры: {', '.join(self.passengers) if self.passengers else 'нет пассажиров'}."


# Пример использования:
bus = Bus(max_seats=5, max_speed=100)

# Посадка пассажиров
bus += "Иванов"
bus += "Петров"
bus += "Сидоров"

# Проверка пассажиров
print(f"Иванов в автобусе: {'Иванов' in bus}")
print(f"Фамилии пассажиров: {bus.passengers}")

# Изменение скорости
bus.change_speed(60)  # Увеличение скорости
bus.change_speed(-20)  # Уменьшение скорости

# Высадка пассажира
bus -= "Петров"
print(bus)

# Попытка высадить пассажира, которого нет в автобусе
bus -= "Николаев"

# Вывод состояния автобуса
print(bus)


class Bus:
    def __init__(self, max_seats, max_stops):
        self.seats = {i: None for i in range(1, max_seats + 1)}  # Словарь мест (место -> пассажир)
        self.max_stops = max_stops  # Максимальное количество остановок
        self.passenger_info = {}  # Словарь с информацией о пассажирах: (пассажир -> (остановка посадки, остановка выхода))
        self.free_seats_flag = True  # Изначально есть свободные места

    def board_passenger(self, passenger_name, boarding_stop, exit_stop):
        """Посадка пассажира, который купил билет."""
        if not self.free_seats_flag:
            print(f"Мест нет! {passenger_name} не может сесть в автобус.")
            return

        # Проверяем, что остановки корректны
        if boarding_stop < 1 or exit_stop > self.max_stops or boarding_stop >= exit_stop:
            print(f"Ошибка в остановках для {passenger_name}: некорректные данные.")
            return

        # Ищем свободное место
        for seat, passenger in self.seats.items():
            if passenger is None:
                self.seats[seat] = passenger_name
                self.passenger_info[passenger_name] = (boarding_stop, exit_stop)
                print(f"{passenger_name} купил(а) билет и сел(а) на место {seat}.")
                break

        # Проверяем, остались ли свободные места
        if all(self.seats[seat] is not None for seat in self.seats):
            self.free_seats_flag = False  # Все места заняты

    def passenger_without_ticket(self, passenger_name, boarding_stop, exit_stop):
        """Посадка пассажира без билета при наличии мест."""
        if not self.free_seats_flag:
            print(f"Мест нет! {passenger_name} не может сесть в автобус.")
            return

        # Проверяем, что остановки корректны
        if boarding_stop < 1 or exit_stop > self.max_stops or boarding_stop >= exit_stop:
            print(f"Ошибка в остановках для {passenger_name}: некорректные данные.")
            return

        # Если места есть, сажаем пассажира без билета
        for seat, passenger in self.seats.items():
            if passenger is None:
                self.seats[seat] = passenger_name
                self.passenger_info[passenger_name] = (boarding_stop, exit_stop)
                print(f"{passenger_name} сел(а) в автобус без билета на место {seat}.")
                break

        # Проверяем, остались ли свободные места
        if all(self.seats[seat] is not None for seat in self.seats):
            self.free_seats_flag = False  # Все места заняты

    def disembark_passenger(self, stop):
        """Высадка пассажиров на остановке."""
        for passenger, (boarding_stop, exit_stop) in list(self.passenger_info.items()):
            if exit_stop == stop:
                # Ищем место, где сидит пассажир, и освобождаем его
                for seat, current_passenger in self.seats.items():
                    if current_passenger == passenger:
                        self.seats[seat] = None
                        self.free_seats_flag = True  # Место освободилось
                        print(f"{passenger} вышел(а) на остановке {stop}.")
                        break
                # Удаляем информацию о пассажире
                del self.passenger_info[passenger]

    def show_passenger_info(self):
        """Показать информацию о пассажирах."""
        for passenger, (boarding_stop, exit_stop) in self.passenger_info.items():
            print(f"Пассажир {passenger}: сядет на остановке {boarding_stop}, выйдет на остановке {exit_stop}.")


# Пример использования:
bus = Bus(max_seats=3, max_stops=5)

# Пассажиры покупают билеты и садятся
bus.board_passenger("Иванов", 1, 3)
bus.board_passenger("Петров", 1, 4)
bus.board_passenger("Сидоров", 2, 5)

# Показать текущую информацию о пассажирах
print("\nИнформация о пассажирах:")
bus.show_passenger_info()

# Пассажир без билета хочет сесть
bus.passenger_without_ticket("Кузнецов", 2, 4)  # Мест нет, пассажира не посадят

# Высадка пассажиров на остановке 3
print("\nОстановка 3:")
bus.disembark_passenger(3)

# Показать информацию после высадки
print("\nИнформация после высадки:")
bus.show_passenger_info()

# Пассажир без билета снова пробует сесть (после высадки место освободилось)
bus.passenger_without_ticket("Кузнецов", 3, 5)

# Показать информацию о пассажирах
print("\nИнформация о пассажирах:")
bus.show_passenger_info()