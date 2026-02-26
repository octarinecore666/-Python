import pytest
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    """Инициализация драйвера Firefox"""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop_purchase(driver):
    """Тест покупки в интернет‑магазине с использованием Page Object"""

    # Создаём объекты страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Открываем сайт магазина
    login_page.open()

    # 2. Авторизуемся как standard_user
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # 3. Добавляем товары в корзину
    inventory_page.add_backpack_to_cart()
    inventory_page.add_tshirt_to_cart()
    inventory_page.add_onesie_to_cart()

    # 4. Переходим в корзину
    inventory_page.go_to_cart()

    # 5. Нажимаем Checkout
    cart_page.click_checkout()

    # 6. Заполняем форму своими данными
    checkout_page.fill_personal_info("Юлия", "Косарева", "630000")

    # 7. Нажимаем Continue
    checkout_page.click_continue()

    # 8. Получаем итоговую стоимость и проверяем её
    total_amount = checkout_page.get_total_amount()
    expected_total = 58.29
    assert (
        abs(total_amount - expected_total) < 0.01
    ), f"Ожидалась сумма ${expected_total}, но получена ${total_amount}"

    print(f"Тест пройден: итоговая сумма корректна — ${total_amount}")
