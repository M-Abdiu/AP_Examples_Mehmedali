class Bird:
    def fly(self):
        print("flying")


class Sparrow(Bird):
    def fly(self):
        print("flying like a sparrow")


class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly")
