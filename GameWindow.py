import sys
import time
from multiprocessing import Process
import threading

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QRect, QEvent
from PyQt5.QtGui import QImage, QPainter, QFont, QPen
from PyQt5.QtWidgets import QLabel, QSizePolicy, QApplication, QWidget

from Objects.Starship import Starship


class GameWindow(QWidget):
    def __init__(self, width, height):
        super().__init__()

        self.lock = True
        self.width = width
        self.height = height

        self.resize(self.width, self.height)

        self.image = QImage(self.width, self.height, QImage.Format_RGB32)
        self.image.fill(Qt.black)
        self.starship = Starship(self.width, self.height)
        self.starship_cords = self.starship.calc_cords()

    def game_prestart(self):
        pass

    # def game_loop(self):
    #     self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())
        # draw starship
        painter.setPen(QPen(Qt.white, 3, Qt.SolidLine))
        c1, c2, c3, c4, c5 = self.starship_cords
        # print("")
        # print(c1, c2, c3, c4, c5)
        painter.drawLine(*c1, *c2)
        painter.drawLine(*c1, *c3)
        painter.drawLine(*c4, *c5)
        painter.end()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.starship.rotate(10)
            self.starship.calc_cords()
            # self.update()

    def on_rotate_left(self):
        self.starship.rotate(5)
        self.starship_cords = self.starship.calc_cords()
        self.update()

    def on_rotate_right(self):
        self.starship.rotate(-5)
        self.starship_cords = self.starship.calc_cords()
        self.update()

    def proc_a(self, v, a):
        self.lock = False
        while v[0] > 0 or v[1] > 0:
            print("bebra")
            a[0] -= 1
            a[1] -= 1
            self.starship.move(0)
            self.starship_cords = self.starship.calc_cords()
            time.sleep(1)
            print(a, v)
        a[0] = 0
        a[1] = 0
        self.lock = True

    def upd(self):
        print("bebra2")
        self.update()

    def on_move_forward(self):  # fix threading
        self.starship.move(3)
        v = self.starship.get_v()
        a = self.starship.get_a()
        self.starship_cords = self.starship.calc_cords()
        self.update()
        print(self.lock)
        t1 = threading.Thread(target=self.proc_a, args=(v, a))
        t2 = threading.Thread(target=self.upd, args=())
        if self.lock:
            t1.start()
            t2.start()
            t1.join()
            t2.join()
