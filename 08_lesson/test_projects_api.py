import os
import requests

BASE_URL = "https://ru.yougile.com/api-v2/projects"
TOKEN = os.environ.get("YOUGILE_TOKEN")  # Исправлено: getenv → get
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}


# Позитивные тесты
def test_create_project():
    payload = {
        "title": "Мандарин",
        "users": {"80a0f15d-50f1-43be-b987-0408401ee009": "admin"},
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    assert response.status_code == 201
    assert "id" in response.json()


def test_update_project():
    project_id = "b5487c25-17fc-4bd8-b6a3-17350083a1c6"
    payload = {
        "deleted": False,
        "title": "Обновленный проект",
        "users": {"80a0f15d-50f1-43be-b987-0408401ee009": "admin"},
    }
    response = requests.put(f"{BASE_URL}/{project_id}", json=payload, headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project():
    project_id = "b5487c25-17fc-4bd8-b6a3-17350083a1c6"
    response = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS)
    assert response.status_code == 200
    assert "title" in response.json()


# Негативные тесты
def test_create_project_invalid():
    payload = {
        "title": "",  # Задаем пустое название
        "users": {"80a0f15d-50f1-43be-b987-0408401ee009": "admin"},
    }
    response = requests.post(f"{BASE_URL}", json=payload, headers=HEADERS)
    assert response.status_code == 400
    assert "message" in response.json()


def test_update_project_not_found():
    project_id = "b5487c25-17fc-4bd8-b6a3-17350083a1c60000000"  # Неверный ID
    payload = {"deleted": True}
    response = requests.put(f"{BASE_URL}/{project_id}", json=payload, headers=HEADERS)
    assert response.status_code == 404


def test_get_project_not_found():
    project_id = "1212"  # Неверный ID
    response = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS)
    assert response.status_code == 404
