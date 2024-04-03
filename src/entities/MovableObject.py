from abc import ABC, abstractmethod

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter

from src import constants


class MovableObject(ABC):
    def __init__(self, position: QPoint):
        self.pos = position

    @abstractmethod
    def upd(self):
        pass

    @abstractmethod
    def paint(self, painter: QPainter):
        pass

    def update_with_bounds(self):
        self.upd()
        self.pos.setX((self.pos.x() + constants.WIDOW_WIDTH) % constants.WIDOW_WIDTH)
        self.pos.SetY((self.pos.y() + constants.WIDOW_HEIGHT) % constants.WIDOW_HEIGHT)