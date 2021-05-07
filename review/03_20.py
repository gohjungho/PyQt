import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit

form_class = uic.loadUiType("review/mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry) 
        # push를 누르면 뒤 함수를 연결

    def inquiry(self):
        price1 = pykorbit.get_current_price("BTC")
        price2 = pykorbit.get_current_price("ETH")
        # price3 = pyupbit.get_current_price("KRW-DOGE")
        self.lineEdit_1.setText(str(price1)) 
        self.lineEdit_2.setText(str(price2)) 
        # self.lineEdit_3.setText(str(price3))

# QApplication 객체 생성 및 이벤트 루프 생성 코드 
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()