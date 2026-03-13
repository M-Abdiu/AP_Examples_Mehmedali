class Animal:
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print("meow")


class Dog(Animal):
    def make_sound(self):
        print("bark")


class Robot:
    def make_sound(self):
        print("beep")


if __name__ == "__main__":
    things = [Cat(), Dog(), Robot()]

    for t in things:
        t.make_sound()
