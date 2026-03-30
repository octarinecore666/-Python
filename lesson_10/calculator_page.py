from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver: webdriver.Remote) -> None:
        """
        Инициализация страницы калькулятора.

        Args:
            driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.delay_field = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self) -> None:
        """
        Открыть страницу калькулятора и дождаться загрузки.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.screen)
        )

    def set_delay(self, delay_value: int) -> None:
        """
        Установить значение задержки.

        Args:
            delay_value: Значение задержки в секундах (целое число)
        """
        delay_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delay_field)
        )
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def click_button(self, button_text: str) -> None:
        """
        Нажать кнопку калькулятора по тексту.

        Args:
            button_text: Текст на кнопке (например, "7", "+", "=")
        """
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//span[contains(@class, 'btn') and contains(text(), '{button_text}')]",
                )
            )
        )
        button.click()

    def get_result(self) -> str:
        """
        Получить текущий результат из экрана калькулятора.

        Returns:
            Текст результата на экране калькулятора (строка)
        """
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(self.screen, "15")
        )
        return self.driver.find_element(*self.screen).text
