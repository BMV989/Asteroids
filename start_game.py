import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QRect, QEvent
from PyQt5.QtGui import QImage, QPainter, QFont
from PyQt5.QtWidgets import QLabel, QSizePolicy, QApplication

from main_game import GameWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        screen = QApplication.primaryScreen()
        self._size = screen.size()
        print(self._size.width(), self._size.height())

        self.setWindowTitle("Asteroids")

        self.setGeometry(0, 0, self._size.width(), self._size.height())
        self.image = QImage(self.size(), QImage.Format_RGB32)  # берет размеры из setGeometry
        self.image.fill(Qt.black)  # Qt.black Qt.white

        label = QLabel("Asteroids", self)
        label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        label.setGeometry(0, 0, 900, 250)  # -48
        label.setIndent(0)
        h = self._size.height() // 4 - 250 // 2 - 48
        w = self._size.width() // 2 - 900 // 2
        label.move(w, h)
        label.setStyleSheet("""
            color: White;
        """)
        label.setFont(QFont("Times", 100))

        label = QLabel("Press space to play", self)
        label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label.setGeometry(0, 0, 1200, 250)  # -48
        h1 = 5 * self._size.height() // 8 - 250 // 2 - 48
        w1 = self._size.width() // 2 - 1200 // 2
        label.move(w1, h1)
        label.setStyleSheet("""
            color: White;
        """)
        label.setFont(QFont("Times", 70))

        self.show()

        self.showMaximized()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            game = GameWindow(self._size.width(), self._size.height(), self.image)
            self.clear()
            self.setCentralWidget(game)
            game.game_loop()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
