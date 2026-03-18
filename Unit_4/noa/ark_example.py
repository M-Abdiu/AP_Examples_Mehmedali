
# Simple animal classes (no gender restriction logic)
class Animal:
    def __init__(self, gender):
        self.gender = gender

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Ark:
    def __init__(self):
        # {(subclass, gender): instance}
        self._animals = {}

    def add_animal(self, animal: Animal):
        key = (type(animal), animal.gender)
        if key in self._animals:
            raise ValueError(f"{animal.__class__.__name__} with gender '{animal.gender}' already in the Ark.")
        self._animals[key] = animal
        print(f"Added to Ark: {animal.__class__.__name__}, gender: {animal.gender}")

    def get_animal(self, animal_class: type, gender: str):
        key = (animal_class, gender)
        return self._animals.get(key, None)

if __name__ == "__main__":
    ark = Ark()
    dog1 = Dog("male")
    dog2 = Dog("female")
    cat1 = Cat("male")
    cat2 = Cat("female")
    for animal in [dog1, dog2, cat1, cat2]:
        try:
            ark.add_animal(animal)
        except ValueError as e:
            print(f"Ark error: {e}")
    # Try to add a duplicate
    try:
        ark.add_animal(Dog("male"))
    except ValueError as e:
        print(f"Ark error: {e}")
