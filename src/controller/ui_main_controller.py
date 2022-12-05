import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
from src.view.main_ui_2 import Ui_calibration_birds_view
from .set_icon_widget import SetIconUserInterface
from .view_additional_function import show_image_to_label, draw_point
from .ui_video_controller import UiVideoController
from .ui_image_controller import UiImageController
from .ui_control_widget import ControlWidget
from .calib_properties import CalibProperties
from .ui_show_result import UiShowResult
from .ui_additional_widget import AdditionalWidget
from .ui_show_fov import ShowRangeFOV
from .ui_show_selected_point import SelectCoordinate


class Controller(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.main_ui = Ui_calibration_birds_view()
        self.main_ui.setupUi(self)

        self.additional_mode_view = AdditionalWidget(self.main_ui)

        self.set_icon = SetIconUserInterface(self.main_ui)
        self.showMaximized()

        self.controller = controller
        self.model = self.controller.model

        self.ui_video_controller = UiVideoController(self)
        self.ui_image_controller = UiImageController(self)
        self.control_widget = ControlWidget(self)
        self.calib_properties = CalibProperties(self)
        self.show_to_window = UiShowResult(self)

        self.change_mode_camera_placement()
        self.width_alignment_1 = 360
        self.width_alignment_2 = 360
        self.hide()

        self.connect_event_button()

    def connect_event_button(self):
        self.main_ui.toolbox_configuration.currentChanged.connect(self.toolbox_activation)
        self.main_ui.radio_button_select_corner.clicked.connect(self.change_mode_camera_placement)
        self.main_ui.radio_button_select_center.clicked.connect(self.change_mode_camera_placement)

        self.main_ui.horizontalSlider.valueChanged.connect(self.change_zoom_slider)
        self.main_ui.button_minus_zoom_anypoint.pressed.connect(lambda: self.onclick_zoom("minus"))
        self.main_ui.button_plus_zoom_anypoint.pressed.connect(lambda: self.onclick_zoom("plus"))

        self.main_ui.radioButton_to_front_image_2.clicked.connect(self.radio_button_event_alignment_image_2)
        self.main_ui.radioButton_to_rear_image_2.clicked.connect(self.radio_button_event_alignment_image_2)
        self.main_ui.radioButton_to_front_image_3.clicked.connect(self.radio_button_event_alignment_image_3)
        self.main_ui.radioButton_to_rear_image_3.clicked.connect(self.radio_button_event_alignment_image_3)
        self.main_ui.radioButton_to_left_image_4.clicked.connect(self.radio_button_event_alignment_image_4)
        self.main_ui.radioButton_to_right_image_4.clicked.connect(self.radio_button_event_alignment_image_4)

        self.main_ui.label_original_alligment_1.wheelEvent = self.mouse_wheelEvent_alignment_1
        self.main_ui.label_original_alligment_2.wheelEvent = self.mouse_wheelEvent_alignment_2

        self.additional_mode_view.doubleSpinBox.valueChanged.connect(self.change_anypoint_mode_view)
        self.additional_mode_view.doubleSpinBox_2.valueChanged.connect(self.change_anypoint_mode_view)
        self.additional_mode_view.doubleSpinBox_3.valueChanged.connect(self.change_anypoint_mode_view)
        self.additional_mode_view.doubleSpinBox_4.valueChanged.connect(self.change_anypoint_mode_view)

        self.main_ui.radio_button_blend_horizontal.clicked.connect(self.change_gradient_mode)
        self.main_ui.radio_button_blend_vertical.clicked.connect(self.change_gradient_mode)
        self.main_ui.radio_button_blend_diagonal.clicked.connect(self.change_gradient_mode)
        self.main_ui.radio_button_overlap.clicked.connect(self.change_gradient_mode)

        self.main_ui.show_fov_image_1.clicked.connect(self.show_fov_window)
        self.main_ui.show_fov_image_2.clicked.connect(self.show_fov_window)
        self.main_ui.show_fov_image_3.clicked.connect(self.show_fov_window)
        self.main_ui.show_fov_image_4.clicked.connect(self.show_fov_window)
        self.main_ui.show_fov_image_5.clicked.connect(self.show_fov_window)
        self.main_ui.show_fov_image_6.clicked.connect(self.show_fov_window)

        self.main_ui.checkBox_show_fov_line.stateChanged.connect(self.show_fov_line)
        self.main_ui.checkBox_merge_by_point.stateChanged.connect(self.show_selected_point_for_merge)

    def show_selected_point_for_merge(self):
        if self.main_ui.checkBox_merge_by_point.isChecked():
            if self.model.list_original_image:
                self.controller.mode_calib = "Point"
                self.controller.fill_image_crop_anypoint_point()
                select_coordinate = SelectCoordinate(self.model, self.controller)
                select_coordinate.exec()
                self.show_to_window.show_overlay_and_birds_view()
        else:
            self.controller.mode_calib = "Normal"

    def show_fov_line(self):
        if self.main_ui.checkBox_show_fov_line.isChecked():
            self.controller.show_fov_image(True)
        else:
            self.controller.show_fov_image(False)
        # for i in range(self.model.total_camera_used):
        #     self.controller.process_generating_reverse_image(i)
        # self.controller.process_generating_reverse_image(0)
        self.show_to_window.show_overlay_and_birds_view()

    def show_fov_window(self):
        activated = self.main_ui.toolbox_configuration.currentIndex()
        show_fov = ShowRangeFOV(activated, self.model, self.controller, self.show_to_window)
        show_fov.exec()

    def change_gradient_mode(self):
        if self.main_ui.radio_button_blend_horizontal.isChecked():
            self.controller.change_gradient_mode("H")
        elif self.main_ui.radio_button_blend_vertical.isChecked():
            self.controller.change_gradient_mode("V")
        elif self.main_ui.radio_button_blend_diagonal.isChecked():
            self.controller.change_gradient_mode("D")
        elif self.main_ui.radio_button_overlap.isChecked():
            self.controller.change_gradient_mode("O")
        if self.model.list_original_image:
            self.show_to_window.show_overlay_and_birds_view()

    def change_anypoint_mode_view(self):
        pitch = self.additional_mode_view.doubleSpinBox.value()
        yaw = self.additional_mode_view.doubleSpinBox_2.value()
        roll = self.additional_mode_view.doubleSpinBox_3.value()
        zoom = self.additional_mode_view.doubleSpinBox_4.value()
        self.controller.generate_maps_anypoint_mode_view(pitch, yaw, roll, zoom)
        self.show_to_window.showing_video_result()

    def get_offset_icy_image_2(self):
        if self.model.list_icy[1] is not None and self.model.list_icy[0] is not None:
            icy_image_1 = self.model.list_icy[1]
            icy_image_2 = self.model.list_icy[0]
            # if self.main_ui.radioButton_to_rear_image_2.isChecked():
            #     if self.model.list_icy[3] is not None:
            #         icy_image_2 = self.model.list_icy[3]

            offset = abs(icy_image_1 - icy_image_2)
            return offset

    def get_offset_icy_image_3(self):
        if self.model.list_icy[1] is not None and self.model.list_icy[0] is not None:
            icy_image_2 = self.model.list_icy[1]
            icy_image_1 = self.model.list_icy[0]

            offset = abs(icy_image_1 - icy_image_2)
            return offset

    def get_offset_icy_image_4(self):
        if self.model.list_icy[3] is not None and self.model.list_icy[1] is not None:
            icy_image_2 = self.model.list_icy[3]
            icy_image_1 = self.model.list_icy[1]
            # if self.main_ui.radioButton_to_rear_image_2.isChecked():
            #     if self.model.list_icy[2] is not None:
            #         icy_image_1 = self.model.list_icy[2]

            offset = abs(icy_image_1 - icy_image_2)
            return offset

    def change_zoom_slider(self, value):
        self.main_ui.horizontalSlider.setMaximum(30)
        self.controller.change_slider_zoom(value)
        self.show_zoom_to_ui()

    def onclick_zoom(self, value):
        if value == "plus":
            self.controller.change_zoom_plus()
        elif value == "minus":
            self.controller.change_zoom_minus()
        self.main_ui.horizontalSlider.setValue(self.model.zoom_control)
        self.show_zoom_to_ui()

    def show_zoom_to_ui(self):
        self.main_ui.label_zoom_anypoint_all.setText(str(self.model.zoom_control))

    def change_mode_camera_placement(self):
        camera_placement = "corner" if self.main_ui.radio_button_select_corner.isChecked() else "center"
        self.model.camera_placement = camera_placement
        if self.model.list_original_image:
            self.show_to_window.show_overlay_and_birds_view()

    def mouse_wheelEvent_alignment_1(self, e):
        """
        Resize image using mouse wheel event.
        """
        if self.model.list_original_image[0] is not None:
            modifiers = QApplication.keyboardModifiers()
            if modifiers == Qt.ControlModifier:
                wheel_counter = e.angleDelta()
                if wheel_counter.y() / 120 == -1:
                    if self.width_alignment_1 <= 360:
                        pass
                    else:
                        self.width_alignment_1 -= 40

                elif wheel_counter.y() / 120 == 1:
                    if self.width_alignment_1 >= 2000:
                        pass
                    else:
                        self.width_alignment_1 += 40

        self.toolbox_activation()

    def mouse_wheelEvent_alignment_2(self, e):
        """
        Resize image using mouse wheel event.
        """
        if self.model.list_original_image[0] is not None:
            modifiers = QApplication.keyboardModifiers()
            if modifiers == Qt.ControlModifier:
                wheel_counter = e.angleDelta()
                if wheel_counter.y() / 120 == -1:
                    if self.width_alignment_2 <= 360:
                        pass
                    else:
                        self.width_alignment_2 -= 40

                elif wheel_counter.y() / 120 == 1:
                    if self.width_alignment_2 >= 2000:
                        pass
                    else:
                        self.width_alignment_2 += 40

        self.toolbox_activation()

    def toolbox_activation(self):
        activated = self.main_ui.toolbox_configuration.currentIndex()
        self.set_icon.icon_toolbox(activated)
        self.main_ui.verticalFrame_alignment_2.show()
        self.main_ui.scrollArea_9.setMinimumWidth(400)
        self.main_ui.scrollArea_9.setMinimumHeight(300)
        self.main_ui.frame_crop_alligment.show()

        if self.model.list_original_image:
            if activated == 0:
                self.main_ui.scrollArea_9.setMinimumWidth(796)
                self.main_ui.label_result_alligment_1.setMinimumWidth(776)
                self.main_ui.scrollArea_9.setMinimumHeight(580)
                self.main_ui.verticalFrame_alignment_2.hide()
                self.main_ui.frame_crop_alligment.hide()
                self.show_toolbox_image_1()

            elif activated == 1:
                self.radio_button_event_alignment_image_2()

            elif activated == 2:
                self.radio_button_event_alignment_image_3()

            elif activated == 3:
                self.radio_button_event_alignment_image_4()

    def show_toolbox_image_1(self):
        show_image_to_label(self.main_ui.label_original_alligment_1, self.model.list_anypoint_image[0], 760)
        self.main_ui.label_result_alligment_1.setText("Please Modify as god as you can. \nThis image "
                                                      "will be reference for other image")
        self.main_ui.spinBox_icx_alligment_1.setValue(self.main_ui.val_icx_image_1.value())
        self.main_ui.spinBox_icy_alligment_1.setValue(self.main_ui.val_icy_image_1.value())

    def radio_button_event_alignment_image_2(self):
        if self.main_ui.button_auto_level.isChecked():
            icy = self.main_ui.val_icy_image_1.value()
            self.main_ui.val_icy_image_2.setValue(icy)

        self.main_ui.label_original_alligment_1.mousePressEvent = self.calib_properties.config_image_2.mouse_event_alignment_label_1
        self.main_ui.label_original_alligment_2.mousePressEvent = self.calib_properties.config_image_1.mouse_event_alignment_label_2

        show_image_to_label(self.main_ui.label_original_alligment_1,
                            self.draw_point_on_the_original_image_alignment_1(self.model.list_original_image[1].copy()),
                            self.width_alignment_1)
        # show_image_to_label(self.main_ui.label_result_alligment_1,
        #                     self.model.list_reverse_alignment[0], 360, plusIcon=True)

        # crop image 1
        # crop_image_1 = self.cropImage(self.model.list_reverse_alignment[0])
        # show_image_to_label(self.main_ui.label_wind_image_1_crop, crop_image_1, 240, plusIcon=True)

        # crop image 2
        show_image_to_label(self.main_ui.label_original_alligment_2,
                            self.draw_point_on_the_original_image_alignment_2(self.model.list_original_image[0].copy()),
                            self.width_alignment_2)
        # show_image_to_label(self.main_ui.label_result_alligment_2,
        #                     self.model.list_reverse_alignment[1], 360, plusIcon=True)
        # crop_image_2 = self.cropImage(self.model.list_reverse_alignment[1])

        # if image left compare to rear
        if self.main_ui.radioButton_to_rear_image_2.isChecked():
            self.main_ui.label_original_alligment_2.mousePressEvent = self.calib_properties.config_image_4.mouse_event_alignment_label_2

            show_image_to_label(self.main_ui.label_original_alligment_2,
                                self.draw_point_on_the_original_image_alignment_2(
                                    self.model.list_original_image[3].copy()),
                                self.width_alignment_2)
            # show_image_to_label(self.main_ui.label_result_alligment_2,
            #                     self.model.list_reverse_alignment[1], 360, plusIcon=True)
            #
            # crop_image_2 = self.cropImage(self.model.list_reverse_alignment[1])

        if self.model.list_icx[0] is not None and self.model.list_icx[1] is not None:
            self.main_ui.spinBox_icx_alligment_1.setValue(self.model.list_icx[0])
            self.main_ui.spinBox_icy_alligment_1.setValue(self.model.list_icy[0])

            self.main_ui.spinBox_icx_alligment_2.setValue(self.model.list_icx[1])
            self.main_ui.spinBox_icy_alligment_2.setValue(self.model.list_icy[1])

        # show_image_to_label(self.main_ui.label_wind_image_2_crop, crop_image_2, 240, plusIcon=True)
        # overlay_crop = self.overlapping_transparency(crop_image_1, crop_image_2)
        # show_image_to_label(self.main_ui.label_wind_image_overlapping_crop, overlay_crop, 240)

    def radio_button_event_alignment_image_3(self):
        if self.main_ui.button_auto_level.isChecked():
            icy = self.main_ui.val_icy_image_1.value()
            self.main_ui.val_icy_image_3.setValue(icy)
        self.main_ui.label_original_alligment_1.mousePressEvent = self.calib_properties.config_image_1.mouse_event_alignment_label_1
        self.main_ui.label_original_alligment_2.mousePressEvent = self.calib_properties.config_image_3.mouse_event_alignment_label_2

        show_image_to_label(self.main_ui.label_original_alligment_1,
                            self.draw_point_on_the_original_image_alignment_1(self.model.list_original_image[0].copy()),
                            self.width_alignment_1)
        # show_image_to_label(self.main_ui.label_result_alligment_1, self.model.list_reverse_alignment[0], 360,
        #                     plusIcon=True)
        # crop image 1
        # crop_image_1 = self.cropImage(self.model.list_reverse_alignment[0])
        # show_image_to_label(self.main_ui.label_wind_image_1_crop, crop_image_1, 240, plusIcon=True)

        show_image_to_label(self.main_ui.label_original_alligment_2,
                            self.draw_point_on_the_original_image_alignment_2(self.model.list_original_image[2].copy()),
                            self.width_alignment_2)
        # show_image_to_label(self.main_ui.label_result_alligment_2, self.model.list_reverse_alignment[1], 360,
        #                     plusIcon=True)
        # crop image 2
        # crop_image_2 = self.cropImage(self.model.list_reverse_alignment[1])

        # show_image_to_label(self.main_ui.label_wind_image_2_crop, crop_image_2, 240, plusIcon=True)

        if self.main_ui.radioButton_to_rear_image_3.isChecked():
            self.main_ui.label_original_alligment_1.mousePressEvent = self.calib_properties.config_image_4.mouse_event_alignment_label_1

            show_image_to_label(self.main_ui.label_original_alligment_1,
                                self.draw_point_on_the_original_image_alignment_1(
                                    self.model.list_original_image[3].copy()),
                                self.width_alignment_1)
            # show_image_to_label(self.main_ui.label_result_alligment_1, self.model.list_reverse_alignment[0], 360,
            #                     plusIcon=True)
            # crop image 2
            # crop_image_1 = self.cropImage(self.model.list_reverse_alignment[0])

        if self.model.list_icx[0] is not None and self.model.list_icx[1] is not None:
            self.main_ui.spinBox_icx_alligment_1.setValue(self.model.list_icx[0])
            self.main_ui.spinBox_icy_alligment_1.setValue(self.model.list_icy[0])

            self.main_ui.spinBox_icx_alligment_2.setValue(self.model.list_icx[1])
            self.main_ui.spinBox_icy_alligment_2.setValue(self.model.list_icy[1])
        # show_image_to_label(self.main_ui.label_wind_image_1_crop, crop_image_1, 240, plusIcon=True)
        # overlay_crop = self.overlapping_transparency(crop_image_1, crop_image_2)
        # show_image_to_label(self.main_ui.label_wind_image_overlapping_crop, overlay_crop, 240)

    def radio_button_event_alignment_image_4(self):
        if self.main_ui.button_auto_level.isChecked():
            icy = self.main_ui.val_icy_image_1.value()
            self.main_ui.val_icy_image_4.setValue(icy)
        self.main_ui.label_original_alligment_1.mousePressEvent = self.calib_properties.config_image_4.mouse_event_alignment_label_1
        self.main_ui.label_original_alligment_2.mousePressEvent = self.calib_properties.config_image_2.mouse_event_alignment_label_2

        show_image_to_label(self.main_ui.label_original_alligment_1,
                            self.draw_point_on_the_original_image_alignment_1(self.model.list_original_image[3].copy()),
                            self.width_alignment_1)
        # show_image_to_label(self.main_ui.label_result_alligment_1, self.model.list_reverse_alignment[0], 360,
        #                     plusIcon=True)
        # crop image 1
        # crop_image_1 = self.cropImage(self.model.list_reverse_alignment[0])
        # show_image_to_label(self.main_ui.label_wind_image_1_crop, crop_image_1, 240, plusIcon=True)

        show_image_to_label(self.main_ui.label_original_alligment_2,
                            self.draw_point_on_the_original_image_alignment_2(self.model.list_original_image[1].copy()),
                            self.width_alignment_2)
        # show_image_to_label(self.main_ui.label_result_alligment_2, self.model.list_reverse_alignment[1], 360,
        #                     plusIcon=True)
        # crop image 2
        # crop_image_2 = self.cropImage(self.model.list_reverse_alignment[1])

        if self.main_ui.radioButton_to_right_image_4.isChecked():
            self.main_ui.label_original_alligment_2.mousePressEvent = self.calib_properties.config_image_3.mouse_event_alignment_label_2

            show_image_to_label(self.main_ui.label_original_alligment_2,
                                self.draw_point_on_the_original_image_alignment_2(
                                    self.model.list_original_image[2].copy()),
                                self.width_alignment_2)
            # show_image_to_label(self.main_ui.label_result_alligment_2, self.model.list_reverse_alignment[1], 360,
            #                     plusIcon=True)
            # crop image 2
            # crop_image_2 = self.cropImage(self.model.list_reverse_alignment[1])

        if self.model.list_icx[0] is not None and self.model.list_icx[1] is not None:
            self.main_ui.spinBox_icx_alligment_1.setValue(self.model.list_icx[0])
            self.main_ui.spinBox_icy_alligment_1.setValue(self.model.list_icy[0])

            self.main_ui.spinBox_icx_alligment_2.setValue(self.model.list_icx[1])
            self.main_ui.spinBox_icy_alligment_2.setValue(self.model.list_icy[1])

        # show_image_to_label(self.main_ui.label_wind_image_2_crop, crop_image_2, 240, plusIcon=True)
        # overlay_crop = self.overlapping_transparency(crop_image_1, crop_image_2)
        # show_image_to_label(self.main_ui.label_wind_image_overlapping_crop, overlay_crop, 240)

    def draw_point_on_the_original_image_alignment_1(self, image):
        icx = self.model.list_icx[0]
        icy = self.model.list_icy[0]
        return draw_point(image, (icx, icy), 2)

    def draw_point_on_the_original_image_alignment_2(self, image):
        icx = self.model.list_icx[1]
        icy = self.model.list_icy[1]
        return draw_point(image, (icx, icy), 2)

    @staticmethod
    def overlapping_transparency(image_1, image_2):
        # print("overlapping transparency")
        # return cv2.addWeighted(image_1, 0.5, image_2, 0.5, 0)
        return cv2.subtract(image_1, image_2)

    @classmethod
    def cropImage(cls, image):
        return image[int(image.shape[0] / 2 - 200):int(image.shape[0] / 2 + 200),
               int(image.shape[1] / 2 - 200):int(image.shape[1] / 2 + 200)]

    def hide(self):
        self.main_ui.line_5.hide()
        self.main_ui.label_3.hide()
        self.main_ui.frame_4.hide()
        self.main_ui.line_2.hide()
        self.main_ui.label_5.hide()
        self.main_ui.button_manual.hide()
        self.main_ui.button_auto_level.hide()
        self.main_ui.line_3.hide()
        self.main_ui.checkBox_show_fov_line.hide()
        self.main_ui.checkBox_merge_by_point.hide()
        self.main_ui.label_9.hide()
        self.main_ui.horizontalSlider.hide()
        self.main_ui.button_minus_zoom_anypoint.hide()
        self.main_ui.button_plus_zoom_anypoint.hide()
        self.main_ui.label_zoom_anypoint_all.hide()
        self.main_ui.button_update_properties.hide()
        self.main_ui.button_change_mode_view.hide()
