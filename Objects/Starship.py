from Objects.MoveableObject import MoveableObject
from math import sin, cos, pi


class Starship(MoveableObject):
    def __init__(self, w, h):
        self.x = w // 2
        self.y = h // 2
        self.angle = 40 / 180 * pi  # в градусах
        self.angle_rotation = 0  # в градусах
        self.side = 70
        self.speed = [0, 0]
        self.a = [0, 0]
        super().__init__(self.x, self.y, self.speed, self.a)

    def move(self):
        self.x = self.x + self.speed[0] + self.a[0]
        self.y = self.y + self.speed[1] + self.a[1]

    def calc_cords(self):
        c0 = int(self.x), int(self.y)
        c1 = (int(self.x - self.side * sin(self.angle / 2)), int(self.y + self.side * cos(self.angle / 2)))
        c2 = (int(self.x + self.side * sin(self.angle / 2)), int(self.y + self.side * cos(self.angle / 2)))
        c3 = (
            int((self.x - self.side * 0.8 * sin(self.angle / 2))),
            int((self.y + self.side * 0.8 * cos(self.angle / 2))))
        c4 = (
            int((self.x + self.side * 0.8 * sin(self.angle / 2))),
            int((self.y + self.side * 0.8 * cos(self.angle / 2))))

        return c0, c1, c2, c3, c4

    def rotate(self, angle):
        angle = (angle+90) / 180 * pi
        r = self.side * cos(self.angle / 2)
        self.x = int(self.x + r * cos(angle))
        self.y = int(self.y + r * sin(angle))
        self.angle_rotation += angle
        print(self.x, self.y)
