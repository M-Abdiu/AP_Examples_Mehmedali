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


class Eagle(FlyingBird):
    pass


class Duck(SwimmingBird, FlyingBird):
    pass


class Seagull(SwimmingBird, FlyingBird):
    def walk(self):
        # Explicitly call the walk method from FlyingBird
        FlyingBird.walk(self)


if __name__ == "__main__":
    penguin = Penguin()
    penguin.walk()      # Inherited from Bird
    penguin.swim()      # Inherited from SwimmingBird

    eagle = Eagle()
    eagle.walk()        # Inherited from Bird
    eagle.fly()         # Inherited from FlyingBird

    duck = Duck()
    duck.fly()          # Inherited from FlyingBird
    duck.swim()         # Inherited from SwimmingBird
    duck.walk()         # Inherited from SwimmingBird due to MRO
