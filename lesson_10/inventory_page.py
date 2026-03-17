from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver: webdriver.Remote) -> None:
        """
        Инициализация страницы товаров.

        Args:
            driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self) -> None:
        """
        Добавить рюкзак в корзину.
        """
        backpack_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        backpack_btn.click()

    def add_tshirt_to_cart(self) -> None:
        """
        Добавить футболку в корзину.
        """
        tshirt_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
        )
        tshirt_btn.click()

    def add_onesie_to_cart(self) -> None:
        """
        Добавить комбинезон в корзину.
        """
        onesie_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))
        )
        onesie_btn.click()

    def go_to_cart(self) -> None:
        """
        Перейти в корзину.
        """
        cart_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon)
        )
        cart_btn.click()
