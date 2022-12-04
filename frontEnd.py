# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from thuVien import lists_speak
import threading

class Ui_siri(object):
    def setupUi(self, siri):
        siri.setObjectName("siri")
        siri.setWindowModality(QtCore.Qt.WindowModal)
        siri.resize(935, 744)
        
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        siri.setFont(font)
        siri.setWindowOpacity(1.0)
        
        self.btn_reset = QtWidgets.QPushButton(siri)
        self.btn_reset.setGeometry(QtCore.QRect(10, 700, 911, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.btn_reset.setFont(font)
        self.btn_reset.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_reset.setCheckable(False)
        self.btn_reset.setObjectName("btn_reset")
        
        self.img = QtWidgets.QLabel(siri)
        self.img.setGeometry(QtCore.QRect(0, 0, 431, 691))
        self.img.setText("")
        self.img.setTextFormat(QtCore.Qt.AutoText)
        self.img.setPixmap(QtGui.QPixmap("anh/top-tro-ly-ao.jpg"))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")
        self.label_2 = QtWidgets.QLabel(siri)
        self.label_2.setGeometry(QtCore.QRect(444, 5, 491, 691))
        self.label_2.setObjectName("label_2")
        
        self.textEdit = QtWidgets.QTextEdit(siri)
        self.textEdit.setGeometry(QtCore.QRect(440, 0, 491, 691))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.stack = QtWidgets.QPushButton(siri)
        self.stack.setGeometry(QtCore.QRect(140, 560, 151, 41))
        self.stack.setObjectName("stack")

        self.retranslateUi(siri)
        QtCore.QMetaObject.connectSlotsByName(siri)
        
    def retranslateUi(self, siri):
        _translate = QtCore.QCoreApplication.translate
        siri.setWindowTitle(_translate("siri", "Trợ lý ảo Siri"))
        self.btn_reset.setText(_translate("siri", "Reset"))
        self.label_2.setText(_translate("siri", "TextLabel"))
        self.stack.setText(_translate("siri", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    siri = QtWidgets.QMainWindow()#QWidget()
    ui = Ui_siri()
    ui.setupUi(siri)
    siri.show()
    sys.exit(app.exec_())