class Bird:
    def make_sound(self):
        print("Pep")


class FlyingBird(Bird):
    def fly(self):
        print("flying")


class SwimmingBird(Bird):
    def swim(self):
        print("swimming")


class WalkingBird(Bird):
    def walk(self):
        print("walking")


class Penguin(SwimmingBird):
    def make_sound(self):
        print("squawk")


class Sparrow(FlyingBird):
    def make_sound(self):
        print("chirp")


class Duck(FlyingBird, SwimmingBird, WalkingBird):
    def make_sound(self):
        print("quack")


if __name__ == "__main__":
    penguin = Penguin()
    penguin.make_sound()  # Inherited from Bird
    penguin.swim()        # Inherited from SwimmingBird
    sparrow = Sparrow()
    sparrow.make_sound()  # Inherited from Bird
    sparrow.fly()         # Inherited from FlyingBird

    duck = Duck()
    duck.make_sound()  # Inherited from Bird
    duck.fly()         # Inherited from FlyingBird
    duck.swim()        # Inherited from SwimmingBird
    duck.walk()        # Inherited from WalkingBird
