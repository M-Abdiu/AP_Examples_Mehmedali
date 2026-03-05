from module import Module
from lecturer import Lecturer
from student import Student

if __name__ == '__main__':
    programming_f = Module("Programming Foundations", "Introduction into the principles of programming", 6)
    stephan = Student("25875567", "Stephan", "Müller")
    stephan.enroll(programming_f)
    lecturer = Lecturer("1001", "Anna", "Schmidt")
    lecturer.lecture(programming_f)

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