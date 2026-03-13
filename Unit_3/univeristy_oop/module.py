class Module:
    def __init__(self, name: str, description: str, ects: str) -> None:
        self.name: str = name
        self.description: str = description
        self.ects: str = ects

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("name can not be an empty string")
        self._name = str(value)

    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, value: str) -> None:
        if not value:
            raise ValueError("description can not be an empty string")
        self._description = str(value)

    @property
    def ects(self) -> int:
        return self._ects

    @ects.setter
    def ects(self, value: str):
        if value <= 0:
            raise ValueError("ects must be positive")
        self._ects = value

    # --------------------------------------------------------------
    # representations
    # --------------------------------------------------------------
    def __str__(self) -> str:
        return f"{self.name} ({self.ects} ECTS)"

    def __repr__(self) -> str:
        return (
            f"Module(name={self.name!r}, description={self.description!r}, "
            f"ects={self.ects!r})"
        )
