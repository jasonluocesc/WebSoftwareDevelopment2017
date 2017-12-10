class Point:

    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def distance_from(self, Point):
        return ((self.x-Point.x)**2+(self.y-Point.y)**2)**0.5


class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def is_inside(self, point):
        c = self.center
        d = point.distance_from(Point(c.x,c.y))
        if d < self.radius:
            return True
        else:
            return False

