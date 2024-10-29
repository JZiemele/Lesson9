import time
import os


class Bus:
    def __init__(self, max_seats):
        self.seats = {i: None for i in range(1, max_seats + 1)}  # Словарь мест (место -> пассажир)

    def board_passenger(self, passenger_name):
        """Посадка пассажира на свободное место."""
        for seat, passenger in self.seats.items():
            if passenger is None:  # Если место свободно
                self.seats[seat] = passenger_name
                break

    def disembark_passenger(self, passenger_name):
        """Высадка пассажира."""
        for seat, passenger in self.seats.items():
            if passenger == passenger_name:
                self.seats[seat] = None
                break

    def display_bus(self):
        """Отображение состояния автобуса в консоли."""

        print("Состояние автобуса:")
        for seat, passenger in self.seats.items():
            if passenger is None:
                print(f"[Место {seat}: Свободно]")
            else:
                print(f"[Место {seat}: {passenger}]")
        print("\n")


# Пример использования:
bus = Bus(max_seats=5)

# Цикл заполнения автобуса
for passenger in ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов"]:
    bus.board_passenger(passenger)
    bus.display_bus()  # Отображаем автобус
    time.sleep(1)  # Задержка в 1 секунду

# Цикл высадки пассажиров
for passenger in ["Иванов", "Петров", "Сидоров"]:
    bus.disembark_passenger(passenger)
    bus.display_bus()  # Отображаем автобус
    time.sleep(1)  # Задержка в 1 секунду