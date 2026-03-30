from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver: webdriver.Remote) -> None:
        """
        Инициализация страницы оформления заказа.

        Args:
            driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.zip_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_personal_info(
        self, first_name: str, last_name: str, zip_code: str
    ) -> None:
        """
        Заполнить форму личной информации.

        Args:
            first_name: Имя пользователя
            last_name: Фамилия пользователя
            zip_code: Почтовый индекс
        """
        # Имя
        first_name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_name_field)
        )
        first_name_input.clear()
        first_name_input.send_keys(first_name)

        # Фамилия
        last_name_input = self.driver.find_element(*self.last_name_field)
        last_name_input.clear()
        last_name_input.send_keys(last_name)

        # Почтовый индекс
        zip_input = self.driver.find_element(*self.zip_code_field)
        zip_input.clear()
        zip_input.send_keys(zip_code)

    def click_continue(self) -> None:
        """
        Нажать кнопку Continue.
        """
        continue_btn = self.driver.find_element(*self.continue_button)
        continue_btn.click()

    def get_total_amount(self) -> float:
        """
        Получить итоговую сумму.

        Returns:
            Итоговая сумма в формате float
        """
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_label)
        )
        total_text = total_element.text  # например, "Total: $58.29"
        total_amount_str = total_text.split("$")[1]  # получаем "58.29"
        return float(total_amount_str)
