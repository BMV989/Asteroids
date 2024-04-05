from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from src import constants
from src.game_window import GameWindow
from src.start_widget import StartWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(constants.WIDOW_WIDTH, constants.WIDOW_HEIGHT)

        self.setWindowTitle("Asteroids")

        self.start_screen = StartWidget(constants.WIDOW_WIDTH, constants.WIDOW_HEIGHT)
        self.game = GameWindow(constants.WIDOW_WIDTH, constants.WIDOW_HEIGHT)
        self.setCentralWidget(self.start_screen)

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Space) and self.start_screen.isActiveWindow():
            self.start_screen.hide()
            self.setCentralWidget(self.game)
            self.game.timer.start(1000 // constants.FPS)

        elif event.key() == Qt.Key_Left:
            self.game.on_rotate_left()
        elif event.key() == Qt.Key_Right:
            self.game.on_rotate_right()

        elif event.key() == Qt.Key_Up:
            self.game.on_move_forward()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Up: pass
