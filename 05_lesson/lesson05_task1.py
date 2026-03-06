from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Инициализация драйвера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Открыть страницу
    driver.get("http://uitestingplayground.com/classattr")
    time.sleep(2)  # Ожидание загрузки

    # Найти кнопку
    button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-test")

    # Проверить border-color
    border_color = button.value_of_css_property("border-color")
    expected_color = "rgb(0, 123, 255)"  # #007bff в RGB

    if border_color.lower() != expected_color.lower():
        print(f"Ошибка: цвет границы кнопки не соответствует ожидаемому.")
        print(f"Ожидается: {expected_color}, получено: {border_color}")
    else:
        print("Цвет границы кнопки корректен (#007bff).")
        # Кликнуть по кнопке
        button.click()
        print("Кнопка нажата успешно!")


finally:
    time.sleep(3)
    driver.quit()
