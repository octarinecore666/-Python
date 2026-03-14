import pytest
import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Subject

engine = create_engine("postgresql://postgres:1239@localhost/mydataQA")
Session = sessionmaker(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    session = Session()
    yield session
    session.close()


def test_add_subject(db_session):
    unique_id = uuid.uuid4().int % 10000
    new_subject = Subject(subject_id=unique_id, subject_title="Новый предмет")

    try:
        db_session.add(new_subject)
        db_session.commit()

        result = db_session.query(Subject).filter_by(subject_id=unique_id).first()
        assert result is not None
        assert result.subject_title == "Новый предмет"
    finally:
        if new_subject in db_session:
            db_session.delete(new_subject)
        db_session.commit()
