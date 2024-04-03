import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPainter, QFont
from PyQt5.QtWidgets import QLabel, QSizePolicy, QWidget

import constants
from GameWindow import GameWindow
from src.MainWindow import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
