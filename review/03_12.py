import sys
from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QIcon

app = QApplication(sys.argv) # QApplication 객체 생성 
label = QLabel("Hello") # 라벨 출력 
label.show() # 창 띄우기 
app.exec_() # 창 유지 
