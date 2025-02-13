import os


class RowingBoat:
    """Реализация класса вёсельной лодки"""

    def __init__(self):
        self.rowers = []  # Добавление гребца в лодку
        self.speed = 0.0  # Установка скорости при гребле
        self.position = 0.0
        self.is_rowing = False

    def add_rower(self, rower: str) -> None:
        """Добавление гребца в лодку"""
        self.rowers.append(rower)

    def remove_rower(self, rower: str) -> None:
        """Удаление гребца из лодки"""
        self.rowers.remove(rower)

    def start_rowing(self) -> None:
        """Запуск процесса гребли"""
        if not self.is_rowing:
            self.is_rowing = True
            self.speed = 5.0

    def stop_rowing(self):
        if self.is_rowing:
            self.is_rowing = False
            self.speed = 0.0

    def get_speed(self) -> float:
        """Получение скорости движения лодки"""
        return self.speed

    def move(self):
        if self.is_rowing:
            self.position += self.speed

    def get_position(self) -> float:
        return self.position
