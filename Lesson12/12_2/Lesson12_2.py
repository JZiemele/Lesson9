import random


class BeeElephant:
    def __init__(self, bee_part, elephant_part):
        """Инициализация частей пчелы и слона."""
        self.bee_part = max(0, min(bee_part, 100))  # Ограничиваем значения от 0 до 100
        self.elephant_part = max(0, min(elephant_part, 100))  # Ограничиваем значения от 0 до 100

    def fly(self):
        """Возвращает True, если часть пчелы не меньше части слона."""
        if self.bee_part >= self.elephant_part:
            return 'Существо может летать'
        return 'Существо летать не может'

    def trumpet(self):
        """Возвращает 'tu-tu-doo-doo', если часть слона не меньше части пчелы, иначе 'wzzzz'."""
        if self.elephant_part >= self.bee_part:
            return "Слон задорно трубит: tu-tu-doo-doo"
        else:
            return "Пчёлка весело зажужжала: wzzzz"

    def eat(self, meal, value):
        """Съедает нектар или траву и изменяет части пчелы и слона соответственно."""
        if meal == "nectar":
            # Пчела ест нектар: часть пчелы увеличивается, слона уменьшается
            self.bee_part = min(self.bee_part + value, 100)  # Не больше 100
            self.elephant_part = max(self.elephant_part - value, 0)  # Не меньше 0
        elif meal == "grass":
            # Слон ест траву: часть слона увеличивается, пчелы уменьшается
            self.elephant_part = min(self.elephant_part + value, 100)  # Не больше 100
            self.bee_part = max(self.bee_part - value, 0)  # Не меньше 0
        else:
            raise ValueError("Можно есть только 'nectar' или 'grass'.")


def play_game():
    # Инициализируем существо
    creature = BeeElephant(bee_part=50, elephant_part=50)
    print(f'Пчела = {creature.bee_part}, Слон = {creature.elephant_part}')

    while creature.bee_part < 100 and creature.elephant_part < 100:
        # Рандомно выбираем еду: "nectar" или "grass"
        meal = random.choice(["nectar", "grass"])
        # Рандомное количество еды от 1 до 30
        value = random.randint(1, 30)


        # Существо ест
        creature.eat(meal, value)


        # Выводим состояние после еды
        print(f"\n{meal.title()} ({value} ед.): Пчела = {creature.bee_part}, Слон = {creature.elephant_part}")
        print("Состояние:", creature.fly())
        print("Звук существа:", creature.trumpet())

        # Проверка, если кто-то набрал 100 очков
        if creature.bee_part == 100:
            print("\nПчела выиграла, достигнув 100 очков!")
            break
        elif creature.elephant_part == 100:
            print("\nСлон выиграл, достигнув 100 очков!")
            break


# Запускаем игру
play_game()