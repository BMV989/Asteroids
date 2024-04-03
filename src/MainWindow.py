from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from src import constants
from src.GameWindow import GameWindow
from src.StartWidget import StartWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.is_start = True
        self.on_move = False

        self.width = constants.WIDOW_WIDTH
        self.height = constants.WIDOW_HEIGHT
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
            # self.showMaximized()

        elif event.key() == Qt.Key_Left:
            self.game.on_rotate_left()
        elif event.key() == Qt.Key_Right:
            self.game.on_rotate_right()

        elif event.key() == Qt.Key_Up:
            self.on_move = True
            self.game.on_move_forward()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.on_move = False
            # self.game.zero_a()
