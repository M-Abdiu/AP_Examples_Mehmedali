class Person:
    _counter = 0

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        Person._counter += 1

    @property
    def firstname(self) -> str:
        return self._firstname

    @firstname.setter
    def firstname(self, value: str) -> None:
        if not value:
            raise ValueError("firstname can not be an empty string")
        self._firstname = str(value)

    @property
    def lastname(self) -> str:
        return self._lastname

    @lastname.setter
    def lastname(self, value: str) -> None:
        if not value:
            raise ValueError("lastname can not be an empty string")
        self._lastname = str(value)

    def __repr__(self) -> str:
        return (
            f"Person(firstname={self.firstname!r}, "
            f"lastname={self.lastname!r})"
        )

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
