def create_student(student_id: str, firstname: str, lastname: str):
    return {
            "student_id": student_id,
            "firstname": firstname, 
            "lastname": lastname,
            "modules": []
    }

def create_module(name: str):
    return {
        "name": name
    }


def enroll(student, module):
    if module not in student["modules"]:
        student["modules"].append(module)