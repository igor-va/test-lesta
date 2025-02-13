import allure
import pytest


pytestmark = [pytest.mark.api]


@allure.feature("Тестирование лодки")
@allure.story("Системные тесты")
@pytest.mark.system
class TestSystem:
    """Системные тесты"""

    @allure.title("Запуск гребли")
    @allure.description("Запуск процесса гребли на лодке")
    @pytest.mark.st3
    def test_start_rowing(self, boat) -> None:
        """Запуск процесса гребли на лодке"""
        with allure.step(f"Запуск процесса гребли"):
            boat.start_rowing()
        with allure.step(f"Проверка, что процесс гребли запущен"):
            assert boat.is_rowing is True
        with allure.step(f"Проверка, что лодка имеет скорость движения"):
            assert boat.get_speed() == 5.0
