def create_student(student_id: str, fname: str, lname: str):
    return {
            "student_id": student_id,
            "firstname": fname, 
            "lastname": lname,
            "modules": []
    }

def create_module(name: str):
    return {
        "name": name
    }


def enroll(student, module):
    if module not in student["modules"]:
        student["modules"].append(module)