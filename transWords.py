import sys
import os
import json
import time
from PyQt5 import QtWidgets, uic
from MainWindow import Ui_MainWindow
from TwCommon import Lang
from ConfigOperation import ConfigOperation
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QTextCursor


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.plainTextEdit_English.hide()
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('Canada.ico'))   
        
        # read config file
        self.cfg = ConfigOperation()

        # English line number
        self.ChineseDoclist = self.loadDocToList(Lang.Chinese)
        self.englishDoclist = self.loadDocToList(Lang.English)
        #print ("Chinese index:%d English index: %d" % (len(self.ChineseDoclist), len(self.englishDoclist)))
        
        self.plainTextEdit_manualEnter.textChanged.connect(self.manualEnterAction)
        #self.pushButton_submit.clicked.connect(self.submitButtonAction)
        self.pushButton_Exit.clicked.connect(self.close)
        self.pushButton_Prev.clicked.connect(self.preButtonAction)
        self.pushButton_Next.clicked.connect(self.nextButtonAction)
        self.pushButton_openChineseText.clicked.connect(self.openChineseFile)
        self.pushButton_openEnglishText.clicked.connect(self.openEnglishFile)
        self.lineEdit_English_Line_Number.textChanged.connect(self.updateEnglishLineNum)
        self.lineEdit_English_Line_Number.setText(str(self.cfg.getDocLineNum(Lang.English)))
        self.lineEdit_Chinese_File.setText(self.cfg.getDocPath(Lang.Chinese))
        self.lineEdit_English_File.setText(self.cfg.getDocPath(Lang.English))
        self.plainTextEdit_Chinese.setStyleSheet(
        """QPlainTextEdit {background-color: #404040;
                           color: #C0C0C0;
                           font-family: Courier;}""")
        self.plainTextEdit_CN_line.setStyleSheet(
        """QPlainTextEdit {background-color: #404040;
                           color: #CCFFE5;
                           font-family: Courier;}""")
        self.plainTextEdit_manualEnter.setStyleSheet(
        """QPlainTextEdit {background-color: #404040;
                           color: #C0C0C0;
                           font-family: Courier;}""")
        self.plainTextEdit_English.setStyleSheet(
        """QPlainTextEdit {background-color: #404040;
                           color: #C0C0C0;
                           font-family: Courier;}""") #text-decoration: underline; # green color: 00FF00        
        self.displayWindow(Lang.Chinese)
        self.plainTextEdit_CN_line.setPlainText(self.ChineseDoclist[self.cfg.getDocLineNum(Lang.English)])

    def openFile(self, lang):
        _fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if _fileName:
            if lang == Lang.Chinese:
                self.lineEdit_Chinese_File.setText(_fileName)
            elif lang == Lang.English:
                self.lineEdit_English_File.setText(_fileName)

            self.cfg.setDocPath(_fileName, lang)
            if lang == Lang.Chinese:
                self.ChineseDoclist = self.loadDocToList(Lang.Chinese)
                self.plainTextEdit_CN_line.setPlainText(self.ChineseDoclist[self.cfg.getDocLineNum(Lang.English)])
                self.displayWindow(Lang.Chinese)
            elif lang == Lang.English:
                self.englishDoclist = self.loadDocToList(Lang.English)
                self.plainTextEdit_English.setPlainText(self.englishDoclist[self.cfg.getDocLineNum(Lang.English)])

    def openChineseFile(self):
        self.openFile (Lang.Chinese)

            
    def openEnglishFile(self):
        self.openFile (Lang.English)

    def displayWindow(self, lang):
        if not self.cfg.getDocPath(lang):
            text = ("Chinese" if lang==Lang.Chinese else "English") + " file path is not configured!"
        elif os.path.isfile(self.cfg.getDocPath(lang)):
            text = ''
            for line in self.ChineseDoclist:
                text += line
            #text = ''
            #for i in range(self.cfg.getDocLineNum(lang), self.cfg.getDocLineNum(lang)+20):
            #    text += self.ChineseDoclist[i]
            
        else:
            text = "File \"" + self.cfg.getDocPath(lang) + "\" doesn't exist!"
        
        if lang == Lang.Chinese:
            self.plainTextEdit_Chinese.setPlainText(text)
            self.plainTextEdit_Chinese.verticalScrollBar().setValue(self.cfg.getDocLineNum(Lang.English))
        elif lang == Lang.English:
            self.plainTextEdit_English.setPlainText(text)

    def updateEnglishLineNum(self):
        repaint = True
        realLen = len(self.englishDoclist)
        tryStr = self.lineEdit_English_Line_Number.text()
        
        if realLen == 0 or not tryStr:
            n = 0
        else:       
            n = int(tryStr)
            if n < 0:
                n = 0
            elif n >= realLen:
                n = realLen - 1
            else:
                repaint = False
        self.cfg.setDocLineNum(n, Lang.English)
        self.plainTextEdit_Chinese.verticalScrollBar().setValue(self.cfg.getDocLineNum(Lang.English))
        self.plainTextEdit_CN_line.setPlainText(self.ChineseDoclist[self.cfg.getDocLineNum(Lang.English)])
        if repaint:
            self.lineEdit_English_Line_Number.setText('' if n==0 else str(n))

    def manualEnterAction(self):
        text = self.plainTextEdit_manualEnter.toPlainText()
        if '\n' in text:
            text = text.replace('\n', '')
            self.plainTextEdit_manualEnter.setPlainText(text)
            self.plainTextEdit_manualEnter.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor);
            self.submitButtonAction()

    # Only reason to keep this function is for "submit" button which may be added back to ui.
    def submitButtonAction(self): 
        if self.plainTextEdit_English.isVisible():
            self.plainTextEdit_manualEnter.clear()
            self.plainTextEdit_manualEnter.setFocus(1)
            self.plainTextEdit_English.hide()
        else:
            self.plainTextEdit_English.setPlainText(self.englishDoclist[self.cfg.getDocLineNum(Lang.English)])
            self.plainTextEdit_English.show()

    def preButtonAction(self):
        num = self.cfg.getDocLineNum(Lang.English)
        if num > 0:
            self.cfg.setDocLineNum(num-1, Lang.English)
        self.plainTextEdit_manualEnter.clear()
        self.plainTextEdit_English.hide()
        self.lineEdit_English_Line_Number.setText(str(self.cfg.getDocLineNum(Lang.English)))
        self.plainTextEdit_CN_line.setPlainText(self.ChineseDoclist[self.cfg.getDocLineNum(Lang.English)])
        self.plainTextEdit_Chinese.verticalScrollBar().setValue(self.cfg.getDocLineNum(Lang.English))

    def nextButtonAction(self):
        num = self.cfg.getDocLineNum(Lang.English) + 1
        if num < len(self.englishDoclist):
            self.cfg.setDocLineNum(num, Lang.English)
        self.plainTextEdit_manualEnter.clear()
        self.plainTextEdit_English.hide()
        self.lineEdit_English_Line_Number.setText(str(self.cfg.getDocLineNum(Lang.English)))
        self.plainTextEdit_CN_line.setPlainText(self.ChineseDoclist[self.cfg.getDocLineNum(Lang.English)])
        self.plainTextEdit_manualEnter.setFocus(1)
        self.plainTextEdit_Chinese.verticalScrollBar().setValue(self.cfg.getDocLineNum(Lang.English))

    def loadDocToList(self, lang): 
        if os.path.isfile(self.cfg.getDocPath(lang)):
            with open(self.cfg.getDocPath(lang), encoding='utf-8') as f:
                lines = f.readlines()
            lines = [x.strip() for x in lines]
            
            if lang == Lang.Chinese:
                i = 0
                for line in lines:
                    lines[i] = str(i).zfill(3) + ' - ' + line + '\n'
                    i = i + 1

        else:
            lines = ['']
        return lines
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.plainTextEdit_Chinese.verticalScrollBar().setValue(window.cfg.getDocLineNum(Lang.English))

    app.exec()