# Form implementation generated from reading ui file 'view/ui_design/select_source.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OpenVideo_OpenCam(object):
    def setupUi(self, OpenVideo_OpenCam):
        OpenVideo_OpenCam.setObjectName("OpenVideo_OpenCam")
        OpenVideo_OpenCam.resize(516, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OpenVideo_OpenCam.sizePolicy().hasHeightForWidth())
        OpenVideo_OpenCam.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(OpenVideo_OpenCam)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(0, 164, 239);")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_source_stream_2 = QtWidgets.QPushButton(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.button_source_stream_2.setFont(font)
        self.button_source_stream_2.setObjectName("button_source_stream_2")
        self.gridLayout.addWidget(self.button_source_stream_2, 1, 2, 1, 1)
        self.button_source_stream_6 = QtWidgets.QPushButton(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.button_source_stream_6.setFont(font)
        self.button_source_stream_6.setObjectName("button_source_stream_6")
        self.gridLayout.addWidget(self.button_source_stream_6, 5, 2, 1, 1)
        self.lineEdit_source_2 = QtWidgets.QLineEdit(OpenVideo_OpenCam)
        self.lineEdit_source_2.setObjectName("lineEdit_source_2")
        self.gridLayout.addWidget(self.lineEdit_source_2, 1, 1, 1, 1)
        self.lineEdit_source_6 = QtWidgets.QLineEdit(OpenVideo_OpenCam)
        self.lineEdit_source_6.setObjectName("lineEdit_source_6")
        self.gridLayout.addWidget(self.lineEdit_source_6, 5, 1, 1, 1)
        self.lineEdit_source_4 = QtWidgets.QLineEdit(OpenVideo_OpenCam)
        self.lineEdit_source_4.setObjectName("lineEdit_source_4")
        self.gridLayout.addWidget(self.lineEdit_source_4, 3, 1, 1, 1)
        self.button_source_stream_1 = QtWidgets.QPushButton(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.button_source_stream_1.setFont(font)
        self.button_source_stream_1.setObjectName("button_source_stream_1")
        self.gridLayout.addWidget(self.button_source_stream_1, 0, 2, 1, 1)
        self.lineEdit_source_5 = QtWidgets.QLineEdit(OpenVideo_OpenCam)
        self.lineEdit_source_5.setObjectName("lineEdit_source_5")
        self.gridLayout.addWidget(self.lineEdit_source_5, 4, 1, 1, 1)
        self.lineEdit_source_1 = QtWidgets.QLineEdit(OpenVideo_OpenCam)
        self.lineEdit_source_1.setObjectName("lineEdit_source_1")
        self.gridLayout.addWidget(self.lineEdit_source_1, 0, 1, 1, 1)
        self.lineEdit_source_3 = QtWidgets.QLineEdit(OpenVideo_OpenCam)
        self.lineEdit_source_3.setObjectName("lineEdit_source_3")
        self.gridLayout.addWidget(self.lineEdit_source_3, 2, 1, 1, 1)
        self.button_source_stream_5 = QtWidgets.QPushButton(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.button_source_stream_5.setFont(font)
        self.button_source_stream_5.setObjectName("button_source_stream_5")
        self.gridLayout.addWidget(self.button_source_stream_5, 4, 2, 1, 1)
        self.button_source_stream_4 = QtWidgets.QPushButton(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.button_source_stream_4.setFont(font)
        self.button_source_stream_4.setObjectName("button_source_stream_4")
        self.gridLayout.addWidget(self.button_source_stream_4, 3, 2, 1, 1)
        self.button_source_stream_3 = QtWidgets.QPushButton(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.button_source_stream_3.setFont(font)
        self.button_source_stream_3.setObjectName("button_source_stream_3")
        self.gridLayout.addWidget(self.button_source_stream_3, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(OpenVideo_OpenCam)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(OpenVideo_OpenCam)
        self.buttonBox.accepted.connect(OpenVideo_OpenCam.accept) # type: ignore
        self.buttonBox.rejected.connect(OpenVideo_OpenCam.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(OpenVideo_OpenCam)

    def retranslateUi(self, OpenVideo_OpenCam):
        _translate = QtCore.QCoreApplication.translate
        OpenVideo_OpenCam.setWindowTitle(_translate("OpenVideo_OpenCam", "Select source"))
        self.label_7.setText(_translate("OpenVideo_OpenCam", "Select Source Video"))
        self.radioButton.setText(_translate("OpenVideo_OpenCam", "Open file"))
        self.radioButton_2.setText(_translate("OpenVideo_OpenCam", "Streaming Camera"))
        self.button_source_stream_2.setText(_translate("OpenVideo_OpenCam", "Open"))
        self.button_source_stream_6.setText(_translate("OpenVideo_OpenCam", "Open"))
        self.button_source_stream_1.setText(_translate("OpenVideo_OpenCam", "Open"))
        self.button_source_stream_5.setText(_translate("OpenVideo_OpenCam", "Open"))
        self.button_source_stream_4.setText(_translate("OpenVideo_OpenCam", "Open"))
        self.button_source_stream_3.setText(_translate("OpenVideo_OpenCam", "Open"))
        self.label.setText(_translate("OpenVideo_OpenCam", "Front"))
        self.label_2.setText(_translate("OpenVideo_OpenCam", "Left"))
        self.label_3.setText(_translate("OpenVideo_OpenCam", "Right"))
        self.label_4.setText(_translate("OpenVideo_OpenCam", "Rear"))
        self.label_5.setText(_translate("OpenVideo_OpenCam", "-"))
        self.label_6.setText(_translate("OpenVideo_OpenCam", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenVideo_OpenCam = QtWidgets.QDialog()
    ui = Ui_OpenVideo_OpenCam()
    ui.setupUi(OpenVideo_OpenCam)
    OpenVideo_OpenCam.show()
    sys.exit(app.exec())
