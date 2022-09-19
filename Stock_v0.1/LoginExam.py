#####################################################################
#   LoginExam.py
#       - This shows how to login at Kiwoom by using openAPI
#           . 키움증권 login sample code
#   written by jslee
#   date : 2000.00.00
#####################################################################



import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyStock')
        self.setGeometry(300, 300, 300, 150)

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        ret = self.kiwoom.dynamicCall('CommConnect()')
        
        
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        self.text_edit.setEnabled(False)

        self.kiwoom.OnEventConnect.connect(self.event_connect)
        

    
    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append('로그인 성공')
            


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    print(f'Done..')