from math import sin, cos, radians
from random import randint, uniform

from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtGui import QPainter

from src import constants
from src.entities.movable_object import MovableObject


class Asteroid(MovableObject):
    def __init__(self, kind: int = 3, pos: QPoint = None):
        pos = pos or QPoint(randint(0, constants.WINDOW_WIDTH), randint(0, constants.WINDOW_HEIGHT))
        deg = randint(0, 11) * 30
        self.kind = kind
        size = QSize(40 * self.kind, 40 * self.kind)
        #
        r = 20 * self.kind
        #
        super().__init__(pos, size, r, deg)
        width = self.size.width()
        height = self.size.height()
        self.corner_pos = QPoint(int(pos.x() - width//2), int(pos.y() - height//2))
        self.speed = uniform(1.5, 3)
        self.types = {
            1: [
                QPoint(int(width * 0.5), 0), QPoint(int(width * 0.75), int(height * 0.1)),
                QPoint(int(width * 0.6), int(height * 0.55)), QPoint(int(width * 0.9), int(height * 0.8)),
                QPoint(int(width * 0.9), int(height * 0.8)), QPoint(int(width * 0.55), int(height * 0.7)),
                QPoint(int(width * 0.4), int(height * 0.85)), QPoint(int(width * 0.25), int(height * 0.6)),
                QPoint(int(width * 0.08), int(height * 0.75)), QPoint(int(width * 0.125), int(height * 0.5)),
                QPoint(int(width * 0.04), int(height * 0.4)), QPoint(int(width * 0.15), int(height * 0.15))
            ],
            2: [
                QPoint(int(width * 0.25), 0), QPoint(int(width * 0.85), int(height * 0.15)),
                QPoint(int(width * 0.9), int(height * 0.9)), QPoint(int(width * 0.55), height),
                QPoint(int(width * 0.35), int(height * 0.8)), QPoint(int(width * 0.15), int(height * 0.88)),
                QPoint(int(width * 0.2), int(height * 0.6)), QPoint(0, int(height * 0.25)),
                QPoint(int(width * 0.3), int(height * 0.45))
            ],
            3: [
                QPoint(width, height), QPoint(int(width * 0.15), int(height * 0.95)),
                QPoint(int(width * 0.075), int(height * 0.6)), QPoint(int(width * 0.25), int(height * 0.45)),
                QPoint(int(width * 0.2), int(height * 0.15)), QPoint(int(width * 0.5), int(height * 0.03)),
                QPoint(int(width * 0.45), int(height * 0.35)), QPoint(int(width * 0.75), int(height * 0.2)),
                QPoint(int(width * 0.9), int(height * 0.48)), QPoint(width, int(height * 0.55)),
                QPoint(int(width * 0.8), int(height * 0.8))
            ]
        }
        types_keys = list(self.types.keys())
        self.type = randint(types_keys[0], types_keys[-1])

    def upd(self):
        self.pos.setX(int(self.pos.x() + self.speed * sin(radians(self.deg))))
        self.pos.setY(int(self.pos.y() - self.speed * cos(radians(self.deg))))
        self.pos.setX((self.pos.x() + constants.CLOSURE_BUFFER_WIDTH) % constants.CLOSURE_BUFFER_WIDTH)
        self.pos.setY((self.pos.y() + constants.CLOSURE_BUFFER_HEIGHT) % constants.CLOSURE_BUFFER_HEIGHT)
        self.corner_pos.setX(int(self.pos.x() - self.size.width()//2))
        self.corner_pos.setY(int(self.pos.y() - self.size.height()//2))

    def paint(self, painter: QPainter):
        painter.translate(self.corner_pos.x(), self.corner_pos.y())
        painter.drawPolygon(self.types[self.type])
        painter.translate(-self.corner_pos.x(), -self.corner_pos.y())
