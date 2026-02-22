import pytest
from selenium import webdriver
from selenium.webdriver.common.by import Bycd 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    """Инициализация драйвера Chrome"""
    driver = webdriver.Chrome()  # Selenium автоматически загрузит драйвер
    yield driver
    driver.quit()

def test_calculator(driver):
    """Тест калькулятора с задержкой"""

    # 1. Открытие страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. Ввод значения задержки (45 секунд) в поле #delay
    delay_field = driver.find_element(By.ID, "delay")
    delay_field.clear()
    delay_field.send_keys("45")

    # 3. Нажатие на кнопки калькулятора
    # Кнопка "7"
    seven_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']")
        )
    )
    seven_button.click()

    # Кнопка "+"
    plus_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[@class='operator btn btn-outline-success' and text()='+']",
            )
        )
    )
    plus_button.click()

    # Кнопка "8"
    eight_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']")
        )
    )
    eight_button.click()

    # Кнопка "="
    equals_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']")
        )
    )
    equals_button.click()

    # 4. Проверка результата через 45 секунд
    result_element = WebDriverWait(driver, 50).until(  # Увеличили таймаут до 50 с
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    # Assert для проверки результата
    screen_element = driver.find_element(By.CLASS_NAME, "screen")
    assert (
        screen_element.text == "15"
    ), f"Ожидался результат '15', но получен '{screen_element.text}'"

    print("Тест пройден: результат расчёта верен!")
