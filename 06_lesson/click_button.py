from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Инициализация драйвера (укажите путь к chromedriver, если он не в PATH)
driver = webdriver.Chrome()  # или webdriver.Firefox() и т. п.

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Ожидание появления кнопки и клик по ней
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ajaxButton"))
    )
    button.click()

    # Ожидание появления зелёной плашки с текстом
    success_message = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )

    # Получение текста и вывод в консоль
    text = success_message.text
    print(text)

except TimeoutException as e:
    print("Элемент не появился в отведённое время:", e)
except Exception as e:
    print("Произошла ошибка:", e)
finally:
    # Закрытие браузера
    driver.quit()
