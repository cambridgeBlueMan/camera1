# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zoomCode.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1170, 624)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 40, 231, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.leftIndent = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.leftIndent.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.leftIndent.setObjectName("leftIndent")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leftIndent)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.rightIndent = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.rightIndent.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.rightIndent.setObjectName("rightIndent")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rightIndent)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.topIndent = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.topIndent.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.topIndent.setObjectName("topIndent")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.topIndent)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.bottomIndent = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bottomIndent.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.bottomIndent.setObjectName("bottomIndent")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bottomIndent)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 220, 551, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.left.setChecked(True)
        self.left.setObjectName("left")
        self.horizontalLayout.addWidget(self.left)
        self.right = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.right.setObjectName("right")
        self.horizontalLayout.addWidget(self.right)
        self.leftPreview = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.leftPreview.setObjectName("leftPreview")
        self.horizontalLayout.addWidget(self.leftPreview)
        self.rightPreview = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.rightPreview.setObjectName("rightPreview")
        self.horizontalLayout.addWidget(self.rightPreview)
        self.lrShow = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.lrShow.setObjectName("lrShow")
        self.horizontalLayout.addWidget(self.lrShow)
        self.lrRecord = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.lrRecord.setObjectName("lrRecord")
        self.horizontalLayout.addWidget(self.lrRecord)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 310, 576, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.top = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.top.setChecked(True)
        self.top.setObjectName("top")
        self.horizontalLayout_3.addWidget(self.top)
        self.bottom = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.bottom.setObjectName("bottom")
        self.horizontalLayout_3.addWidget(self.bottom)
        self.topPreview = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.topPreview.setObjectName("topPreview")
        self.horizontalLayout_3.addWidget(self.topPreview)
        self.bottomPreview = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.bottomPreview.setObjectName("bottomPreview")
        self.horizontalLayout_3.addWidget(self.bottomPreview)
        self.tbShow = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.tbShow.setObjectName("tbShow")
        self.horizontalLayout_3.addWidget(self.tbShow)
        self.tbRecord = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.tbRecord.setObjectName("tbRecord")
        self.horizontalLayout_3.addWidget(self.tbRecord)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(70, 400, 548, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setEnabled(False)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_4.setEnabled(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.quit = QtWidgets.QPushButton(Form)
        self.quit.setGeometry(QtCore.QRect(650, 570, 99, 30))
        self.quit.setObjectName("quit")
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(330, 40, 191, 171))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.durationLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.durationLabel.setObjectName("durationLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.durationLabel)
        self.duration = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.duration.setObjectName("duration")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.duration)
        self.fullSensor = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.fullSensor.setObjectName("fullSensor")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fullSensor)
        self.isGetFileName = QtWidgets.QCheckBox(Form)
        self.isGetFileName.setGeometry(QtCore.QRect(550, 50, 181, 27))
        self.isGetFileName.setObjectName("isGetFileName")
        self.captureStill = QtWidgets.QPushButton(Form)
        self.captureStill.setGeometry(QtCore.QRect(830, 70, 99, 30))
        self.captureStill.setObjectName("captureStill")

        self.retranslateUi(Form)
        self.rightPreview.clicked.connect(Form.setAndShowPreview)
        self.leftPreview.clicked.connect(Form.setAndShowPreview)
        self.topPreview.clicked.connect(Form.setAndShowPreview)
        self.bottomPreview.clicked.connect(Form.setAndShowPreview)
        self.lrShow.clicked.connect(Form.doZoom)
        self.lrRecord.clicked.connect(Form.doZoomWithRecord)
        self.tbShow.clicked.connect(Form.doZoom)
        self.tbRecord.clicked.connect(Form.doZoomWithRecord)
        self.fullSensor.clicked.connect(Form.setAndShowPreview)
        self.quit.clicked.connect(Form.doQuit)
        self.duration.textChanged['QString'].connect(Form.getDuration)
        self.captureStill.clicked.connect(Form.doCaptureStill)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Left Indent"))
        self.leftIndent.setText(_translate("Form", "0"))
        self.label_2.setText(_translate("Form", "Right Indent"))
        self.rightIndent.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "Top Indent"))
        self.topIndent.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "Bottom Indent"))
        self.bottomIndent.setText(_translate("Form", "0"))
        self.label_5.setText(_translate("Form", "Horizontal Pan"))
        self.left.setText(_translate("Form", "Left"))
        self.right.setText(_translate("Form", "Right"))
        self.leftPreview.setText(_translate("Form", "Left Preview"))
        self.rightPreview.setText(_translate("Form", "Right Preview"))
        self.lrShow.setText(_translate("Form", "Show"))
        self.lrRecord.setText(_translate("Form", "Record"))
        self.label_6.setText(_translate("Form", "Vertical Pan"))
        self.top.setText(_translate("Form", "Top"))
        self.bottom.setText(_translate("Form", "Bottom"))
        self.topPreview.setText(_translate("Form", "Top Preview"))
        self.bottomPreview.setText(_translate("Form", "Bottom Preview"))
        self.tbShow.setText(_translate("Form", "Show"))
        self.tbRecord.setText(_translate("Form", "Record"))
        self.label_7.setText(_translate("Form", "Diagonal with Zoom"))
        self.radioButton_3.setText(_translate("Form", "Left"))
        self.radioButton_4.setText(_translate("Form", "Right"))
        self.pushButton_5.setText(_translate("Form", "Left Preview"))
        self.pushButton_6.setText(_translate("Form", "Right Preview"))
        self.pushButton_7.setText(_translate("Form", "Show"))
        self.pushButton_8.setText(_translate("Form", "Record"))
        self.quit.setText(_translate("Form", "Quit"))
        self.durationLabel.setText(_translate("Form", "Duration"))
        self.duration.setText(_translate("Form", "30"))
        self.fullSensor.setText(_translate("Form", "Full Sensor"))
        self.isGetFileName.setText(_translate("Form", "Prompt for File Name"))
        self.captureStill.setText(_translate("Form", "Snap!"))

