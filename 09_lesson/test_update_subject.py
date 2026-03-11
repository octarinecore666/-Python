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


def test_update_subject(db_session):
    # Уникальный ID для теста, чтобы избежать конфликтов
    unique_id = 999

    # Создаём начальную запись
    subject_to_update = Subject(subject_id=unique_id, subject_title="Старый предмет")
    db_session.add(subject_to_update)
    db_session.commit()

    try:
        # Находим запись для обновления
        subject = db_session.query(Subject).filter_by(subject_id=unique_id).first()
        assert subject is not None, "Запись не найдена в БД"
        assert subject.subject_title == "Старый предмет"

        # Обновляем поле
        subject.subject_title = "Обновлённый предмет"
        db_session.commit()  # Сохраняем изменения

        # Проверяем, что обновление прошло успешно
        updated_subject = (
            db_session.query(Subject).filter_by(subject_id=unique_id).first()
        )
        assert updated_subject is not None
        assert updated_subject.subject_title == "Обновлённый предмет"
    finally:
        # Очищаем данные после теста
        if subject_to_update in db_session:
            db_session.delete(subject_to_update)
        db_session.commit()
