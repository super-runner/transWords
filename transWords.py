import sys
import os
import json
from PyQt5 import QtWidgets, uic
from MainWindow import Ui_MainWindow
from TwCommon import Lang
from ConfigOperation import ConfigOperation

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.plainTextEdit_English.hide()
        self.setFixedSize(self.size())
        
        # read config file
        self.cfg = ConfigOperation()

        # English line number
        self.ChineseDoclist = self.loadDocToList(Lang.Chinese)
        self.englishDoclist = self.loadDocToList(Lang.English)
        #print ("Chinese index:%d English index: %d" % (len(self.ChineseDoclist), len(self.englishDoclist)))
        
        self.pushButton_submit.clicked.connect(self.submitButtonAction)
        self.pushButton_Exit.clicked.connect(self.close)
        self.pushButton_Prev.clicked.connect(self.preButtonAction)
        self.pushButton_Next.clicked.connect(self.nextButtonAction)
        self.pushButton_openChineseText.clicked.connect(self.openChineseFile)
        self.pushButton_openEnglishText.clicked.connect(self.openEnglishFile)
        self.lineEdit_English_Line_Number.textChanged.connect(self.updateEnglishLineNum)
        self.lineEdit_English_Line_Number.setText(str(self.cfg.getDocLineNum(Lang.English)))
        self.lineEdit_Chinese_File.setText(self.cfg.getDocPath(Lang.Chinese))
        self.lineEdit_English_File.setText(self.cfg.getDocPath(Lang.English))
        
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
            #text = open(self.cfg.getDocPath(lang), encoding='utf-8').read()
            text = ''
            i = 0
            for line in self.ChineseDoclist:
                text += str(i).zfill(3) + ' - ' + line + '\n'
                i = i + 1
        else:
            text = "File \"" + self.cfg.getDocPath(lang) + "\" doesn't exist!"
        
        if lang == Lang.Chinese:
            self.plainTextEdit_Chinese.setPlainText(text)
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
        self.plainTextEdit_CN_line.setPlainText(self.ChineseDoclist[self.cfg.getDocLineNum(Lang.English)])
        if repaint:
            self.lineEdit_English_Line_Number.setText('' if n==0 else str(n))

        
    def submitButtonAction(self):
        if self.plainTextEdit_English.isVisible():
            self.plainTextEdit_manualEnter.clear()
            self.plainTextEdit_English.hide()
            self.plainTextEdit_manualEnter.setFocus(1)
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
        
    def nextButtonAction(self):
        num = self.cfg.getDocLineNum(Lang.English) + 1
        if num < len(self.englishDoclist):
            self.cfg.setDocLineNum(num, Lang.English)
        self.plainTextEdit_manualEnter.clear()
        self.plainTextEdit_English.hide()
        self.lineEdit_English_Line_Number.setText(str(self.cfg.getDocLineNum(Lang.English)))
        self.plainTextEdit_CN_line.setPlainText(self.ChineseDoclist[self.cfg.getDocLineNum(Lang.English)])
        self.plainTextEdit_manualEnter.setFocus(1)

    def loadDocToList(self, lang): 
        if os.path.isfile(self.cfg.getDocPath(lang)):
            with open(self.cfg.getDocPath(lang), encoding='utf-8') as f:
                lines = f.readlines()
            lines = [x.strip() for x in lines]
        else:
            lines = ['']
        return lines
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()