import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,200,300,400) # (x축 위치, y축 위치, 윈도우의 너비, 윈도우의 높이)
        self.setWindowTitle("PyQt") # 윈도우 타이틀바의 텍스트를 'PyQt'로 변경
        self.setWindowIcon(QIcon("gingerbread.JPG"))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()