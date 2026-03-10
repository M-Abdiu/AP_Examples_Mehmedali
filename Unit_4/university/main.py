from person import Person
from module import Module
from lecturer import Lecturer
from student import Student

if __name__ == '__main__':
    programming_f = Module(
        "Programming Foundations",
        "Introduction into the principles of programming",
        6
    )
    stephan = Student("Stephan", "Müller", "25875567")
    stephan.enroll(programming_f)
    lecturer = Lecturer("Anna", "Schmidt", "1001")
    lecturer.lecture(programming_f)

    print(f"Total Persons: {Person._counter}")

    print()
    print()

    print(f"Total Students: {Student.student_count()}")
    print(stephan)
    for module in stephan.modules:
        print(f" -> enrolled: {module}")

    print()
    print()

    print(f"Total Lecturers: {Lecturer.lecturer_count()}")
    print(lecturer)
    for module in lecturer.modules:
        print(f" -> lecturing: {module}")
