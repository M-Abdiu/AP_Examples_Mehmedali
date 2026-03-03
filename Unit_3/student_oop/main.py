from module import Module
from student import Student

if __name__ == '__main__':
    programming_f = Module("Programming Foundations", "Introduction into the principles of programming", 6)
    stephan = Student("25875567", "Stephan", "Müller")
    stephan.enroll(programming_f)

    print(f"Total Students: {Student.student_count()}")

    print(stephan)
    for module in stephan.modules:
        print(f" * {module}")