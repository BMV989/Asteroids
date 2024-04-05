from PyQt5.QtCore import QPoint, QSize, Qt
from math import cos, sin, radians

from PyQt5.QtGui import QPainter, QPen, QColor

from src import constants
from src.entities.movable_object import MovableObject


class Bullet(MovableObject):
    def __init__(self, pos: QPoint, deg: int):
        super().__init__(pos, QSize(4, 4), deg)
        self.speed = 12

    def upd(self):
        self.pos.setX(int(self.pos.x() + self.speed * sin(radians(self.deg))))
        self.pos.setY(int(self.pos.y() - self.speed * cos(radians(self.deg))))

    def is_out_of_bounds(self):
        return not (0 <= self.pos.x() <= constants.WIDOW_WIDTH
                    and 0 <= self.pos.y() <= constants.WIDOW_HEIGHT)

    def paint(self, painter: QPainter):
        painter.setPen(QPen(QColor(Qt.white), 2, Qt.SolidLine))
        painter.translate(self.pos.x(), self.pos.y())
        painter.drawRoundedRect(0, 0, self.size.width(), self.size.height(), 1, 1)
        painter.translate(-self.pos.x(), -self.pos.y())
        painter.setPen(QPen(QColor(Qt.white), 3, Qt.SolidLine))
