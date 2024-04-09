from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QFont, QPainter
from PyQt5.QtWidgets import QLabel, QWidget, QSizePolicy

from src import constants


class StartWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)

        label = QLabel("Asteroids", self)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label.setGeometry(250, 0, 900, 550)  # -48

        label.setStyleSheet("""
                    color: White;
                """)
        label.setFont(QFont("Arial", 100))

        label = QLabel("Press space to play", self)
        label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label.setGeometry(0, 300, 1000, 250)  # -48

        label.setStyleSheet("""
                    color: White;
                """)
        label.setFont(QFont("Arial", 70))

        self.show()

    def paintEvent(self, event):
        image = QImage(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT, QImage.Format_RGB32)
        image.fill(Qt.black)
        painter = QPainter(self)
        painter.drawImage(self.rect(), image, image.rect())
