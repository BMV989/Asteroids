from __future__ import annotations

from abc import ABC, abstractmethod

from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtGui import QPainter

from src import constants


class MovableObject(ABC):
    def __init__(self, position: QPoint, size: QSize, deg: int = 0):
        self.size = size
        self.pos = position
        self.deg = deg

    @abstractmethod
    def upd(self):
        pass

    @abstractmethod
    def paint(self, painter: QPainter):
        pass

    def is_in_collision_with(self, other: MovableObject) -> bool:
        return (self.pos.x() < other.pos.x() + other.size.width() and
                self.pos.x() + self.size.width() > other.pos.x() and
                self.pos.y() < other.pos.y() + other.size.height() and
                self.pos.y() + self.size.height() > other.pos.y())
