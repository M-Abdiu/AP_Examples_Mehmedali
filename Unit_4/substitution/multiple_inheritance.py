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


class Duck(FlyingBird, SwimmingBird, WalkingBird):
    def make_sound(self):
        print("quack")


if __name__ == "__main__":
    duck = Duck()
    duck.make_sound()  # Inherited from Bird
    duck.fly()         # Inherited from FlyingBird
    duck.swim()        # Inherited from SwimmingBird
    duck.walk()        # Inherited from WalkingBird
