# This is a simple Python script for a calculator in a class


class Taschenrechner:
    """Ein einfacher Taschenrechner mit Grundrechenarten."""

    def __init__(self):
        """Initialize the calculator."""
        pass

    def add(self, a, b):
        """Add two numbers together."""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


if __name__ == "__main__":
    tr = Taschenrechner()

    print("Testing add method:")
    print(tr.add(7, 3))  # Should print 10

    print("Testing subtract method:")
    print(tr.subtract(5, 2))  # Should print 3

    print("Testing multiply method:")
    print(tr.multiply(4, 3))  # Should print 12

    print("Testing divide method:")
    print(tr.divide(10, 2))  # Should print 5
