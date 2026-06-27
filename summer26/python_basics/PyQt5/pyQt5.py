# PyQt5 introduction

#boiler plate for a basic window

#import sys
#from PyQt5.QtWidgets import QApplication, QMainWindow

#class Mainwindow(QMainWindow):
#    def __init__(self):
#        super().__init__()

#def main():
#    app = QApplication(sys.argv)
#    window = Mainwindow()
#    window.show()  
#    sys.exit(app.exec_())      

#if __name__ == "__main__":
#    main()    


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel #to write anything inside window 
from PyQt5.QtGui import QFont              #used for fonts adjustments
from PyQt5.QtCore import Qt                #used for allignments
from PyQt5.QtGui import QPixmap            #used for image processing 
#from PyQt5.QtGui import QIcon             #to work with windows icon

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        import os
        print(os.getcwd())
        self.setWindowTitle("My first GUI")
        self.setGeometry(0, 0, 500, 500)                #self.setGeometry(x, y, width, height)
                                                        # x, y is 0,0 then window will appear on the top
                                                        #left corner and width, height is size of the
                                                        #the window (pixels of the window)
        #self.setWindowIcon(QIcon("banan_icon.jpg")) 

        #label = QLabel("Hello", self)   
        #label.setFont(QFont("Arial", 30))
        #label.setGeometry(0, 0, 500, 50)  
        #label.setStyleSheet("color: red;"
        #                    "background: pink;"
        #                    "font-weight: bold;"
        #                    "font-style: italic;"
        #                    "text-decoration: underline;") 

        #label.setAlignment(Qt.AlignTop)                 #aligns vertically top 
        #label.setAlignment(Qt.AlignBottom)               #aligns vertically bottom
        #label.setAlignment(Qt.AlignVCenter)              #aligns in vertically center

        #label.setAlignment(Qt.AlignRight)                #aligns horzontally right
        #label.setAlignment(Qt.AlignHCenter)               #aligns horzontally center
        #label.setAlignment(Qt.AlignLeft)                  #aligns horizontally left

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)      #center and top
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)   #center and bottom
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  #center both
        #label.setAlignment(Qt.AlignCenter)

        #working with image
        label_1 = QLabel(self)
        label_1.setGeometry(0, 0, 250, 250)
        pixMap = QPixmap("/Users/abhinavkumarchoubey/Documents/languages/summer26/python_basics/PyQT5/banan_icon.jpeg")
        label_1.setPixmap(pixMap)
        label_1.setScaledContents(True)
        label_1.setGeometry((self.width() - label_1.width()) // 2, 
                            (self.height() - label_1.height()) // 2,
                            label_1.width(),
                            label_1.height())


def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()  
    sys.exit(app.exec_())      

if __name__ == "__main__":
    main() 