from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QFont, QPainter
from PyQt5.QtWidgets import QLabel, QWidget, QSizePolicy


class StartWidget(QWidget):
    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height

        self.resize(self.width, self.height)

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
        image = QImage(self.width, self.height, QImage.Format_RGB32)
        image.fill(Qt.black)
        painter = QPainter(self)
        painter.drawImage(self.rect(), image, image.rect())
