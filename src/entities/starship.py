from math import sin, cos, pi

from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtGui import QPainter

from src import constants
from src.entities.movable_object import MovableObject


class Starship(MovableObject):
    def __init__(self):
        super().__init__(QPoint(constants.WIDOW_WIDTH // 2, constants.WIDOW_HEIGHT // 2), QSize(45, 60))

    def upd(self):
        pass

    def paint(self, painter: QPainter):
        pass
