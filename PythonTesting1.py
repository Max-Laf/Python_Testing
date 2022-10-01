from cgitb import text

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QMessageBox


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lbl_red = QLabel('RPM')
        lbl_green = QLabel('Throttle')
        lbl_blue = QLabel('SPeed')

        lbl_red.setStyleSheet(open('mystylesheet.css').read())
        lbl_green.setStyleSheet(open('mystylesheet.css').read())
        lbl_blue.setStyleSheet(open('mystylesheet.css').read())

        button1 = QPushButton("Show Text")
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20, 20)
        self.textbox1.resize(280, 40)

        button1.setStyleSheet(open('mystylesheet.css').read())
        self.textbox1.setStyleSheet(open('mystylesheet.css').read())

        outerbox = QHBoxLayout()

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.textbox1)
        vbox2.addWidget(button1)

        outerbox.addLayout(vbox, 0)
        outerbox.addLayout(vbox2, 1)
        outerbox.addStretch()

        self.setLayout(outerbox)

        self.setWindowTitle('Programme')
        #self.setGeometry(150, 150, 1500, 800)
        button1.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        print(self.textbox1.text())
        self.textbox1.setText("")


app = QApplication(sys.argv)
app.setStyleSheet(open('mystylesheet.css').read())
ex = MyApp()
sys.exit(app.exec_())