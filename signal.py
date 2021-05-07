import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MySignal(QObject):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int, int)

    def run(self):
        self.signal1.emit()
        self.signal2.emit(1, 2)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mysignal = MySignal()
        mysignal.signal1.connect(self.signal1_emitted)
        mysignal.signal2.connect(self.signal2_emitted)
        mysignal.run()


    @pyqtSlot() # 슬롯: 이벤트가 발생할 때 호출되는 함수나 메소드 
    def signal1_emitted(self):
        print("signal1 emitted")

    @pyqtSlot(int, int)
    def signal2_emitted(self, arg1, arg2):
        print("signal1 emitted", arg1, arg2)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()