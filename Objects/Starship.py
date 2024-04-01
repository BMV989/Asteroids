from Objects.MovableObject import MovableObject
from math import sin, cos, pi


class Starship(MovableObject):
    def __init__(self, w, h):
        #########################################
        self.x = w // 2  # координаты носа
        self.y = h // 2  # координаты носа
        #########################################
        self.angle = 40 / 180 * pi  # радианы
        self.angle_rotation = 0  # в градусах
        self.side = 70
        self.r = self.side * cos(self.angle / 2)
        self.small_r = self.side * sin(self.angle / 2)
        self.r2 = self.r * 0.2
        self.speed = [0, 0]
        self.a = [0, 0]
        #########################################
        self.center = int(self.x), int(self.y + self.r)
        self.side_x1 = int(self.x - self.side * sin(self.angle / 2))
        self.side_y1 = int(self.y + self.side * cos(self.angle / 2))
        self.side_x2 = int(self.x + self.side * sin(self.angle / 2))
        self.side_y2 = int(self.y + self.side * cos(self.angle / 2))
        self.side_x3 = int(self.x - self.side * 0.8 * sin(self.angle / 2))
        self.side_y3 = int(self.y + self.side * 0.8 * cos(self.angle / 2))
        self.side_x4 = int(self.x + self.side * 0.8 * sin(self.angle / 2))
        self.side_y4 = int(self.y + self.side * 0.8 * cos(self.angle / 2))
        #########################################
        self.small_c_x1 = self.center[0] - self.r2 * sin(self.angle_rotation)
        self.small_c_y1 = self.center[1] - self.r2 * cos(self.angle_rotation)
        #########################################
        super().__init__(self.x, self.y, self.speed, self.a)

    def move(self, a):
        self.a[0] += a
        self.a[1] += a

        self.speed[0] += self.a[0]
        self.speed[1] += self.a[1]
        self.x = self.x + self.speed[0]
        self.y = self.y + self.speed[1]
        self.center = int(self.x), int(self.y + self.r)

    def get_v(self):
        return self.speed

    def get_a(self):
        return self.a

    def calc_cords(self):
        c0 = int(self.x), int(self.y)
        c1 = (self.side_x1, self.side_y1)
        c2 = (self.side_x2, self.side_y2)
        c3 = (self.side_x3, self.side_y3)
        c4 = (self.side_x4, self.side_y4)

        return c0, c1, c2, c3, c4

    def rotate(self, angle):
        self.angle_rotation += angle
        if self.angle_rotation < 0:
            self.angle_rotation = 360 + self.angle_rotation
        if self.angle_rotation > 360:
            self.angle_rotation -= 360
        angle_in_rads = self.angle_rotation / 180 * pi

        self.x = int(self.center[0] - self.r * sin(angle_in_rads))
        self.y = int(self.center[1] - self.r * cos(angle_in_rads))

        self.small_c_x1 = self.center[0] - self.r2 * sin(angle_in_rads)
        self.small_c_y1 = self.center[1] - self.r2 * cos(angle_in_rads)

        self.side_x1 = int(self.center[0] - self.small_r * cos(angle_in_rads))
        self.side_y1 = int(self.center[1] + self.small_r * sin(angle_in_rads))
        self.side_x2 = int(self.center[0] + self.small_r * cos(angle_in_rads))
        self.side_y2 = int(self.center[1] - self.small_r * sin(angle_in_rads))
        self.side_x3 = int(self.small_c_x1 - self.small_r * 0.8 * cos(angle_in_rads))
        self.side_y3 = int(self.small_c_y1 + self.small_r * 0.8 * sin(angle_in_rads))
        self.side_x4 = int(self.small_c_x1 + self.small_r * 0.8 * cos(angle_in_rads))
        self.side_y4 = int(self.small_c_y1 - self.small_r * 0.8 * sin(angle_in_rads))
