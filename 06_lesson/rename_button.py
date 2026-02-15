from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Инициализация драйвера (укажите путь к chromedriver, если он не в PATH)
driver = webdriver.Chrome()  # или webdriver.Firefox() и т. п.

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/textinput")

    # Находим поле ввода и вводим текст "SkyPro"
    input_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "newButtonName"))
    )
    input_field.send_keys("SkyPro")

    # Находим синюю кнопку и кликаем по ней
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Ожидаем, что текст кнопки обновился (содержит "SkyPro")
    updated_button = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )

    # Получаем актуальный текст кнопки
    button_text = driver.find_element(By.ID, "updatingButton").text
    print(button_text)

except TimeoutException as e:
    print("Элемент не появился в отведённое время:", e)
except Exception as e:
    print("Произошла ошибка:", e)
finally:
    # Закрытие браузера
    driver.quit()
