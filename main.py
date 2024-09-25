from sqlalchemy import create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    sessionmaker,
    mapped_column
)
from datetime import datetime

engine = create_engine("sqlite:///my.db", echo=True)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Lesson(Base):
    __tablename__ = "lesson"
    id: Mapped[int] = mapped_column(primary_key=True)
    teacher: Mapped[str]
    datetime: Mapped[datetime]
    subject: Mapped[str]

Base.metadata.create_all(engine)

def add_lesson(subject, teacher, datetime_input):
    session = Session()
    lesson_datetime = datetime.strptime(datetime_input, "%Y-%m-%d %H:%M")
    new_lesson = Lesson(subject=subject, teacher=teacher, datetime=lesson_datetime)
    session.add(new_lesson)
    session.commit()

def show_lessons():
    session = Session()
    lessons = session.query(Lesson).all()
    return lessons

if __name__ == "__main__":
    add_lesson(
        subject="Python", teacher="dmytro", datetime_input="2022-12-02 18:00"
)
lessons = show_lessons()
for lesson in lessons:
        print(
            f" {lesson.subject}, {lesson.teacher}, {lesson.datetime}"
)