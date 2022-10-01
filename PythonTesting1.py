import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        outerLayout = QVBoxLayout()
        toplayout = QHBoxLayout()
        lowerLayout = QHBoxLayout()

        toplayout.addWidget(QLabel("RPM  "), 1)
        toplayout.addWidget(QLabel("Speed"), 2)
        toplayout.addWidget(QLabel("Throttle"), 3)
        toplayout.addStretch()

        lowerLayout.addWidget(QPushButton("ADD"), 0)
        lowerLayout.addWidget(QPushButton("Lower"), 1)
        lowerLayout.addWidget(QPushButton("Manage"), 2)
        lowerLayout.addStretch()

        outerLayout.addLayout(toplayout)
        outerLayout.addLayout(lowerLayout)

        self.setLayout(outerLayout)
        self.setGeometry(100, 100, 200, 100)
        self.setWindowTitle("Push for window")


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
