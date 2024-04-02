from abc import ABC, abstractmethod

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter


class MovableObject(ABC):
    def __init__(self, position: QPoint):
        self.pos = position

    @abstractmethod
    def paint(self, painter: QPainter):
        pass
