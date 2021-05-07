# 스레드 실습

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Worker(QThread):
    def run(self):
        while 1: 
            print("hi")
            self.sleep(1)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.start()

app = QApplication(sys.argv)
myWindow = MyWindow()
myWindow.show()
app.exec_()