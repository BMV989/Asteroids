import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QRect, QEvent
from PyQt5.QtGui import QImage, QPainter, QFont
from PyQt5.QtWidgets import QLabel, QSizePolicy, QApplication, QWidget


class GameWindow(QWidget):
    def __init__(self, width, height, background):
        super().__init__()  # бесполезная залупа

        self._width = width
        self._height = height
        self._img = background

        # self.setGeometry(0, 0, self._size.width(), self._size.height())

        self.show()


    def game_loop(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())
