#####################################################################
#   ExamPython.py
#       - This shows how to use 
#           . description
#   written by jslee
#   date : 2000.00.00
#####################################################################


import numpy as np
import win32com.client
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyStock')
        self.setGeometry(300, 300, 300, 400)
    
        btn1 = QPushButton('Click me', self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        QMessageBox.about(self, 'message', 'clicked')




if __name__ == '__main__':
    
    
    """
    ###################################################################
    # COM(Component Object Management) exam
    ###################################################################
    # explore 창 생성
    explore = win32com.client.Dispatch("InternetExplorer.Application")	
    explore.Visible = True

    # excel 창 생성
    excel = win32com.client.Dispatch("Excel.Application")	
    excel.Visible = True
    ###################################################################
    """
    
    '''
    # pyqt exam
    app = QApplication(sys.argv)
    print(sys.argv)
    label = QLabel('Hello PyQt')
    label.show()
    app.exec_()
    '''
    
    # MyWindow class 실행
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()    
    app.exec_()
    
    
    
    
    
    print(f'Done..')