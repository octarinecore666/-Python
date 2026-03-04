from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        """Открыть страницу авторизации"""
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        """Ввести имя пользователя"""
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.username_field)
        )
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        """Ввести пароль"""
        password_input = self.driver.find_element(*self.password_field)
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):
        """Нажать кнопку входа"""
        login_btn = self.driver.find_element(*self.login_button)
        login_btn.click()
