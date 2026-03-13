from functools import total_ordering

from module import Module
from person import Person


@total_ordering
class Student(Person):
    _counter = 0

    def __init__(self, firstname: str, lastname: str, student_id: str) -> None:
        super().__init__(firstname, lastname)
        self.student_id: str = student_id
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
    def student_id(self, value: str) -> None:
        if not value.isdigit():
            raise ValueError("student_id must contain only digits")
        self._student_id = value

    @property
    def modules(self) -> tuple[Module, ...]:
        # return a read only copy as tuple, to ensure enrollment via enroll method
        return tuple(self._modules)

    def __repr__(self) -> str:
        return (
            f"Student(student_id={self.student_id!r}, "
            f"firstname={self.firstname!r}, "
            f"lastname={self.lastname!r})"
        )

    def __str__(self) -> str:  # overrides Person.__str__
        return f"{self.firstname} {self.lastname} ({self.student_id})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.student_id == other.student_id

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return (self.lastname, self.firstname) < (other.lastname, other.firstname)
