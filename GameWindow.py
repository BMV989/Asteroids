import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QRect, QEvent
from PyQt5.QtGui import QImage, QPainter, QFont
from PyQt5.QtWidgets import QLabel, QSizePolicy, QApplication, QWidget


class GameWindow(QWidget):
    def __init__(self, width, height):
        super().__init__()  # бесполезная залупа

        self.width = width
        self.height = height

        self.resize(self.width, self.height)

        self.image = QImage(self.width, self.height, QImage.Format_RGB32)
        self.image.fill(Qt.black)

    def game_loop(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())
