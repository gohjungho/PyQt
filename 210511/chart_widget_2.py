import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtChart import QLineSeries, QChart
from PyQt5.QtGui import QPainter

class ChartWidget(QWidget):
    def __init__(self, parent=None, ticker="BTC"):
        super().__init__(parent)
        uic.loadUi("210510/chart.ui", self)
        self.ticker = ticker
        self.viewLimit = 128 # 데이터의 수

        self.priceData = QLineSeries()
        self.priceData.append(0, 10)
        self.priceData.append(1, 20)
        self.priceData.append(2, 10)

        self.priceChart = QChart()
        self.priceChart.addSeries(self.priceData)

        self.priceView.setChart(self.priceChart)
        self.priceChart.legend().hide()
        self.priceView.setRenderHints(QPainter.Antialiasing)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    cw = ChartWidget()
    cw.show()
    exit(app.exec_())