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
        label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        label.setGeometry(0, 0, 900, 250)  # -48
        label.setIndent(0)
        h = self.height // 4 - 250 // 2 - 48
        w = self.width // 2 - 900 // 2
        label.move(w, h)
        label.setStyleSheet("""
                    color: White;
                """)
        label.setFont(QFont("Times", 100))

        label = QLabel("Press space to play", self)
        label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label.setGeometry(0, 0, 1200, 250)  # -48
        h1 = 5 * self.height // 8 - 250 // 2 - 48
        w1 = self.width // 2 - 1200 // 2
        label.move(w1, h1)
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

        self.next_window = False

        screen = QApplication.primaryScreen()
        self.size = screen.size()
        self.width = self.size.width()
        self.height = self.size.height()
        self.resize(self.width, self.height)

        self.setWindowTitle("Asteroids")

        self.start_screen = StartWidget(self.width, self.height)
        self.game = GameWindow(self.width, self.height)
        self.setCentralWidget(self.start_screen)

        self.showMaximized()
        # start_screen.setLayout(self.layout())

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Space) and (not self.next_window):
            self.next_window = True
            self.start_screen.hide()
            self.setCentralWidget(self.game)
            self.showMaximized()
            # self.game.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
