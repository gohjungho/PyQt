import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼 클릭")

# QApplication 객체 생성 및 이벤트 루프 생성 코드 
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()