from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from .view_additional_function import calculate_ratio_image


class ConfigurationImage2:
    def __init__(self, view_controller):
        self.view_controller = view_controller
        self.connect_configuration()

    def connect_configuration(self):
        self.view_controller.main_ui.val_icx_image_2.valueChanged.connect(self.change_properties_optical_center)
        self.view_controller.main_ui.val_icy_image_2.valueChanged.connect(self.change_properties_optical_center)
        self.view_controller.main_ui.val_zoom_image_2.valueChanged.connect(self.change_properties_anypoint)
        self.view_controller.main_ui.val_rotate_image_2.valueChanged.connect(self.change_properties_anypoint)
        self.view_controller.main_ui.val_coordinate_x_image_2.valueChanged.connect(self.change_properties_overlay)
        self.view_controller.main_ui.val_coordinate_y_image_2.valueChanged.connect(self.change_properties_overlay)
        self.view_controller.main_ui.val_crop_top_image_2.valueChanged.connect(self.change_properties_cropping)
        self.view_controller.main_ui.val_crop_bottom_image_2.valueChanged.connect(self.change_properties_cropping)
        self.view_controller.main_ui.val_crop_left_image_2.valueChanged.connect(self.change_properties_cropping)
        self.view_controller.main_ui.val_crop_right_image_2.valueChanged.connect(self.change_properties_cropping)

    def mouse_wheelEvent_left(self, e):
        """
        Resize image using mouse wheel event.
        """
        if self.view_controller.model.list_original_image[1] is not None:
            modifiers = QApplication.keyboardModifiers()
            if modifiers == Qt.KeyboardModifier.ControlModifier:
                wheel_counter = e.angleDelta()
                print(wheel_counter)

    # This is mouse event alignment_label_1
    def mouse_event_alignment_label_1(self, e):
        """
        select area for new icx and icy on image
        """
        print("Click even config image 2 label 1")
        if e.button() == Qt.MouseButton.LeftButton:
            pos_x = round(e.position().x())
            pos_y = round(e.position().y())
            print(pos_x)
            print(pos_y)
            if self.view_controller.model.list_original_image[1] is not None:
                ratio_x, ratio_y = calculate_ratio_image(self.view_controller.main_ui.label_original_alligment_1,
                                                         self.view_controller.model.list_original_image[1])
                icx_left = round(pos_x * ratio_x)
                icy_left = round(pos_y * ratio_y)
                print("from view: icx: {} icy:{}".format(icx_left, icy_left))
                self.view_controller.model.list_icx[0] = icx_left
                self.view_controller.model.list_icy[0] = icy_left
                self.view_controller.controller.generate_reverse_alignment(0, 1)
                self.select_image_state()

        # elif e.button() == Qt.RightButton:
        #     if self.image_left is not None:
        #         menu = QtWidgets.QMenu()
        #         save = menu.addAction("Open Image")
        #         info = menu.addAction("Show Info")
        #         save.triggered.connect(self.openImageLeft)
        #         # info.triggered.connect(self.onclick_help)
        #         menu.exec_(e.globalPos())

    # This is mouse event alignment_label_2
    def mouse_event_alignment_label_2(self, e):
        """
        select area for new icx and icy on image
        """
        print("Click even config image 2 label 1")
        if e.button() == Qt.MouseButton.LeftButton:
            pos_x = round(e.position().x())
            pos_y = round(e.position().y())
            print(pos_x)
            print(pos_y)
            if self.view_controller.model.list_original_image[1] is not None:
                ratio_x, ratio_y = calculate_ratio_image(self.view_controller.main_ui.label_original_alligment_2,
                                                         self.view_controller.model.list_original_image[1])
                icx_left = round(pos_x * ratio_x)
                icy_left = round(pos_y * ratio_y)
                print("from view: icx: {} icy:{}".format(icx_left, icy_left))
                self.view_controller.model.list_icx[1] = icx_left
                self.view_controller.model.list_icy[1] = icy_left
                self.view_controller.controller.generate_reverse_alignment(1, 1)
                self.select_image_state()

        # elif e.button() == Qt.RightButton:
        #     if self.image_left is not None:
        #         menu = QtWidgets.QMenu()
        #         save = menu.addAction("Open Image")
        #         info = menu.addAction("Show Info")
        #         save.triggered.connect(self.openImageLeft)
        #         # info.triggered.connect(self.onclick_help)
        #         menu.exec_(e.globalPos())

    def select_image_state(self):
        image_state = self.view_controller.main_ui.toolbox_configuration.currentIndex()
        if image_state == 0:
            self.view_controller.show_toolbox_image_1()
            print("image 1")
        elif image_state == 1:
            self.view_controller.radio_button_event_alignment_image_2()
            print("image 2")
        elif image_state == 2:
            print("image 3")
            self.view_controller.radio_button_event_alignment_image_3()
        elif image_state == 3:
            print("image 4")
            self.view_controller.radio_button_event_alignment_image_4()

    def change_properties_optical_center(self):
        """
        This change_properties_center_image_2_event function will be used to control icx & icy
        each action of the part image 2 in the user interface frame
        """
        self.view_controller.model.properties_image["Image_2"]["icx"] = self.view_controller.main_ui.val_icx_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["icy"] = self.view_controller.main_ui.val_icy_image_2.value()
        self.view_controller.controller.process_generating_reverse_image(1)
        self.view_controller.show_to_window.show_overlay_and_birds_view()
        if self.view_controller.model.list_frame_video:
            self.view_controller.controller.update_properties_anypoint()
            self.view_controller.show_to_window.showing_video_result()

    def change_properties_anypoint(self):
        """
        The change_properties_anypoint_image_2 function will be used control zoom & rotate
        each acton of the part image 2 in the user interface frame
        """
        self.view_controller.model.properties_image["Image_2"]["zoom"] = self.view_controller.main_ui.val_zoom_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["rotate"] = self.view_controller.main_ui.val_rotate_image_2.value()
        self.view_controller.controller.process_generating_anypoint_image(1)
        self.view_controller.show_to_window.show_overlay_and_birds_view()
        if self.view_controller.model.list_frame_video:
            self.view_controller.controller.update_properties_anypoint()
            self.view_controller.show_to_window.showing_video_result()

    def change_properties_overlay(self):
        """
        The change_properties_overlay_image_2 function will be used control shift_x & shift_y
        each acton of the part image 2 in the user interface frame
        """
        self.view_controller.model.properties_image["Image_2"]["shift_x"] = self.view_controller.main_ui.val_coordinate_x_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["shift_y"] = self.view_controller.main_ui.val_coordinate_y_image_2.value()
        self.view_controller.show_to_window.show_overlay_and_birds_view()

    def change_properties_cropping(self):
        """
        The change_properties_cropping_image_2 function will be used control crop_top, crop_bottom,
        crop_left & crop_right each acton of the part image 2 in the user interface frame
        """
        self.view_controller.model.properties_image["Image_2"]["crop_top"] = self.view_controller.main_ui.val_crop_top_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["crop_bottom"] = self.view_controller.main_ui.val_crop_bottom_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["crop_left"] = self.view_controller.main_ui.val_crop_left_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["crop_right"] = self.view_controller.main_ui.val_crop_right_image_2.value()
        self.view_controller.show_to_window.show_overlay_and_birds_view()

    def update_properties(self):
        """
        The update_properties_image_2 function. The data is come from user interface control by user and will
        store on the model class
        """
        self.view_controller.model.properties_image["Image_2"] = {}
        self.view_controller.model.properties_image["Image_2"]["icx"] = self.view_controller.main_ui.val_icx_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["icy"] = self.view_controller.main_ui.val_icy_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["zoom"] = self.view_controller.main_ui.val_zoom_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["rotate"] = self.view_controller.main_ui.val_rotate_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["shift_x"] = self.view_controller.main_ui.val_coordinate_x_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["shift_y"] = self.view_controller.main_ui.val_coordinate_y_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["crop_top"] = self.view_controller.main_ui.val_crop_top_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["crop_bottom"] = self.view_controller.main_ui.val_crop_bottom_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["crop_left"] = self.view_controller.main_ui.val_crop_left_image_2.value()
        self.view_controller.model.properties_image["Image_2"]["crop_right"] = self.view_controller.main_ui.val_crop_right_image_2.value()

    def load_config(self):
        self.block_signal()
        self.view_controller.main_ui.val_icx_image_2.setValue(self.view_controller.model.properties_image["Image_2"]["icx"])
        self.view_controller.main_ui.val_icy_image_2.setValue(self.view_controller.model.properties_image["Image_2"]["icy"])
        self.view_controller.main_ui.val_zoom_image_2.setValue(self.view_controller.model.properties_image["Image_2"]["zoom"])
        self.view_controller.main_ui.val_rotate_image_2.setValue(self.view_controller.model.properties_image["Image_2"]["rotate"])
        self.view_controller.main_ui.val_coordinate_x_image_2.setValue(self.view_controller.model.properties_image["Image_2"]["shift_x"])
        self.view_controller.main_ui.val_coordinate_y_image_2.setValue(self.view_controller.model.properties_image["Image_2"]["shift_y"])
        self.view_controller.main_ui.val_crop_top_image_2.setValue(self.view_controller.model.properties_image["Image_2"]["crop_top"])
        self.view_controller.main_ui.val_crop_bottom_image_2.setValue(self.view_controller.model.properties_image["Image_2"]["crop_bottom"])
        self.view_controller.main_ui.val_crop_left_image_2.setValue(self.view_controller.model.properties_image["Image_2"]["crop_left"])
        self.view_controller.main_ui.val_crop_right_image_2.setValue(self.view_controller.model.properties_image["Image_2"]["crop_right"])
        self.unblock_signal()

    def block_signal(self):
        self.view_controller.main_ui.val_icx_image_2.blockSignals(True)
        self.view_controller.main_ui.val_icy_image_2.blockSignals(True)
        self.view_controller.main_ui.val_zoom_image_2.blockSignals(True)
        self.view_controller.main_ui.val_rotate_image_2.blockSignals(True)
        self.view_controller.main_ui.val_coordinate_x_image_2.blockSignals(True)
        self.view_controller.main_ui.val_coordinate_y_image_2.blockSignals(True)
        self.view_controller.main_ui.val_crop_top_image_2.blockSignals(True)
        self.view_controller.main_ui.val_crop_bottom_image_2.blockSignals(True)
        self.view_controller.main_ui.val_crop_left_image_2.blockSignals(True)
        self.view_controller.main_ui.val_crop_right_image_2.blockSignals(True)

    def unblock_signal(self):
        self.view_controller.main_ui.val_icx_image_2.blockSignals(False)
        self.view_controller.main_ui.val_icy_image_2.blockSignals(False)
        self.view_controller.main_ui.val_zoom_image_2.blockSignals(False)
        self.view_controller.main_ui.val_rotate_image_2.blockSignals(False)
        self.view_controller.main_ui.val_coordinate_x_image_2.blockSignals(False)
        self.view_controller.main_ui.val_coordinate_y_image_2.blockSignals(False)
        self.view_controller.main_ui.val_crop_top_image_2.blockSignals(False)
        self.view_controller.main_ui.val_crop_bottom_image_2.blockSignals(False)
        self.view_controller.main_ui.val_crop_left_image_2.blockSignals(False)
        self.view_controller.main_ui.val_crop_right_image_2.blockSignals(False)

    def update_icx_icy(self):
        self.block_signal()
        self.view_controller.main_ui.val_icx_image_2.setValue(self.view_controller.controller.moildev[1].icx())
        self.view_controller.main_ui.val_icy_image_2.setValue(self.view_controller.controller.moildev[1].icy())
        self.unblock_signal()