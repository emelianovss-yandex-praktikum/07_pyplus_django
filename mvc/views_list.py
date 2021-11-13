from models import Student, Grade


student_1 = Student(
    id=3,
    grades=[
        Grade(name="chemistry", estimate=4),
    ]
)

student_2 = Student(
    id=4,
    grades=[
        Grade(name="physics", estimate=5),
        Grade(name="sport", estimate=3),
    ]
)

students = [student_1, student_2]


def main():
    for student in students:
        print(f"ID[{student.id}] - {student.mean()}")


if __name__ == '__main__':
    main()
