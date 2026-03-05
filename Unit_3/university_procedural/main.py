from student import create_module, create_student, enroll

from datetime import date

if __name__ == '__main__':
    programming = create_module("Programming")
    stephan = create_student("Stephan", "Müller", "25875567")
    
    enroll(stephan, programming)

    print(stephan)