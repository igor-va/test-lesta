import allure
import pytest

from utilities.generic_utilities import *


pytestmark = [pytest.mark.api]


@allure.feature("Тестирование лодки")
@allure.story("Функциональные тесты")
@pytest.mark.func
class TestFunctional:
    """Функциональные тесты"""

    @allure.title("Добавление гребца")
    @allure.description("Добавление гребца в лодку")
    @pytest.mark.ft1
    def test_add_rower(self, boat) -> None:
        """Добавление гребца в лодку"""
        with allure.step(f"Создание тестовых данных"):
            rower = generate_random_name()
        with allure.step(f"Добавление гребца в лодку"):
            boat.add_rower(rower)
        with allure.step(f"Проверка, что гребец добавлен в лодку"):
            assert rower in boat.rowers, f"Ошибка, гребец не был добавлен в лодку"

    @allure.title("Удаление гребца")
    @allure.description("Удаление гребца из лодки")
    @pytest.mark.ft2
    def test_remove_rower(self, boat) -> None:
        """Удаление гребца из лодки """
        with allure.step(f"Создание тестовых данных"):
            rower = generate_random_name()
        with allure.step(f"Добавление гребца в лодку"):
            boat.add_rower(rower)
        with allure.step(f"Удаление гребца из лодки"):
            boat.remove_rower(rower)
        with allure.step(f"Проверка, что гребец удален из лодки"):
            assert rower not in boat.rowers, f"Ошибка, гребец не был удален из лодки"
