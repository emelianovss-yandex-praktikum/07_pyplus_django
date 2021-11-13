from models import Student, Grade


student = Student(
    id=2,
    grades=[
        Grade(name="math", estimate=5),
        Grade(name="sport", estimate=5),
    ]
)


def main():
    print(f"ID: {student.id}")
    for grade in student.grades:
        print(f"  {grade.estimate} - {grade.name}")


if __name__ == '__main__':
    main()
