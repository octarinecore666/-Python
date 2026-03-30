import pytest
import allure
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


@allure.title("Тест покупки в интернет‑магазине")
@allure.description(
    "Полный сценарий покупки: авторизация, добавление товаров в корзину, оформление заказа"
)
@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_purchase(driver):
    """Тест покупки в интернет‑магазине с использованием Page Object"""
    # Создаём объекты страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открыть сайт магазина"):
        login_page.open()

    with allure.step("Авторизоваться как standard_user"):
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    with allure.step("Добавить товары в корзину"):
        inventory_page.add_backpack_to_cart()
        inventory_page.add_tshirt_to_cart()
        inventory_page.add_onesie_to_cart()

    with allure.step("Перейти в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Нажать Checkout"):
        cart_page.click_checkout()

    with allure.step("Заполнить форму личной информации"):
        checkout_page.fill_personal_info("Юлия", "Косарева", "630000")

    with allure.step("Нажать Continue"):
        checkout_page.click_continue()

    with allure.step("Получить итоговую стоимость и проверить её"):
        total_amount = checkout_page.get_total_amount()
        expected_total = 58.29
        assert (
            abs(total_amount - expected_total) < 0.01
        ), f"Ожидалась сумма ${expected_total}, но получена ${total_amount}"

    with allure.step("Проверка успешного завершения покупки"):
        assert total_amount > 0, "Итоговая сумма должна быть положительной"
        print(f"Тест пройден: итоговая сумма корректна — ${total_amount}")
