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
        with allure.step(f"Проверка, что скорость движения лодки больше 0"):
            assert boat.get_speed() > 0.0, f"Ошибка, скорость движения лодки не больше 0"

    @allure.title("Остановка гребли")
    @allure.description("Остановка процесса гребли на лодке")
    @pytest.mark.st4
    def test_stop_rowing(self, boat) -> None:
        """Остановка процесса гребли на лодке"""
        with allure.step(f"Запуск процесса гребли"):
            boat.start_rowing()
        with allure.step(f"Остановка процесса гребли"):
            boat.stop_rowing()
        with allure.step(f"Проверка, что процесс гребли остановлен"):
            assert boat.is_rowing is False
        with allure.step(f"Проверка, что скорость движения лодки равно 0"):
            assert boat.get_speed() == 0.0, f"Ошибка, скорость движения лодки не равно 0"
