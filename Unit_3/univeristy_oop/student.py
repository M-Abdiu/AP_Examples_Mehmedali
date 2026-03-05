from functools import total_ordering

from module import Module


@total_ordering
class Student:
    _counter = 0

    def __new__(cls, *args, **kwargs):
        # THIS IS NOT NEEDED AND ONLY FOR DEMONSTRATION PURPOSES, 
        # AS __new__ IS NOT COMMONLY USED IN PYTHON
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, student_id: str, firstname: str, lastname: str) -> None:
        self.student_id: str = student_id
        self.firstname: str = firstname
        self.lastname: str = lastname
        self._modules: list[Module] = []
        Student._counter += 1

    @classmethod
    def student_count(cls) -> int:
        return cls._counter

    def enroll(self, module: Module) -> None:
        if module not in self._modules:
            self._modules.append(module)

    @property
    def student_id(self) -> str:
        return self._student_id
    
    @student_id.setter
    def student_id(self, value:str) -> None:
        if not value.isdigit():
            raise ValueError("student_id must contain only digits")
        self._student_id = value

    @property
    def firstname(self) -> str:
        return self._firstname
    
    @firstname.setter
    def firstname(self, value: str) -> None:
        if not value:
            raise ValueError("firstname can not be an empty string")
        self._firstname: str = str(value)

    @property
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, value: str) -> None:
        if not value:
            raise ValueError("lastname can not be an empty string")
        self._lastname: str = str(value)

    @property
    def modules(self) -> tuple[Module, ...]:
        # return a read only copy as tuple, to ensure enrollment via enroll method
        return tuple(self._modules)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"

    def __repr__(self) -> str:
        return (
            f"Student(student_id={self.student_id!r}, "
            f"firstname={self.firstname!r}, "
            f"lastname={self.lastname!r})"
        )
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.student_id == other.student_id
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return (self.lastname, self.firstname) < (other.lastname, other.firstname)
