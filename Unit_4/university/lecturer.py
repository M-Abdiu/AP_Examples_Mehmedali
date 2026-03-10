from module import Module
from person import Person


class Lecturer(Person):
    _counter = 0

    def __init__(self, firstname: str, lastname: str, employee_id: str) -> None:
        super().__init__(firstname, lastname)
        self.employee_id = employee_id
        self._modules: list[Module] = []
        Lecturer._counter += 1

    @classmethod
    def lecturer_count(cls) -> int:
        return cls._counter

    @property
    def employee_id(self) -> str:
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value: str) -> None:
        if not value.isdigit():
            raise ValueError("employee_id must contain only digits")
        self._employee_id = value

    def lecture(self, module: Module) -> None:
        if module not in self._modules:
            self._modules.append(module)

    @property
    def modules(self) -> tuple[Module, ...]:
        return tuple(self._modules)

    def __repr__(self) -> str:
        return (
            f"Lecturer(employee_id={self.employee_id!r}, "
            f"firstname={self.firstname!r}, "
            f"lastname={self.lastname!r})"
        )

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname} ({self.employee_id})"
