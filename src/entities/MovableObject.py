from abc import ABC, abstractmethod

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter

from src import constants


class MovableObject(ABC):
    def __init__(self, position: QPoint, speed: float = 0, deg: int = 0):
        self.pos = position
        self.speed = speed
        self.deg = deg

    @abstractmethod
    def upd(self):
        pass

    @abstractmethod
    def paint(self, painter: QPainter):
        pass

    def update_with_bounds(self):
        self.upd()
        self.pos.setX((self.pos.x() + constants.WIDOW_WIDTH) % constants.WIDOW_WIDTH)
        self.pos.setY((self.pos.y() + constants.WIDOW_HEIGHT) % constants.WIDOW_HEIGHT)