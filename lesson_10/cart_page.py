from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver: webdriver.Remote) -> None:
        """
        Инициализация страницы корзины.

        Args:
            driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self) -> None:
        """
        Нажать кнопку Checkout.
        """
        checkout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        checkout_btn.click()
