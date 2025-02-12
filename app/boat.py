import os


class RowingBoat:
    """Реализация класса вёсельной лодки"""

    def __init__(self):
        self.rowers = []

    def add_rower(self, rower: str) -> None:
        """Добавление гребца в лодку"""
        self.rowers.append(rower)


