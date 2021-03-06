import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 위젯 생성 코드 
        self.setGeometry(100,200,300,400) # (x축 위치, y축 위치, 윈도우의 너비, 윈도우의 높이)
        self.setWindowTitle("PyQt") # 윈도우 타이틀바의 텍스트를 'PyQt'로 변경
        self.setWindowIcon(QIcon("gingerbread.JPG"))

        btn = QPushButton("버튼1", self)
        btn.move(10, 10)
        btn.clicked.connect(self.btn_clicked)

        # btn = QPushButton("버튼2", self)
        # btn.move(10, 40)
        # btn.clicked.connect(self.btn_clicked)
    
    # 이벤트 처리 코드 
    def btn_clicked(self): # 현재는 콘솔에 찍힘 
        print("버튼 클릭")

# QApplication 객체 생성 및 이벤트 루프 생성 코드 
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()