class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


p1_x = int(input("p1.x: "))
p1_y = int(input("p1.y: "))

p2_x = int(input("p2.x: "))
p2_y = int(input("p2.y: "))

p1 = Point(p1_x, p1_y)
p2 = Point(p2_x, p2_y)

print(p1.dist(p2))
