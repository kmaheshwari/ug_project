# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(641, 523)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cipher = QtWidgets.QLineEdit(Form)
        self.cipher.setObjectName("cipher")
        self.gridLayout.addWidget(self.cipher, 1, 0, 1, 2)
        self.translate = QtWidgets.QPushButton(Form)
        self.translate.setObjectName("translate")
        self.gridLayout.addWidget(self.translate, 2, 0, 1, 1)
        self.reset = QtWidgets.QPushButton(Form)
        self.reset.setObjectName("reset")
        self.gridLayout.addWidget(self.reset, 2, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.result = QtWidgets.QTextEdit(Form)
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 5, 0, 1, 2)
        self.result.setReadOnly(True)

        self.retranslateUi(Form)
        self.reset.clicked.connect(self.cipher.clear)
        self.reset.clicked.connect(self.result.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DashBoard"))
        self.label.setText(_translate("Form", "Cipher text"))
        self.cipher.setPlaceholderText(_translate("Form", "Enter the cipher text here"))
        self.translate.setText(_translate("Form", "Translate"))
        self.reset.setText(_translate("Form", "Reset"))
        self.label_2.setText(_translate("Form", "Output"))

