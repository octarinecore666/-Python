from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


try:
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(2)

    # 1. Ввод логина и пароля
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # 2. Поиск кнопки Login (альтернативные варианты)
    try:
        # Вариант 1: поиск по тексту
        login_button = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Login')]"
        )
    except:
        try:
            # Вариант 2: поиск по классу иконки
            login_button = driver.find_element(By.CSS_SELECTOR, "i.fa-sign-in")
        except:
            # Вариант 3: поиск внутри формы
            form = driver.find_element(By.TAG_NAME, "form")
            login_button = form.find_element(By.TAG_NAME, "button")

    # 3. Клик по кнопке
    login_button.click()

    # 4. Получение alt-текста зелёной плашки
    green_badge = driver.find_element(By.CSS_SELECTOR, "a[href*='github.com'] > img")
    alt_text = green_badge.get_attribute("alt")
    print("Текст с зелёной плашки (alt):")
    print(alt_text)

finally:
    time.sleep(3)
    driver.quit()
