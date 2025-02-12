import allure
import pytest


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
            rower = "Иван"
        with allure.step(f"Добавление гребца в лодку"):
            boat.add_rower(rower)
        with allure.step(f"Проверка, что гребец добавлен в лодку"):
            assert rower in boat.rowers
