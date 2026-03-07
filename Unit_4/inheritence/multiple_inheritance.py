class Bird:
    def walk(self):
        print("Pep")


class FlyingBird(Bird):
    def walk(self):
        print("hopping")

    def fly(self):
        print("flying")


class SwimmingBird(Bird):
    def walk(self):
        print("waddeling")

    def swim(self):
        print("swimming")


class Penguin(SwimmingBird):
    def make_sound(self):
        print("squawk")


class Sparrow(FlyingBird):
    pass


class Duck(SwimmingBird, FlyingBird):
    pass


if __name__ == "__main__":
    penguin = Penguin()
    penguin.walk()  # Inherited from Bird
    penguin.swim()        # Inherited from SwimmingBird

    sparrow = Sparrow()
    sparrow.walk()  # Inherited from Bird
    sparrow.fly()         # Inherited from FlyingBird

    duck = Duck()
    duck.fly()         # Inherited from FlyingBird
    duck.swim()        # Inherited from SwimmingBird
    duck.walk()        # Inherited from SwimmingBird due to MRO
