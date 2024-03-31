import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QRect, QEvent
from PyQt5.QtGui import QImage, QPainter, QFont
from PyQt5.QtWidgets import QLabel, QSizePolicy, QApplication, QWidget

from GameWindow import GameWindow


class StartWidget(QWidget):
    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height
        print(self.width, self.height)

        self.resize(self.width, self.height)

        self.image = QImage(self.width, self.height, QImage.Format_RGB32)
        self.image.fill(Qt.black)

        label = QLabel("Asteroids", self)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label.setGeometry(250, 0, 900, 550)  # -48
        label.setStyleSheet("""
                    color: White;
                """)
        label.setFont(QFont("Times", 100))

        label = QLabel("Press space to play", self)
        label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label.setGeometry(0, 300, 1000, 250)  # -48

        label.setStyleSheet("""
                    color: White;
                """)
        label.setFont(QFont("Times", 70))

        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.in_move = False

        self.is_start = True

        screen = QApplication.primaryScreen()
        self.size = screen.size()
        self.width = self.size.width()
        self.height = self.size.height()
        self.resize(self.width, self.height)

        self.setWindowTitle("Asteroids")

        self.start_screen = StartWidget(self.width, self.height)
        self.game = GameWindow(self.width, self.height)
        self.setCentralWidget(self.start_screen)

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Space) and self.is_start:
            self.is_start = False
            self.start_screen.hide()
            self.setCentralWidget(self.game)
            self.showMaximized()

        if event.key() == Qt.Key_Left:
            self.game.on_rotate_left()
        if event.key() == Qt.Key_Right:
            self.game.on_rotate_right()

        if event.key() == Qt.Key_Up:
            print("bebra")
            self.in_move = True
            self.game.on_move_forward()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
