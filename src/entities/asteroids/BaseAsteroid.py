from abc import ABC
from math import sin, cos
from random import randint, uniform

from PyQt5.QtCore import QPoint

from src import constants
from src.entities.MovableObject import MovableObject


class BaseAsteroid(MovableObject, ABC):
    def __init__(self):
        pos = QPoint(randint(0, constants.WIDOW_WIDTH), randint(0, constants.WIDOW_HEIGHT))
        speed = int(uniform(1.5, 3))
        deg = randint(0, 11) * 30
        super().__init__(pos, speed, deg)

    def upd(self):
        self.pos.setX(int(self.pos.x() + self.speed * sin(self.deg * constants.DEG_TO_RAD)))
        self.pos.setY(int(self.pos.y() - self.speed * cos(self.deg * constants.DEG_TO_RAD)))
