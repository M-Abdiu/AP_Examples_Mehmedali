"""
Generator Functions Demo
========================
This file demonstrates how to define and use generator functions in Python.

Key concepts:
- yield vs return
- Lazy evaluation
- Memory efficiency
- Generator expressions
"""


# =============================================================================
# 1. BASIC GENERATOR FUNCTION
# =============================================================================

def countdown(n: int):
    """A simple generator that counts down from n to 1."""
    print(f"Starting countdown from {n}")
    while n >= 0:
        yield n  # Pause here, return n, resume on next iteration
        n -= 1
    print("Countdown finished!")


# Using the generator
print("=" * 50)
print("1. Basic Generator: Countdown")
print("=" * 50)

for num in countdown(5):
    print(f"  {num}...")

print('-' * 20)


# =============================================================================
# 2. UNDERSTANDING YIELD VS RETURN
# =============================================================================

def get_squares_list(n: int) -> list[int]:
    """Regular function: builds and returns a complete list."""
    result = []
    for x in range(n):
        result.append(x ** 2)
    return result  # Returns everything at once


def get_squares_generator(n: int):
    """Generator function: yields one value at a time."""
    for x in range(n):
        yield x ** 2  # Pauses here, resumes on next call


print("=" * 50)
print("2. Yield vs Return")
print("=" * 50)

# Both produce the same results, but differently
print("List version:", get_squares_list(5))
print("Generator version:", list(get_squares_generator(5)))  # Convert to list to see all

print('-' * 20)


# =============================================================================
# 3. LAZY EVALUATION - VALUES COMPUTED ON DEMAND
# =============================================================================

def verbose_squares(n: int):
    """Generator that prints when each value is computed."""
    for x in range(n):
        print(f"    Computing {x}² = {x ** 2}")
        yield x ** 2


print("=" * 50)
print("3. Lazy Evaluation (values computed on demand)")
print("=" * 50)

gen = verbose_squares(5)
print(f"Generator created: {gen}")
print("Nothing computed yet!\n")

print("Now requesting values one by one:")
print(f"  First value: {next(gen)}")
print(f"  Second value: {next(gen)}")
print(f"  Third value: {next(gen)}")
print("  (stopped early - remaining values never computed!)")

print('-' * 20)


# =============================================================================
# 4. GENERATOR STATE IS PRESERVED
# =============================================================================

def counter():
    """Generator that remembers its state between yields."""
    count = 0
    while True:  # Infinite generator!
        count += 1
        yield count


print("=" * 50)
print("4. State Preservation")
print("=" * 50)

my_counter = counter()
print(f"First call:  {next(my_counter)}")
print(f"Second call: {next(my_counter)}")
print(f"Third call:  {next(my_counter)}")
print("(Generator remembers count between calls)")

print('-' * 20)


# =============================================================================
# 5. GENERATOR EXPRESSIONS (one-liner syntax)
# =============================================================================

print("=" * 50)
print("5. Generator Expressions")
print("=" * 50)

# List comprehension - uses brackets [], creates list immediately
squares_list = [x ** 2 for x in range(5)]
print(f"List comprehension: {squares_list}")
print(f"  Type: {type(squares_list)}")

# Generator expression - uses parentheses (), creates generator
squares_gen = (x ** 2 for x in range(5))
print(f"Generator expression: {squares_gen}")
print(f"  Type: {type(squares_gen)}")
print(f"  Converted to list: {list(squares_gen)}")

print('-' * 20)


# =============================================================================
# 6. PRACTICAL EXAMPLE: PROCESSING DATA EFFICIENTLY
# =============================================================================

def read_sensor_data():
    """Simulates reading from a sensor (could be a file, API, etc.)."""
    import random
    for i in range(10):
        yield {"id": i, "temperature": random.uniform(18.0, 25.0)}


def filter_high_temps(readings, threshold: float = 22.0):
    """Generator that filters readings above a threshold."""
    for reading in readings:
        if reading["temperature"] > threshold:
            yield reading


print("=" * 50)
print("6. Practical Example: Chaining Generators")
print("=" * 50)

# Chain generators together - no intermediate lists created!
raw_data = read_sensor_data()
high_temps = filter_high_temps(raw_data, threshold=22.0)

print("High temperature readings:")
for reading in high_temps:
    print(f"  Sensor {reading['id']}: {reading['temperature']:.1f}°C")

print('-' * 20)


# =============================================================================
# 7. USING GENERATORS WITH BUILT-IN FUNCTIONS
# =============================================================================

print("=" * 50)
print("7. Generators with Built-in Functions")
print("=" * 50)

numbers = range(1, 101)  # 1 to 100

# These work efficiently with generators - no intermediate list!
total = sum(x ** 2 for x in numbers)
print(f"Sum of squares 1-100: {total}")

has_even = any(x % 2 == 0 for x in numbers)
print(f"Has even number: {has_even}")

all_positive = all(x > 0 for x in numbers)
print(f"All positive: {all_positive}")

max_square = max(x ** 2 for x in range(10))
print(f"Max square (0-9): {max_square}")

print('-' * 20)


# =============================================================================
# 8. EXHAUSTED GENERATORS
# =============================================================================

print("=" * 50)
print("8. Important: Generators Can Only Be Iterated Once!")
print("=" * 50)

gen = (x for x in range(3))

print("First iteration:")
for x in gen:
    print(f"  {x}")

print("Second iteration:")
for x in gen:
    print(f"  {x}")  # This won't print anything!

print("  (nothing! generator is exhausted)")
