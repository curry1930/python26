import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Click!", self)
        self.setGeometry(0, 0, 500, 500)
        self.label = QLabel("Hello",self)
        self.initUI()

    def initUI(self):
        self.button.setStyleSheet("Font-size: 30px;")
        self.button.setGeometry(150, 200, 200, 100)
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(200, 300, 400, 100)
        self.label.setStyleSheet("Font-size: 50px;")

    def on_click(self):
        #print("Button Clicked!")
        #self.button.setText("Clicked!")
        #self.button.setDisabled(True)
        self.label.setText("Thank you!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()   
    sys.exit(app.exec_())         

