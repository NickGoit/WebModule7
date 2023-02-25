from faker import Faker

import random

from database.db import session
from database.models import Student, StudentGroup


NUMBER_STUDENTS = 50

fake = Faker('uk_UA')


def seed_students():
    st_groups = session.query(StudentGroup).all()

    for _ in range(NUMBER_STUDENTS):
        student_group = random.choice(st_groups)
        student = Student(
            name=fake.name(),
            group_id=student_group.id)

        session.add(student)
    session.commit()


if __name__ == '__main__':
    seed_students()

