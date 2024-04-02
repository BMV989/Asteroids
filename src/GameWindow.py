
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QImage, QPainter, QPen
from PyQt5.QtWidgets import QWidget

from src.entities.BigAsteroid1 import BigAsteroid1
from src.entities.Starship import Starship


class GameWindow(QWidget):
    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height

        self.resize(self.width, self.height)

        self.image = QImage(self.width, self.height, QImage.Format_RGB32)
        self.image.fill(Qt.black)
        self.starship = Starship(self.width, self.height)
        self.asteroids = [BigAsteroid1()]

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())
        painter.setPen(QPen(Qt.white, 3, Qt.SolidLine))
        self.starship.paint(painter)
        for aster in self.asteroids:
            aster.paint(painter)

    def on_rotate_left(self):
        self.starship.rotate(15)
        self.update()

    def on_rotate_right(self):
        self.starship.rotate(-15)
        self.update()
"""
    def proc_a(self, v, a):
        while v[0] > 0 or v[1] > 0:
            a[0] -= 1
            a[1] -= 1
            self.starship.move(0)
            time.sleep(1)
            print(a, v)
        a[0] = 0
        a[1] = 0

    def upd(self):
        self.update()
"""
    def on_move_forward(self):
        pass
        """
        self.starship.move(3)
        self.starship.get_v()
        self.starship.get_a()
        self.update()
        pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

        if threading.Lock():
            pool.submit(self.proc_a)
            pool.submit(self.upd)
            pool.shutdown(wait=True)
"""