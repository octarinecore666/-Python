import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()  # Selenium сам загрузит GeckoDriver
    yield driver
    driver.quit()
    # 1. Зайти на сайт


def test_shop_purchase(driver):
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизация
    # Ввод имени пользователя
    username_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "user-name"))
    )
    username_field.clear()
    username_field.send_keys("standard_user")

    # Ввод пароля
    password_field = driver.find_element(By.ID, "password")
    password_field.clear()
    password_field.send_keys("secret_sauce")

    # Нажатие кнопки Login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # 3. Добавление товаров в корзину
    # Sauce Labs Backpack
    backpack_add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    backpack_add_button.click()

    # Sauce Labs Bolt T-Shirt
    tshirt_add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
    )
    tshirt_add_button.click()

    # Sauce Labs Onesie
    onesie_add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))
    )
    onesie_add_button.click()

    # 4. Переход в корзину
    cart_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart_icon.click()

    # 5. Нажатие Checkout
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

    # 6. Заполнение формы
    first_name_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "first-name"))
    )
    first_name_field.clear()
    first_name_field.send_keys("Юлия")

    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.clear()
    last_name_field.send_keys("Косарева")

    zip_code_field = driver.find_element(By.ID, "postal-code")
    zip_code_field.clear()
    zip_code_field.send_keys("630000")

    # 7. Нажатие Continue
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    # 8. Чтение итоговой стоимости
    total_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text  # например, "Total: $58.29"

    # Извлекаем числовую часть из строки
    total_amount_str = total_text.split("$")[1]  # получаем "58.29"
    total_amount = float(total_amount_str)

    # 9. Проверка итоговой суммы
    expected_total = 58.29
    assert (
        abs(total_amount - expected_total) < 0.01
    ), f"Ожидалась сумма ${expected_total}, но получена ${total_amount}"

    print(f"Тест пройден: итоговая сумма корректна — ${total_amount}")
