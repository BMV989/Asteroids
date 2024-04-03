from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter


from src.entities.asteroids.BaseAsteroid import BaseAsteroid


class BigAsteroidA(BaseAsteroid):
    def __init__(self):
        super().__init__()

    def paint(self, painter: QPainter):
        a = QPoint(self.pos.x() - 67, self.pos.y() + 31)
        b = QPoint(self.pos.x() - 48, self.pos.y() - 4)
        c = QPoint(self.pos.x() - 68, self.pos.y() - 40)
        d = QPoint(self.pos.x() - 24, self.pos.y() - 75)
        e = QPoint(self.pos.x(), self.pos.y() - 56)
        f = QPoint(self.pos.x() + 39, self.pos.y() - 75)
        g = QPoint(self.pos.x() + 74, self.pos.y() - 40)
        h = QPoint(self.pos.x() + 33, self.pos.y() - 22)
        i = QPoint(self.pos.x() + 75, self.pos.y() + 14)
        j = QPoint(self.pos.x() + 32, self.pos.y() + 67)
        w = QPoint(self.pos.x() - 17, self.pos.y() + 47)
        v = QPoint(self.pos.x() - 32, self.pos.y() + 67)
        painter.drawLine(a, b)
        painter.drawLine(b, c)
        painter.drawLine(c, d)
        painter.drawLine(d, e)
        painter.drawLine(e, f)
        painter.drawLine(f, g)
        painter.drawLine(g, h)
        painter.drawLine(h, i)
        painter.drawLine(i, j)
        painter.drawLine(j, w)
        painter.drawLine(w, v)
        painter.drawLine(v, a)
