import os
import pytest
from dotenv import load_dotenv
import requests

# Загружаем переменные из .env (если файл есть)
load_dotenv()


BASE_URL = "https://ru.yougile.com/api-v2"


@pytest.fixture(scope="session")
def auth_token():
    token = os.environ.get("YOUGILE_TOKEN")
    if not token:
        raise ValueError(
            "YOUGILE_TOKEN environment variable is not set. "
            "Create .env file with your token in the project root directory."
        )
    return token


@pytest.fixture
def headers(auth_token):
    return {"Authorization": f"Bearer {auth_token}", "Content-Type": "application/json"}


@pytest.fixture
def project_cleanup(headers):
    """Фикстура для отслеживания и удаления созданных проектов"""
    created_projects = []

    def _track_project(project_id):
        created_projects.append(project_id)

    yield _track_project

    # Очистка после тестов — помечаем проекты как удалённые
    for project_id in created_projects:
        url = f"{BASE_URL}/projects/{project_id}"
        requests.put(url, json={"deleted": True}, headers=headers)


@pytest.fixture
def create_test_project(headers, project_cleanup):
    """Фикстура для создания тестового проекта"""

    def _create_project(title="Test Project"):
        url = f"{BASE_URL}/projects"
        data = {"title": title, "users": {}}
        response = requests.post(url, json=data, headers=headers)
        assert response.status_code == 201
        project_id = response.json()["id"]
        # Отслеживаем проект для последующей очистки
        project_cleanup(project_id)
        return project_id

    return _create_project
