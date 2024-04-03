from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter

from src import constants
from src.entities.MovableObject import MovableObject
from random import randint


class BigAsteroidA(MovableObject):
    def __init__(self):
        self.position = QPoint(randint(120, constants.WIDOW_WIDTH - 120),
                               randint(120, constants.WIDOW_HEIGHT - 120))
        super().__init__(self.position)
        self.a = QPoint(self.position.x() - 67, self.position.y() + 31)
        self.b = QPoint(self.position.x() - 48, self.position.y() - 4)
        self.c = QPoint(self.position.x() - 68, self.position.y() - 40)
        self.d = QPoint(self.position.x() - 24, self.position.y() - 75)
        self.e = QPoint(self.position.x(), self.position.y() - 56)
        self.f = QPoint(self.position.x() + 39, self.position.y() - 75)
        self.g = QPoint(self.position.x() + 74, self.position.y() - 40)
        self.h = QPoint(self.position.x() + 33, self.position.y() - 22)
        self.i = QPoint(self.position.x() + 75, self.position.y() + 14)
        self.j = QPoint(self.position.x() + 32, self.position.y() + 67)
        self.w = QPoint(self.position.x() - 17, self.position.y() + 47)
        self.v = QPoint(self.position.x() - 32, self.position.y() + 67)
    def upd(self):
        pass

    def paint(self, painter: QPainter):
        painter.drawLine(self.a, self.b)
        painter.drawLine(self.b, self.c)
        painter.drawLine(self.c, self.d)
        painter.drawLine(self.d, self.e)
        painter.drawLine(self.e, self.f)
        painter.drawLine(self.f, self.g)
        painter.drawLine(self.g, self.h)
        painter.drawLine(self.h, self.i)
        painter.drawLine(self.i, self.j)
        painter.drawLine(self.j, self.w)
        painter.drawLine(self.w, self.v)
        painter.drawLine(self.v, self.a)
