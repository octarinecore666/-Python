import pytest
import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    """Инициализация драйвера Chrome"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Тест калькулятора с задержкой")
@allure.description(
    "Проверка корректности расчёта на калькуляторе с установкой задержки"
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    """Тест калькулятора с задержкой, использующий Page Object"""
    calculator_page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator_page.open()

    with allure.step("Установить задержку 45 секунд"):
        calculator_page.set_delay(45)

    with allure.step("Нажать кнопки: 7, +, 8, ="):
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")

    with allure.step("Получить результат и проверить его"):
        result = calculator_page.get_result()
        assert result == "15", f"Ожидался результат '15', но получен '{result}'"
