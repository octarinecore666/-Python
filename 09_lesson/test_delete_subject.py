import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Subject

# Строка подключения
engine = create_engine("postgresql://postgres:1239@localhost/mydataQA")
Session = sessionmaker(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    session = Session()
    yield session
    session.close()


def test_delete_subject(db_session):
    # Уникальный ID для теста, чтобы избежать конфликтов
    unique_id = 999

    # Создаём запись для удаления
    subject_to_delete = Subject(
        subject_id=unique_id, subject_title="Предмет для удаления"
    )
    db_session.add(subject_to_delete)
    db_session.commit()

    try:
        # Проверяем, что запись создана и доступна
        subject = db_session.query(Subject).filter_by(subject_id=unique_id).first()
        assert (
            subject is not None
        ), "Запись не найдена в БД — не удалось создать тестовые данные"
        assert subject.subject_title == "Предмет для удаления"

        # Удаляем запись
        db_session.delete(subject)
        db_session.commit()  # Сохраняем изменения

        # Проверяем, что запись удалена
        deleted_subject = (
            db_session.query(Subject).filter_by(subject_id=unique_id).first()
        )
        assert deleted_subject is None, "Запись не была удалена из БД"
    finally:
        # Дополнительная очистка: если запись не удалилась
        remaining = db_session.query(Subject).filter_by(subject_id=unique_id).first()
        if remaining:
            db_session.delete(remaining)
            db_session.commit()
