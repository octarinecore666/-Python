from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

# Инициализация драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/inputs")
    time.sleep(2)  # Ожидание загрузки

    # Найти поле ввода (тип number)
    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

    # 1. Ввести текст "Sky"
    input_field.send_keys("Sky")
    print("Введено: Sky")

    # 2. Очистить поле
    input_field.clear()
    print("Поле очищено")

    # 3. Ввести текст "Pro"
    input_field.send_keys("Pro")
    print("Введено: Pro")

finally:
    # Закрыть браузер через 3 секунды
    time.sleep(3)
    driver.quit()
