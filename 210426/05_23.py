# 상승장/하락장 알리미

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pybithumb

tickers = ["BTC", "ETH", "BCH", "ETC"]
form_class = uic.loadUiType("210426/bull.ui")[0] # "폴더이름/파일명"

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        timer = QTimer(self) # 타이머 추가. 정해진 시간 만큼 자동으로 refresh
        timer.start(5000)
        timer.timeout.connect(self.timeout)

        self.tableWidget.setRowCount(len(tickers)) # 화면에 뿌려주는 역할 

    def timeout(self):
        for i, ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, item)

            price, last_ma5, state = self.get_market_infos(ticker)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(last_ma5)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(state))

    def get_market_infos(self, ticker):
        df = pybithumb.get_ohlcv(ticker)
        ma5 = df['close'].rolling(window=5).mean()
        last_ma5 = ma5[-2]
        price = pybithumb.get_current_price(ticker)

        state = None 
        if price > last_ma5:
            state = "상승장" 
        else: 
            state = "하락장"

        return price, last_ma5, state 

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()