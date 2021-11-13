from typing import List
from dataclasses import dataclass
from statistics import mean


@dataclass
class Grade:
    name: str
    estimate: int


@dataclass
class Student:
    id: int
    grades: List[Grade]

    def mean(self):
        return mean(map(lambda x: x.estimate, self.grades))


if __name__ == '__main__':
    student = Student(id=1, grades=[])
    print(student)

    student.grades.append(Grade(name="math", estimate=3))
    student.grades.append(Grade(name="russian", estimate=5))
    print(student)
    print(student.mean())
