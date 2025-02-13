import pytest

from app.boat import RowingBoat


@pytest.fixture
def boat():
    """Создание экземпляра класса вёсельной лодки"""
    return RowingBoat()
