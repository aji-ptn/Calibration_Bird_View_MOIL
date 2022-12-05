import cv2
from src.view.select_coordinate import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QMessageBox, QLabel
from PyQt5 import QtCore
from .view_additional_function import show_image_to_label, draw_list_point_with_text, \
    init_ori_ratio, calculate_height, draw_point


class SelectCoordinate(QDialog):
    def __init__(self, model, controller):
        super(SelectCoordinate, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.model = model
        self.controller = controller
        self.keys_properties = 0
        self.i = 0
        self.number_of_point = 0
        # self.process_select_point = False

        self.list_point_image = {"front_left": {}, "front_right": {}, "left_front": {}, "left_rear": {},
                                 "right_front": {}, "right_rear": {}, "rear_left": {}, "rear_right": {}}

        self.keys_image = list(self.list_point_image)
        self.list_point_image["front_left"] = []
        self.image = self.model.list_crop_anypoint_image_point[0]
        self.width = 800

        self.point_selection()
        self.show_image()
        self.add_label_zoom()

        self.ui.label_image.mousePressEvent = self.mouse_event
        self.ui.label_image.mouseMoveEvent = self.mouse_moved_event

    def add_label_zoom(self):
        self.add_label = QLabel(self.ui.label_image)
        self.add_label.setGeometry(QtCore.QRect(5, 5, 100, 100))
        self.add_label.setFrameShape(QLabel.Shape.Box)
        self.add_label.setFrameShadow(QLabel.Shadow.Raised)
        self.add_label.hide()

    def mouse_moved_event(self, e):
        pos_x = round(e.x())
        pos_y = round(e.y())
        ratio_x, ratio_y = init_ori_ratio(self.ui.label_image, self.image)
        X = round(pos_x * ratio_x)
        Y = round(pos_y * ratio_y)
        if X > 70 and Y > 70:
            self.add_label.show()
            self.add_label.setGeometry(QtCore.QRect(pos_x + 15, pos_y - 15, 100, 100))
            if self.ui.label_image.height() - pos_y < 200:
                self.add_label.setGeometry(QtCore.QRect(pos_x + 15, pos_y - 150, 100, 100))

            if self.ui.label_image.width() - pos_x < 200:
                self.add_label.setGeometry(QtCore.QRect(pos_x - 150 , pos_y + 15, 100, 100))

            if self.ui.label_image.height() - pos_y < 200 and self.ui.label_image.width() - pos_x < 200:
                self.add_label.setGeometry(QtCore.QRect(pos_x - 150, pos_y - 150, 100, 100))

            if self.ui.label_image.height() - pos_y < 20 and self.ui.label_image.width() - pos_x < 20:
                self.add_label.hide()
            image_ = cv2.circle(self.image.copy(), (X, Y), 2, (200, 5, 200), -1)
            image = image_[Y - 70: (Y - 70) + 140, X - 70:(X - 70) + 140]
            show_image_to_label(self.add_label, image, 140)

        else:
            self.add_label.hide()

    def mouse_event(self, e):
        if e.button() == QtCore.Qt.MouseButton.LeftButton:
            pos_x = round(e.x())
            pos_y = round(e.y())
            if self.number_of_point == 4:
                self.number_of_point = 0

            self.number_of_point += 1
            self.config_coordinate(pos_x, pos_y)

    def config_coordinate(self, pos_x=None, pos_y=None):
        if pos_x is not None and pos_y is not None:
            ratio_x, ratio_y = init_ori_ratio(self.ui.label_image, self.image)
            X = round(pos_x * ratio_x)
            Y = round(pos_y * ratio_y)
            self.point_selection(X, Y)

    def point_selection(self, X=None, Y=None):
        key_image = list(self.model.properties_image)
        if self.number_of_point == 0:
            self.ui.label_point.setText(self.keys_image[self.i] + " select point 1")
        elif self.number_of_point == 1:
            self.list_point_image[self.keys_image[self.i]].append([X, Y])
            self.ui.label_point.setText(self.keys_image[self.i] + " select point 2")
        elif self.number_of_point == 2:
            self.list_point_image[self.keys_image[self.i]].append([X, Y])
            self.ui.label_point.setText(self.keys_image[self.i] + " select point 3")
        elif self.number_of_point == 3:
            self.list_point_image[self.keys_image[self.i]].append([X, Y])
            self.ui.label_point.setText(self.keys_image[self.i] + " select point 4")
        elif self.number_of_point == 4:
            if self.i < 7:
                self.list_point_image[self.keys_image[self.i]].append([X, Y])
                self.ui.label_point.setText(self.keys_image[self.i + 1] + " select point 1")
                self.show_image()
                self.list_point_image[self.keys_image[self.i + 1]] = []
                self.i += 1

                if self.i == 0 or self.i == 1:
                    self.width = 800
                    self.image = self.model.list_crop_anypoint_image_point[0]
                    self.keys_properties = 0

                elif self.i == 2 or self.i == 3:
                    self.width = 400
                    self.image = self.model.list_crop_anypoint_image_point[1]
                    self.keys_properties = 1

                elif self.i == 4 or self.i == 5:
                    self.width = 400
                    self.image = self.model.list_crop_anypoint_image_point[2]
                    self.keys_properties = 2

                elif self.i == 6 or self.i == 7:
                    self.width = 800
                    self.image = self.model.list_crop_anypoint_image_point[3]
                    self.keys_properties = 3

                else:
                    self.width = None
                    self.image = None

            else:
                self.list_point_image[self.keys_image[self.i]].append([X, Y])
                QMessageBox.information(None, "Info", "Finish !!!")
                self.model.properties_image[key_image[self.keys_properties]][self.keys_image[self.i]] = \
                    self.list_point_image[self.keys_image[self.i]]
                self.show_image()
                self.controller.control_perspective.fill_data_src(self.model.properties_image)
                # self.model.overlap_image = self.controller.merge_image_by_clicked()
                self.close()

        self.model.properties_image[key_image[self.keys_properties]][self.keys_image[self.i]] = \
            self.list_point_image[self.keys_image[self.i]]
        self.show_image()

    def show_image(self):
        image = draw_list_point_with_text(self.image, self.list_point_image[self.keys_image[self.i]], 5)
        show_image_to_label(self.ui.label_image, image, self.width)
        height = calculate_height(self.image, self.width)
        self.setMaximumWidth(self.width)
        self.setMaximumHeight(height)
