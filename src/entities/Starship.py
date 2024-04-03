from math import sin, cos, pi

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter

from src import constants
from src.entities.MovableObject import MovableObject


class Starship(MovableObject):
    def __init__(self, w, h):
        self.center = [w // 2, h // 2]
        self.angle = 40 / 180 * pi  # радианы
        self.angle_rotation = 45  # в градусах
        self.side = 70
        self.r = self.side * cos(self.angle / 2)
        self.small_r = self.side * sin(self.angle / 2)
        self.r2 = self.r * 0.2
        self.speed = [0, 0]
        self.a = [[0, 0]]
        self.alpha = [[0, 0]]  # трение
        #########################################
        self.x = self.center[0]  # координаты носа
        self.y = self.center[1] - self.r  # координаты носа
        #########################################
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
        super().__init__(QPoint(int(self.x), int(self.y)))

    def move(self):
        self.a.append([0, 0])
        self.a[-1][0] -= 4 * sin(self.angle_rotation / 180 * pi)
        self.a[-1][1] -= 4 * cos(self.angle_rotation / 180 * pi)

        self.alpha.append([0, 0])
        self.alpha[-1][0] -= 1 * sin(self.angle_rotation / 180 * pi + pi)
        self.alpha[-1][1] -= 1 * cos(self.angle_rotation / 180 * pi + pi)

        """
        self.a[0] += a
        self.a[1] += a

        self.speed[0] += self.a[0]
        self.speed[1] += self.a[1]
        self.x = self.x + self.speed[0]
        self.y = self.y + self.speed[1]
        self.center = int(self.x), int(self.y + self.r)
        """

    def calc_v(self):
        a_x = 0
        a_y = 0
        for i in range(len(self.a)):
            a_x += self.a[i][0] + self.alpha[i][0]
            a_y += self.a[i][1] + self.alpha[i][1]
        self.speed[0] += a_x
        self.speed[1] += a_y
        if self.speed[0] >= 0:
            self.speed[0] = 0
        if self.speed[1] >= 0:
            self.speed[1] = 0

        if self.speed[0] < 0 and a_x == 0:
            self.speed[0] += 0.001 * sin(self.angle_rotation / 180 * pi)
        if self.speed[1] < 0 and a_y == 0:
            self.speed[1] += 0.001 * cos(self.angle_rotation / 180 * pi)

        self.center[0] += self.speed[0] * sin(self.angle_rotation / 180 * pi)
        self.center[1] += self.speed[1] * cos(self.angle_rotation / 180 * pi)
        print(self.speed)
        print(self.a)
        print(self.alpha)
        # if self.speed[0] == -1.3965358928434324:
        #     pass

        self.center[0] = (self.center[0] + constants.WIDOW_WIDTH) % constants.WIDOW_WIDTH
        self.center[1] = (self.center[1] + constants.WIDOW_HEIGHT) % constants.WIDOW_HEIGHT

    def reduce_speed(self):
        # if self.speed[0] < 0:
        #     self.speed[0] += 0.3
        # if self.speed[1] < 0:
        #     self.speed[1] += 0.3
        pass

    def calc_a(self):
        for i in range(len(self.a)):
            self.a[i][0] += self.alpha[i][0]
            self.a[i][1] += self.alpha[i][1]
            # if self.a[i][0] > 0:  # умножить на косинус или синус ???
            #     self.a[i][0] = 0
            # if self.a[i][1] > 0:
            #     self.a[i][1] = 0
            if self.a[i][0] >= 0 and self.a[i][1] >= 0:
                del self.a[i]
                del self.alpha[i]

    def get_v(self):
        return self.speed

    def nullify_a(self):
        self.a = [[0, 0]]

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
        self.calc_all_cords()

    def calc_all_cords(self):
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
    def upd(self):
        pass
    def paint(self, painter: QPainter):
        c1, c2, c3, c4, c5 = self.calc_cords()
        painter.drawLine(*c1, *c2)
        painter.drawLine(*c1, *c3)
        painter.drawLine(*c4, *c5)
