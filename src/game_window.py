from copy import copy

from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QImage, QPainter, QPen
from PyQt5.QtWidgets import QWidget

from src import constants
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
        self.asteroids = [Asteroid() for _ in range(6)]
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.game_loop)

    def game_loop(self):
        if len(self.asteroids) < 6:
            self.asteroids.append(Asteroid())
        for aster in self.asteroids:
            if aster.kind != 3:
                pass
            aster.upd()

            if self.starship.is_in_collision_with(aster):
                print("you lose")
                self.starship = Starship()
                self.bullets = []
                self.asteroids = [Asteroid() for _ in range(6)]

        self.starship.upd()
        bullets_for_del = set()
        asteroids_for_del = set()
        for bullet in self.bullets:
            bullet.upd()
            for asteroid in self.asteroids:
                if bullet.is_in_collision_with(asteroid):
                    bullets_for_del.add(bullet)
                    # self.asteroids.remove(asteroid)
                    asteroids_for_del.add(asteroid)
            if bullet.is_out_of_bounds():
                bullets_for_del.add(bullet)
        for bullet in bullets_for_del:
            self.bullets.remove(bullet)
        for asteroid in asteroids_for_del:
            self.asteroids.remove(asteroid)
            if asteroid.kind > 1:
                self.asteroids.append(Asteroid(asteroid.kind - 1, copy(asteroid.pos)))  # необходима копия
                self.asteroids.append(Asteroid(asteroid.kind - 1, copy(asteroid.pos)))

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
