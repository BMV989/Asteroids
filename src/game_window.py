from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPainter, QPen
from PyQt5.QtWidgets import QWidget

from src.entities.asteroid import Asteroid
from src.entities.starship import Starship


class GameWindow(QWidget):
    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height

        self.resize(self.width, self.height)

        self.starship = Starship()
        self.asteroids = [Asteroid() for _ in range(4)]
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.game_loop)

    def game_loop(self):
        for aster in self.asteroids:
            aster.update_with_bounds()
        self.update()

    def paintEvent(self, event):
        image = QImage(self.width, self.height, QImage.Format_RGB32)
        image.fill(Qt.black)
        painter = QPainter(self)
        painter.drawImage(self.rect(), image, image.rect())
        painter.setPen(QPen(Qt.white, 3, Qt.SolidLine))
        self.starship.paint(painter)
        for aster in self.asteroids:
            aster.paint(painter)
