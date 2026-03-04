from time import sleep
from selenium import webdriver

cookie = {"name": "cookie_policy", "value": "1"}

def test_card_counter():
  browser = webdriver.Chrome()

  # Перейти на сайт «Лабиринта»
  browser.get("https://www.labirint.ru/")
  browser.implicitly_wait(4)
  browser.maximize_window()
  browser.add_cookie(cookie)
  sleep(5)

  # Найти все книги по слову Python
  # Добавить все книги в корзину и посчитать
  # Перейти в корзину
  # Проверить счетчик товаров

  browser.quit()