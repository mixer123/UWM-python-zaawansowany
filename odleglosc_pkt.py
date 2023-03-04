import math


class Point:
    x = 4
    y = 2

    def reset(self):
        self.x = 0
        self.y = 0

    def left(self, move):
        self.x -= move

    def move(self, mx, my):
        self.x += mx
        self.y += my

    def dist(self, other=None):
        if other is None:
            return math.sqrt(self.x ** 2 + self.y ** 2)
        else:
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


p1 = Point()
p1.move(-1, 1)
print(p1.x, p1.y)
p2 = Point()
print(p1.dist())
print(p1.dist(p2))
print(p1.dist(p1))