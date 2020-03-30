# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import string

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 300)
        MainWindow.setMinimumSize(QSize(600, 300))
        MainWindow.setMaximumSize(QSize(600, 300))

        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")

        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)

        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)

        self.frame = QFrame(self.centralWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(110, 100, 351, 151))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.output1 = QTextEdit(self.frame)
        self.output1.setObjectName(u"output1")
        self.output1.setGeometry(QRect(120, 0, 221, 41))
        self.output1.setFont(font2)
        self.output1.setReadOnly(True)
        self.output1.setText("17")

        self.output2 = QTextEdit(self.frame)
        self.output2.setObjectName(u"output2")
        self.output2.setGeometry(QRect(120, 50, 221, 41))
        self.output2.setFont(font2)
        self.output2.setReadOnly(True)
        self.output2.setText("6")

        self.output3 = QTextEdit(self.frame)
        self.output3.setObjectName(u"output3")
        self.output3.setGeometry(QRect(120, 100, 221, 41))
        self.output3.setFont(font2)
        self.output3.setReadOnly(True)
        self.output3.setText("5")

        self.label_1 = QLabel(self.centralWidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(50, 30, 81, 31))
        self.label_1.setFont(font)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 91, 21))
        self.label_2.setFont(font1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 60, 91, 21))
        self.label_3.setFont(font1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 110, 91, 21))
        self.label_4.setFont(font1)

        self.input = QTextEdit(self.centralWidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(150, 30, 351, 41))
        self.input.setFont(font1)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.input.textChanged.connect(self.characterCounting)
        self.input.textChanged.connect(self.numberCounting)
        self.input.textChanged.connect(self.symbolCounting)

        QMetaObject.connectSlotsByName(MainWindow)


    def characterCounting(self):
        characterCount = 0
        string = self.input.toPlainText()
        for c in string:
            if c.isalpha():
                characterCount += 1
        self.output1.setText(str(characterCount))

    def numberCounting(self):
        numberCount = 0
        string = self.input.toPlainText()
        for c in string:
            if c.isdigit():
                numberCount += 1
        self.output2.setText(str(numberCount))

    def symbolCounting(self):
        string = self.input.toPlainText()
        symbolCount = len(string)
        for c in string:
            if c.isdigit():
                symbolCount -= 1
            if c.isalpha():
                symbolCount -= 1
        self.output3.setText(str(symbolCount))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(u"字符计数")
        self.input.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                            "p, li { white-space: pre-wrap; }\n"
                            "</style></head><body style=\" font-family:'Arial'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:14pt;\">Beijing.2008.(29th Olympics)</span></p></body></html>")
        self.output1.setPlaceholderText("")
        self.output2.setPlaceholderText("")
        self.output3.setPlaceholderText("")
        self.label_1.setText(u"输入")
        self.label_2.setText(u"字母个数")
        self.label_3.setText(u"数字个数")
        self.label_4.setText(u"其他字符")
