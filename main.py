from PyQt5.QtWidgets import QWidget,QDesktopWidget,QApplication,QPushButton,QLineEdit,QTextEdit
from PyQt5 import QtGui
import sys
import answer as an

class Viewer(QWidget):
    sizex=1100
    sizey=900

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
         #채팅로그창
        self.tx1=QTextEdit('',self)
        self.tx1.move(20,20)
        self.tx1.resize(self.sizex-40,self.sizey*4//5)
        self.tx1.setDisabled(True)
        self.tx1.setStyleSheet("color: black;"
                             "border-style: solid;"
                             "border-width: 2px;"
                             "border-color: #000000;"
                             "border-radius: 3px")
        self.tx1.setCurrentFont(QtGui.QFont("맑은 고딕",10))

        #입력창
        self.li1=QLineEdit('',self)
        self.li1.move(20,self.sizey*4//5+30)
        self.li1.resize(self.sizex-120,self.sizey*1//5-40)
        self.li1.returnPressed.connect(self.btn1clickevent)

        #엔터버튼
        self.btn1=QPushButton('↵',self)
        self.btn1.setCheckable(False)
        self.btn1.move(self.sizex-100,self.sizey*4//5+30)
        self.btn1.resize(80,self.sizey*1//5-40)
        self.btn1.clicked.connect(self.btn1clickevent)
        
        #기본 설정
        self.setWindowTitle('5조 동의대 컴공과 챗봇 GUI')
        self.resize(self.sizex,self.sizey)
        self.center()
        self.show()
        
    #화면 중앙에 창 표시
    def center(self):
        a=self.frameGeometry()
        b=QDesktopWidget().availableGeometry().center()
        a.moveCenter(b)
        self.move(a.topLeft())

    #채팅로그에 쓰기 이벤트
    def btn1clickevent(self):
        text=self.li1.text()
        self.tx1.setTextColor(QtGui.QColor(0,0,0))
        self.tx1.append('me>> '+text+'\n')

        self.tx1.setTextColor(QtGui.QColor(0,0,255))
        self.tx1.append(an.chatbotfn(text)+'\n\n')
        ####챗봇에 text 쓰기 후 답변 출력?

        self.li1.clear()       

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=Viewer()
    sys.exit(app.exec_())