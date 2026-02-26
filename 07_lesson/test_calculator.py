import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    """Инициализация драйвера Chrome"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(driver):
    """Тест калькулятора с задержкой, использующий Page Object"""

    # Создаём объект страницы калькулятора
    calculator_page = CalculatorPage(driver)

    # 1. Открываем страницу калькулятора
    calculator_page.open()

    # 2. Устанавливаем задержку 45 секунд
    calculator_page.set_delay(45)

    # 3. Нажимаем кнопки: 7, +, 8, =
    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")

    # 4. Получаем результат и проверяем его
    result = calculator_page.get_result()
    assert result == "15", f"Ожидался результат '15', но получен '{result}'"

    print("Тест пройден: результат расчёта верен!")
