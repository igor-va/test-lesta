import os


class RowingBoat(object):
    """Реализация класса вёсельной лодки"""

    def __init__(self):
        self.rowers = []  # Гребцы в лодке
        self.speed = 0.0  # Текущая скорость лодки
        self.position = 0.0  # Позиция лодки
        self.is_rowing = False  # Процесс гребли

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

    def stop_rowing(self) -> None:
        """Остановка процесса гребли"""
        if self.is_rowing:
            self.is_rowing = False
            self.speed = 0.0

    def get_speed(self) -> float:
        """Получение текущей скорости движения лодки"""
        return self.speed

    def move(self) -> None:
        """Изменение позиции лодки"""
        if self.is_rowing:
            self.position += self.speed

    def get_position(self) -> float:
        """Получение текущей позиции лодки"""
        return self.position
