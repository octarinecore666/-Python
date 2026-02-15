from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import time

driver = webdriver.Chrome()

try:
    # 1. Переход на сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # 2. Ожидание видимости контейнера с картинками
    container = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "image-container"))
    )

    # 3. Список ID всех изображений в контейнере 
    image_ids = ["compass", "calendar", "award", "landscape"]


    # 4. Ждём, пока КАЖДОЕ изображение станет видимым
    images = []
    for img_id in image_ids:
        img = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, img_id))
        )
        images.append(img)

    # 5. Дополнительная проверка: ждём, пока ВСЕ изображения будут полностью загружены
    # (атрибут 'complete' == "true" для каждого)
    def all_images_fully_loaded(driver):
        for img_id in image_ids:
            img = driver.find_element(By.ID, img_id)
            if img.get_attribute("complete") != "true":
                return False
        return True

    WebDriverWait(driver, 10).until(all_images_fully_loaded)

    # 6. Получаем src у 3‑й картинки (index=2, id="award")
    if len(images) >= 3:
        src_value = images[2].get_attribute("src")
        print(src_value)  # Выводим в консоль
    else:
        print("Не найдено достаточно изображений (ожидалось 4).")

except TimeoutException:
    print("Время ожидания истекло: изображения не загрузились.")
except WebDriverException as e:
    print(f"Ошибка WebDriver: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")

finally:
    # Закрываем браузер
    driver.quit()
