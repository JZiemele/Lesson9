import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

class Bus:
    def __init__(self, max_seats, max_stops, max_speed):
        self.seats = {i: None for i in range(1, max_seats + 1)}  # Словарь мест (место -> пассажир)
        self.max_stops = max_stops  # Максимальное количество остановок
        self.max_speed = max_speed  # Максимальная скорость автобуса
        self.passenger_info = {}  # Словарь с информацией о пассажирах
        self.reserved_seats = set()  # Места, зарезервированные для пассажиров
        self.free_seats_flag = True  # Изначально есть свободные места
        self.speed = 0  # Начальная скорость
        self.without_ticket_passengers = []  # Список безбилетников
        self.rejected_passengers = []  # Список пассажиров, которым отказали в посадке

    def board_passenger(self, passenger_name, boarding_stop, exit_stop):
        """Посадка пассажира, который купил билет на остановке."""
        if not self.free_seats_flag:
            print(f"Мест нет! {passenger_name} не может сесть в автобус.")
            return

        if boarding_stop < 1 or exit_stop > self.max_stops or boarding_stop >= exit_stop:
            print(f"Ошибка в остановках для {passenger_name}: некорректные данные.")
            return

        # Ищем свободное место
        for seat, passenger in self.seats.items():
            if passenger is None and seat not in self.reserved_seats:
                self.reserved_seats.add(seat)
                self.passenger_info[passenger_name] = (boarding_stop, exit_stop, seat)
                print(f"Пассажир {passenger_name} купил билет заранее на остановку {boarding_stop}. Место {seat} зарезервировано (синее).")
                break

        if all(self.seats[seat] is not None for seat in self.seats):
            self.free_seats_flag = False  # Все места заняты

    def check_free_seats(self):
        """Проверяет наличие свободных мест."""
        self.free_seats_flag = None in self.seats.values()

    def add_without_ticket_passenger(self, passenger_name, boarding_stop, exit_stop):
        """Добавляем пассажира, который будет садиться без билета."""
        self.without_ticket_passengers.append((passenger_name, boarding_stop, exit_stop))

    def passenger_without_ticket(self, passenger_name, boarding_stop, exit_stop):
        """Посадка пассажира без билета при наличии мест."""
        if not self.free_seats_flag:
            print(f"Мест нет! {passenger_name} не может сесть в автобус на остановке {boarding_stop}.")
            self.rejected_passengers.append((passenger_name, boarding_stop, exit_stop))
            return

        # Проверка корректности остановок
        if boarding_stop < 1 or exit_stop > self.max_stops or boarding_stop >= exit_stop:
            print(f"Ошибка в остановках для {passenger_name}: некорректные данные.")
            return

        # Если есть свободное место, садим пассажира без билета
        for seat, passenger in self.seats.items():
            if seat in self.reserved_seats:  # Пропускаем зарезервированные места
                continue
            if passenger is None:
                self.seats[seat] = passenger_name
                self.passenger_info[passenger_name] = (boarding_stop, exit_stop, seat)
                print(f"{passenger_name} сел в автобус без билета на место {seat}.")
                break

        if all(self.seats[seat] is not None for seat in self.seats):
            self.free_seats_flag = False  # Все места заняты

    def change_speed(self, value):
        """Увеличение или уменьшение скорости автобуса."""
        self.speed = max(0, min(self.speed + value, self.max_speed))  # Скорость не может быть меньше 0 или больше максимальной
        print(f"Текущая скорость автобуса: {self.speed} км/ч")

    def disembark_passenger(self, stop):
        """Высадка пассажиров на остановке."""
        for passenger, (boarding_stop, exit_stop, seat) in list(self.passenger_info.items()):
            if exit_stop == stop:
                self.seats[seat] = None
                self.reserved_seats.discard(seat)  # Место больше не зарезервировано
                print(f"{passenger} вышел на остановке {stop}.")
                del self.passenger_info[passenger]
                self.check_free_seats()

    def show_passenger_info(self):
        """Показать информацию о пассажирах."""
        for passenger, (boarding_stop, exit_stop, seat) in self.passenger_info.items():
            print(f"Пассажир {passenger}: посадка на остановке {boarding_stop}, "
                  f"высадка на остановке {exit_stop} на месте {seat}.")

    def show_rejected_passengers(self):
        """Показать информацию о пассажирах, которым отказали в посадке."""
        if self.rejected_passengers:
            print("\nПассажиры, которым отказали в посадке:")
            for passenger_name, boarding_stop, exit_stop in self.rejected_passengers:
                print(f"{passenger_name} пытался сесть на остановке {boarding_stop}, но мест не было.")
        else:
            print("\nНет пассажиров, которым отказали в посадке.")

    def seat_passenger(self, stop):
        """Посадка пассажиров на их места при соответствующей остановке."""
        for passenger, (boarding_stop, exit_stop, seat) in self.passenger_info.items():
            if boarding_stop == stop:
                self.seats[seat] = passenger  # Пассажир занимает место
                print(f"{passenger} сел на место {seat} на остановке {stop} (зелёное место).")

    def seat_without_ticket_passenger(self, stop):
        """Посадка безбилетных пассажиров, если они хотят сесть на данной остановке."""
        for passenger_name, boarding_stop, exit_stop in self.without_ticket_passengers[:]:
            if boarding_stop == stop:
                # Пробуем посадить пассажира
                self.passenger_without_ticket(passenger_name, boarding_stop, exit_stop)
                # Если пассажир не смог сесть, добавляем его в rejected_passengers
                if (passenger_name, boarding_stop, exit_stop) not in self.rejected_passengers:
                    # Удаляем пассажира из списка безбилетников только если он получил отказ
                    self.without_ticket_passengers.remove((passenger_name, boarding_stop, exit_stop))

    def show_bus(self, stop):
        """Графическое отображение состояния автобуса."""
        fig, ax = plt.subplots()
        ax.set_xlim(0, 10)
        ax.set_ylim(0, len(self.seats) + 1)
        ax.set_title(f'Остановка {stop}, состояние автобуса')

        for i, (seat, passenger) in enumerate(self.seats.items(), start=1):
            if seat in self.reserved_seats and passenger is None:
                color = 'blue'  # Зарезервировано (синий)
            elif passenger is not None:
                color = 'green'  # Пассажир сидит (зелёный)
            else:
                color = 'white'  # Свободно
            ax.add_patch(patches.Rectangle((1, i), 8, 0.8, edgecolor='black', facecolor=color))
            ax.text(5, i + 0.4, f'{seat}: {passenger if passenger else "Свободно"}', ha='center', va='center')

        plt.show()

    def simulate_trip(self):
        """Симуляция движения автобуса по маршруту."""
        for stop in range(1, self.max_stops + 1):
            print(f"\nОстановка {stop}:")
            self.seat_passenger(stop)  # Пассажиры садятся на своих остановках
            self.disembark_passenger(stop)  # Высадка пассажиров
            self.check_free_seats()
            self.seat_without_ticket_passenger(stop)  # Безбилетники пытаются сесть
            self.show_bus(stop)  # Показать состояние автобуса

            if stop < self.max_stops:
                print(f"Автобус на остановке {stop}. Пассажиры:")
                self.show_passenger_info()
                self.change_speed(40)  # Увеличиваем скорость при выезде с остановки
                time.sleep(1)  # Задержка перед поездкой

                self.change_speed(60)  # Максимальная скорость
                time.sleep(2)  # Едем

                self.change_speed(-60)  # Замедляемся перед остановкой
                time.sleep(1)

                self.change_speed(-self.speed)  # Устанавливает скорость в 0 после остановки

# Пример использования
bus = Bus(max_seats=6, max_stops=5, max_speed=100)

# Пассажиры покупают билеты и садятся
bus.board_passenger("Иванов", 1, 3)
bus.board_passenger("Петров", 1, 4)
bus.board_passenger("Сидоров", 2, 5)
bus.board_passenger("Соловьёв", 1, 2)
bus.board_passenger("Задорнов", 3, 5)
bus.board_passenger("Кристина Молния", 1, 4)
# Добавляем безбилетных пассажиров
bus.add_without_ticket_passenger("Кузнецов", 2, 4)
bus.add_without_ticket_passenger("Хазин", 3, 5)

# Симуляция движения автобуса с остановками и изменениями скорости
bus.simulate_trip()