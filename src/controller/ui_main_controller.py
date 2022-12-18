import cv2
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt
from .set_icon_widget import SetIconUserInterface
from .view_additional_function import show_image_to_label, draw_point
from .ui_video_controller import UiVideoController
from .ui_image_controller import UiImageController
from .ui_control_widget import ControlWidget
from .calib_properties import CalibProperties
from .ui_show_result import UiShowResult


class Controller(QMainWindow):
    def __init__(self, model, ui):
        """
        Main controller contain logic and connected to main ui

        Args:
            controller:
            ui:
        """
        super().__init__()
        self.main_ui = ui
        self.main_ui.setupUi(self)

        self.set_icon = SetIconUserInterface(self.main_ui)
        self.showMaximized()

        self.model = model
        # self.model = self.controller.model

        self.ui_video_controller = UiVideoController(self)
        self.ui_image_controller = UiImageController(self)
        self.control_widget = ControlWidget(self)
        self.calib_properties = CalibProperties(self)
        self.show_to_window = UiShowResult(self)
        self.main_ui.radio_button_blend_diagonal.hide()
        self.main_ui.radio_button_blend_vertical.hide()

        self.width_alignment_1 = 360
        self.width_alignment_2 = 360
        self.hide()

        self.connect_event_button()

    def connect_event_button(self):
        self.main_ui.radio_button_blend_horizontal.clicked.connect(self.change_gradient_mode)
        self.main_ui.radio_button_blend_vertical.clicked.connect(self.change_gradient_mode)
        self.main_ui.radio_button_blend_diagonal.clicked.connect(self.change_gradient_mode)
        self.main_ui.radio_button_overlap.clicked.connect(self.change_gradient_mode)

    def change_gradient_mode(self):
        if self.main_ui.radio_button_blend_horizontal.isChecked():
            self.model.change_gradient_mode_("H")
        elif self.main_ui.radio_button_blend_vertical.isChecked():
            self.model.change_gradient_mode_("V")
        elif self.main_ui.radio_button_blend_diagonal.isChecked():
            self.model.change_gradient_mode_("D")
        elif self.main_ui.radio_button_overlap.isChecked():
            self.model.change_gradient_mode_("O")
        if self.model.model_data.list_original_image:
            self.show_to_window.show_overlay_and_birds_view()

    @staticmethod
    def overlapping_transparency(image_1, image_2):
        return cv2.subtract(image_1, image_2)

    @classmethod
    def cropImage(cls, image):
        return image[int(image.shape[0] / 2 - 200):int(image.shape[0] / 2 + 200),
               int(image.shape[1] / 2 - 200):int(image.shape[1] / 2 + 200)]

    # def hide(self):
    #     self.main_ui.line_5.hide()

