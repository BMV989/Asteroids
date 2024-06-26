from copy import copy
import os
from random import randint

from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QImage, QPainter, QPen, QFont
from PyQt5.QtWidgets import QWidget

from src import constants
from src.entities.asteroid import Asteroid
from src.entities.bullet import Bullet
from src.entities.starship import Starship


class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.game_loop)

        self.init_game()

    def game_loop(self):
        asteroids_for_del = set()
        big_asters = 0
        self.starship.upd()
        for i in self.asteroids:
            if i.kind == 3:
                big_asters += 1
        if big_asters < 6:  # len(self.asteroids)
            big_asters += 1
            self.asteroids.append(Asteroid())
        for aster in self.asteroids:
            aster.upd()

            if not self.starship.is_in_collision_with(aster):
                continue
            self.lives -= 1
            if self.lives == 0:
                os.makedirs("./resources", exist_ok=True)
                hs_score = self.get_hs_score()
                with open("./resources/hs_score.txt", "w") as f:
                    if hs_score == '':
                        f.write(str(self.score))
                    else:
                        f.write(str(max(int(hs_score), self.score)))
                return self.init_game()
            self.starship.reset()
            asteroids_for_del.add(aster)
        bullets_for_del = set()
        for bullet in self.bullets:
            bullet.upd()

            for asteroid in self.asteroids:
                if bullet.is_in_collision_with(asteroid):
                    bullets_for_del.add(bullet)
                    asteroids_for_del.add(asteroid)

            if bullet.is_out_of_bounds():
                bullets_for_del.add(bullet)

        for bullet in bullets_for_del:
            self.bullets.remove(bullet)

        for aster in asteroids_for_del:
            self.destroy_aster(aster)

        self.update()

    def paintEvent(self, event):
        image = QImage(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT, QImage.Format_RGB32)
        image.fill(Qt.black)
        painter = QPainter(self)
        painter.drawImage(self.rect(), image, image.rect())
        painter.setPen(QPen(Qt.white, 3, Qt.SolidLine))
        self.starship.paint(painter)
        for aster in self.asteroids:
            aster.paint(painter)
        for bullet in self.bullets:
            bullet.paint(painter)
        painter.setFont(QFont('Courier New', 24))
        painter.drawText(10, 60, str(self.score))
        painter.drawText(10, 100, "A" * self.lives)
        painter.drawText(10, 140, f"HS:{self.get_hs_score()}")

    def shoot(self):
        self.bullets.append(
            Bullet(QPoint(self.starship.side_x0, self.starship.side_y0), self.starship.angle_rotation))

    def on_move(self):
        self.starship.fast_forward_mode = True

    def stop_move(self):
        self.starship.fast_forward_mode = False

    def on_rotate_left(self):
        self.starship.rotation_direction = 1

    def stop_rotate(self):
        self.starship.rotation_direction = 0

    def on_rotate_right(self):
        self.starship.rotation_direction = -1

    def on_move_forward(self):
        self.starship.move()
        self.starship.calc_all_cords()

    @staticmethod
    def get_hs_score():
        try:
            with open("./resources/hs_score.txt", "r") as f:
                return f.readline()
        except FileNotFoundError:
            return 0

    def destroy_aster(self, aster: Asteroid):
        reward = {
            1: 100,
            2: 50,
            3: 20
        }
        self.asteroids.remove(aster)
        self.score += reward[aster.kind]
        if aster.kind > 1:
            ang_1 = randint(0, 11) * 30
            ang_2 = 360 - ang_1
            if ang_1 == 0 or ang_1 == 360:
                ang_2 = 180
            elif ang_1 == 180:
                ang_2 = 0
            self.asteroids.append(Asteroid(aster.kind - 1, copy(aster.pos), degree=ang_1))  # необходима копия
            self.asteroids.append(Asteroid(aster.kind - 1, copy(aster.pos), degree=ang_2))

    def init_game(self):
        self.starship = Starship()
        self.asteroids = [Asteroid() for _ in range(6)]
        self.bullets = []
        self.score = 0
        self.lives = constants.LIVES
