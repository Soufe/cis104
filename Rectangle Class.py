class Rect(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def circumference(self):
        return 2 * (self.width + self.height)
a = Rect(3, 4)
print(a.area())
print(a.circumference())