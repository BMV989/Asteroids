from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QImage, QPainter, QPen
from PyQt5.QtWidgets import QWidget

from src.entities.asteroid import Asteroid
from src.entities.bullet import Bullet
from src.entities.starship import Starship


class GameWindow(QWidget):
    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.bullets = []
        self.resize(self.width, self.height)

        self.starship = Starship()
        self.asteroids = [Asteroid() for _ in range(4)]
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.game_loop)

    def game_loop(self):
        for aster in self.asteroids:
            aster.upd()
        self.starship.upd()
        for bullet in self.bullets:
            bullet.upd()
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
        for bullet in self.bullets:
            bullet.paint(painter)

    def shoot(self):
        self.bullets.append(
            Bullet(QPoint(self.starship.side_x0, self.starship.side_y0), self.starship.angle_rotation))

    def on_move(self):
        self.starship.fast_forward_mode = True

    def stop_move(self):
        self.starship.fast_forward_mode = False

    def on_rotate_left(self):
        self.starship.rotate_left = True

    def stop_rotate_left(self):
        self.starship.rotate_left = False

    def on_rotate_right(self):
        self.starship.rotate_right = True

    def stop_rotate_right(self):
        self.starship.rotate_right = False

    def on_move_forward(self):
        self.starship.move()
        self.starship.calc_all_cords()