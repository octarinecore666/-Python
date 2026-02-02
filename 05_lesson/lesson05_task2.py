from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Инициализация драйвера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Открыть страницу
    driver.get("http://uitestingplayground.com/dynamicid")
    time.sleep(2)  # Базовое ожидание загрузки

    # Найти кнопку по классам (стабильные атрибуты)
    button = driver.find_element(
        By.CSS_SELECTOR,
        "button.btn.btn-primary"
    )

    # Кликнуть по кнопке
    button.click()
    print("Кнопка нажата успешно!")

finally:
    time.sleep(3)
    driver.quit()
