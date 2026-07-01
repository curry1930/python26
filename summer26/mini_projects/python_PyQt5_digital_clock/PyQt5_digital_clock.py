#Python PyQt5 digital clock

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_lable = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_lable)
        self.setLayout(vbox)

        self.time_lable.setAlignment(Qt.AlignCenter)

        self.time_lable.setStyleSheet("Font-size: 80px;"
                                      "Color: hsl(124, 98%, 50%);")
        
        font_id = QFontDatabase.addApplicationFont("/Users/abhinavkumarchoubey/Documents/languages/summer26/mini_projects/python_PyQt5_digital_clock/digital-7.ttf") 
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_lable.setFont(my_font)

        self.setStyleSheet("background-color: black;")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")       #hh, mm, ss are format specifier
        self.time_lable.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
