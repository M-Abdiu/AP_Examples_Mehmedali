class Animal:
    registered_animals = []

    def __new__(cls, gender, *args, **kwargs):
        # gender is now always explicitly provided
        for animal in Animal.registered_animals:
            if isinstance(animal, cls) and animal.gender == gender:
                raise ValueError(f"An instance of {cls.__name__} with gender '{gender}' already exists.")
        instance = super(Animal, cls).__new__(cls)
        Animal.registered_animals.append(instance)
        return instance

    def __init__(self, gender):
        self.gender = gender

class Dog(Animal):
    def __init__(self, gender):
        super().__init__(gender)

class Cat(Animal):
    def __init__(self, gender):
        super().__init__(gender)

# Example usage:
if __name__ == "__main__":
    dog_male = Dog("male")
    print(f"Created: {dog_male.__class__.__name__}, gender: {dog_male.gender}")
    dog_female = Dog("female")
    print(f"Created: {dog_female.__class__.__name__}, gender: {dog_female.gender}")
    try:
        another_male_dog = Dog("male")
    except ValueError as e:
        print(f"Error: {e}")
    cat_female = Cat("female")
    print(f"Created: {cat_female.__class__.__name__}, gender: {cat_female.gender}")
    try:
        another_female_cat = Cat("female")
    except ValueError as e:
        print(f"Error: {e}")
