from PyQt5.QtCore import QPoint, QSize, Qt
from math import cos, sin, radians, pi

from PyQt5.QtGui import QPainter, QPen, QColor

from src import constants
from src.entities.movable_object import MovableObject


class Bullet(MovableObject):
    def __init__(self, pos: QPoint, deg: int):
        super().__init__(pos, QSize(8, 8), deg)

    def upd(self):
        if 0 <= self.deg <= 90:
            self.pos.setX(self.pos.x() - int(30 * sin(self.deg / 180 * pi)))
            self.pos.setY(self.pos.y() - int(30 * cos(self.deg / 180 * pi)))
        elif 90 < self.deg <= 180:
            self.pos.setX(self.pos.x() - int(30 * sin(pi - self.deg / 180 * pi)))
            self.pos.setY(self.pos.y() + int(30 * cos(pi - self.deg / 180 * pi)))
        elif 180 < self.deg <= 270:
            self.pos.setX(self.pos.x() + int(30 * cos(pi * 3 / 2 - self.deg / 180 * pi)))
            self.pos.setY(self.pos.y() + int(30 * sin(pi * 3 / 2 - self.deg / 180 * pi)))
        elif 270 < self.deg <= 360:
            self.pos.setX(self.pos.x() + int(30 * sin(pi * 2 - self.deg / 180 * pi)))
            self.pos.setY(self.pos.y() - int(30 * cos(pi * 2 - self.deg / 180 * pi)))

    def is_out_of_bounds(self):
        return not (0 <= self.pos.x() <= constants.WINDOW_WIDTH
                    and 0 <= self.pos.y() <= constants.WINDOW_HEIGHT)

    def paint(self, painter: QPainter):
        painter.setPen(QPen(Qt.white, 4, Qt.SolidLine))
        painter.drawPoint(self.pos)
