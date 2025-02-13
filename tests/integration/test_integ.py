import allure
import pytest


pytestmark = [pytest.mark.api]


@allure.feature("Тестирование лодки")
@allure.story("Интеграционные тесты")
@pytest.mark.integ
class TestIntegration:
    """Интеграционные тесты"""

    @allure.title("Движение лодки")
    @allure.description("Запустить греблю и проверить изменение позиции лодки")
    @pytest.mark.it3
    def test_move(self, boat) -> None:
        """Запустить греблю и проверить изменение позиции лодки"""
        with allure.step(f"Запуск процесса гребли"):
            boat.start_rowing()
        with allure.step(f"Изменение позиции лодки"):
            boat.move()
        with allure.step(f"Проверка, что позиция лодки изменилась на величину скорости"):
            assert boat.get_position() == 5.0
