import math
from copy import copy
from math import sin, cos, pi
from random import random

from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtGui import QPainter

from src import constants
from src.entities.movable_object import MovableObject


class Starship(MovableObject):
    def __init__(self):
        self.center = [constants.WIDOW_WIDTH // 2, constants.WIDOW_HEIGHT // 2]
        self.angle = 40 / 180 * pi  # радианы
        self.angle_rotation = 0  # в градусах
        self.angel_vector = 0  # градусах
        self.side = 70
        self.r = self.side * cos(self.angle / 2)
        self.small_r = self.side * sin(self.angle / 2)
        self.r2 = self.r * 0.2
        self.speed = [0, 0]
        self.fast_forward_mode = False
        self.rotate_left = False
        self.rotate_right = False
        #########################################
        self.x = self.center[0]  # координаты носа
        self.y = self.center[1] - self.r  # координаты носа
        #########################################
        self.side_x0 = int(self.center[0])
        self.side_y0 = int(self.center[1] - self.r - 10)
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
        self.side_x5 = int(self.x - self.side * 0.4 * sin(self.angle / 2))
        self.side_y5 = int(self.y + self.side * 0.4 * cos(self.angle / 2))
        self.side_x6 = int(self.x + self.side * 0.4 * sin(self.angle / 2))
        self.side_y6 = int(self.y + self.side * 0.4 * cos(self.angle / 2))
        #########################################
        super().__init__(QPoint(int(self.x), int(self.y)), QSize(int(2 * self.small_r), int(self.r)))

    def move(self):
        self.angel_vector = copy(self.angle_rotation)

        if 0 <= self.angel_vector <= 90:
            self.speed[0] += 10 * sin(self.angel_vector / 180 * pi)  # -
            self.speed[1] += 10 * cos(self.angel_vector / 180 * pi)  # -
        elif 90 < self.angel_vector <= 180:
            self.speed[0] += 10 * sin(pi - self.angel_vector / 180 * pi)  # -
            self.speed[1] += 10 * cos(pi - self.angel_vector / 180 * pi)
        elif 180 < self.angel_vector <= 270:
            self.speed[0] += 10 * cos(pi * 3 / 2 - self.angel_vector / 180 * pi)
            self.speed[1] += 10 * sin(pi * 3 / 2 - self.angel_vector / 180 * pi)
        elif 270 < self.angel_vector <= 360:
            self.speed[0] += 10 * sin(pi * 2 - self.angel_vector / 180 * pi)
            self.speed[1] += 10 * cos(pi * 2 - self.angel_vector / 180 * pi)  # -

    def upd(self):
        if self.fast_forward_mode:
            self.move()
        if self.rotate_left:
            for i in range(1000):
                self.rotate(0.01)
        if self.rotate_right:
            for i in range(1000):
                self.rotate(-0.01)

        if 0 <= self.angel_vector <= 90:
            self.center[0] -= self.speed[0]
            self.center[1] -= self.speed[1]
        elif 90 < self.angel_vector <= 180:
            self.center[0] -= self.speed[0]
            self.center[1] += self.speed[1]
        elif 180 < self.angel_vector <= 270:
            self.center[0] += self.speed[0]
            self.center[1] += self.speed[1]
        elif 270 < self.angel_vector <= 360:
            self.center[0] += self.speed[0]
            self.center[1] -= self.speed[1]

        self.center[0] = (self.center[0] + constants.WIDOW_WIDTH) % constants.WIDOW_WIDTH
        self.center[1] = (self.center[1] + constants.WIDOW_HEIGHT) % constants.WIDOW_HEIGHT
        self.slow()
        self.calc_all_cords()

    def slow(self):
        acceleration = math.hypot(self.speed[0], self.speed[1])
        if acceleration > 10:
            scale = 10 / acceleration
            self.speed[0] *= scale
            self.speed[1] *= scale
        self.speed[0] = self.speed[0] * 0.98
        self.speed[1] = self.speed[1] * 0.98

    def pack_cords(self):
        c0 = int(self.x), int(self.y)
        c1 = (self.side_x1, self.side_y1)
        c2 = (self.side_x2, self.side_y2)
        c3 = (self.side_x3, self.side_y3)
        c4 = (self.side_x4, self.side_y4)
        c5 = (self.side_x5, self.side_y5)
        c6 = (self.side_x6, self.side_y6)

        return c0, c1, c2, c3, c4, c5, c6

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

        self.side_x0 = int(self.center[0] - (self.r + 10) * sin(angle_in_rads))
        self.side_y0 = int(self.center[1] - (self.r + 10) * cos(angle_in_rads))
        self.side_x1 = int(self.center[0] - self.small_r * cos(angle_in_rads))
        self.side_y1 = int(self.center[1] + self.small_r * sin(angle_in_rads))
        self.side_x2 = int(self.center[0] + self.small_r * cos(angle_in_rads))
        self.side_y2 = int(self.center[1] - self.small_r * sin(angle_in_rads))
        self.side_x3 = int(self.small_c_x1 - self.small_r * 0.8 * cos(angle_in_rads))
        self.side_y3 = int(self.small_c_y1 + self.small_r * 0.8 * sin(angle_in_rads))
        self.side_x4 = int(self.small_c_x1 + self.small_r * 0.8 * cos(angle_in_rads))
        self.side_y4 = int(self.small_c_y1 - self.small_r * 0.8 * sin(angle_in_rads))
        self.side_x5 = int(self.small_c_x1 - self.small_r * 0.4 * cos(angle_in_rads))
        self.side_y5 = int(self.small_c_y1 + self.small_r * 0.4 * sin(angle_in_rads))
        self.side_x6 = int(self.small_c_x1 + self.small_r * 0.4 * cos(angle_in_rads))
        self.side_y6 = int(self.small_c_y1 - self.small_r * 0.4 * sin(angle_in_rads))

    def paint(self, painter: QPainter):
        c1, c2, c3, c4, c5, c6, c7 = self.pack_cords()
        painter.drawLine(*c1, *c2)
        painter.drawLine(*c1, *c3)
        painter.drawLine(*c4, *c5)

        if self.fast_forward_mode and random() < 0.8:
            painter.drawLine(*c6, int(self.center[0]) + 10, int(self.center[1]) + 10)
            painter.drawLine(*c7, int(self.center[0]) + 10, int(self.center[1]) + 10)
