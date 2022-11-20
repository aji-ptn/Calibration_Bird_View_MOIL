from PyQt5 import QtWidgets, QtCore, QtGui


class AdditionalWidget(object):
    def __init__(self, view_controller):
        """
        This class for pitch yaw roll image anypoint
        """
        self.view_controller = view_controller
        self.add_button()
        self.button_addition_mode.hide()
        self.add_frame_pitch_yaw_roll()
        self.frame_pitch_yaw_roll.hide()

        self.button_addition_mode.clicked.connect(self.hide_show_frame_pitch_yaw_roll)

    # def change_properties_anypoint_mode_view(self):
    #     pitch = self.doubleSpinBox.value()
    #     yaw = self.doubleSpinBox_2.value()
    #     roll = self.doubleSpinBox_3.value()
    #     zoom = self.doubleSpinBox_4.value()
    #     return pitch, yaw, roll, zoom

    def hide_show_frame_pitch_yaw_roll(self):
        if self.button_addition_mode.isChecked():
            self.frame_pitch_yaw_roll.show()
        else:
            self.frame_pitch_yaw_roll.hide()

    def add_button(self):
        self.button_addition_mode = QtWidgets.QPushButton(self.view_controller.scrollArea)
# <<<<<<< HEAD:src/views/pyqt5/ui_additional_widget.py
# =======
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.button_addition_mode.setFont(font)
# >>>>>>> origin/UI_pyqt5:src/views/pyqt5/ui_additional_widget.py
        self.button_addition_mode.setGeometry(QtCore.QRect(10, 10, 25, 25))
        self.button_addition_mode.setCheckable(True)
        self.button_addition_mode.setObjectName("button_additional")
        self.button_addition_mode.setText("<>")
# <<<<<<< HEAD:src/views/pyqt5/ui_additional_widget.py
# =======
        _translate = QtCore.QCoreApplication.translate
        self.button_addition_mode.setText(_translate("Pitch_Yaw_Roll", "<>"))
# >>>>>>> origin/UI_pyqt5:src/views/pyqt5/ui_additional_widget.py

    def add_frame_pitch_yaw_roll(self):
        self.frame_pitch_yaw_roll = QtWidgets.QFrame(self.view_controller.scrollArea)
        self.frame_pitch_yaw_roll.setGeometry(QtCore.QRect(40, 10, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.frame_pitch_yaw_roll.setFont(font)
        self.frame_pitch_yaw_roll.setStyleSheet("")
        self.frame_pitch_yaw_roll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_pitch_yaw_roll.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pitch_yaw_roll.setObjectName("frame_pitch_yaw_roll")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_pitch_yaw_roll)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.frame_pitch_yaw_roll)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame_pitch_yaw_roll)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setMinimum(-5000.0)
        self.doubleSpinBox.setProperty("value", 0.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Pitch_Yaw_Roll", "Pitch"))

        self.label_2 = QtWidgets.QLabel(self.frame_pitch_yaw_roll)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.frame_pitch_yaw_roll)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setMinimum(-5000.0)
        self.doubleSpinBox_2.setMaximum(5000.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_2)
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("Pitch_Yaw_Roll", "Yaw"))

        self.label_3 = QtWidgets.QLabel(self.frame_pitch_yaw_roll)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.frame_pitch_yaw_roll)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setMinimum(-5000.0)
        self.doubleSpinBox_3.setMaximum(5000.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_3)
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Pitch_Yaw_Roll", "Roll"))

        self.label_4 = QtWidgets.QLabel(self.frame_pitch_yaw_roll)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.frame_pitch_yaw_roll)
# <<<<<<< HEAD:src/views/pyqt5/ui_additional_widget.py
        self.doubleSpinBox_4.setValue(4)
# =======
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.doubleSpinBox_4.setValue(4)
        self.doubleSpinBox_4.setFont(font)
# >>>>>>> origin/UI_pyqt5:src/views/pyqt5/ui_additional_widget.py
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_4)
        self.verticalLayout.addLayout(self.formLayout)
        _translate = QtCore.QCoreApplication.translate
        self.label_4.setText(_translate("Pitch_Yaw_Roll", "Zoom"))