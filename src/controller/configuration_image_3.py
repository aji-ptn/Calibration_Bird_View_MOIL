from PyQt6.QtCore import Qt
from .view_additional_function import calculate_ratio_image


class ConfigurationImage3:
    def __init__(self, view_controller):
        """
        Function construction for class ConfigurationImage3
        Args:
            view_controller: main view controller
        """
        self.view_controller = view_controller
        self.connect_configuration()

    def connect_configuration(self):
        """
        Connect button from user interface to the program
        """
        self.view_controller.main_ui.val_alpha_image_3.valueChanged.connect(self.change_properties_optical_center)
        self.view_controller.main_ui.val_beta_image_3.valueChanged.connect(self.change_properties_optical_center)
        self.view_controller.main_ui.val_zoom_image_3.valueChanged.connect(self.change_properties_anypoint)
        self.view_controller.main_ui.val_rotate_image_3.valueChanged.connect(self.change_properties_anypoint)
        self.view_controller.main_ui.val_coordinate_x_image_3.valueChanged.connect(self.change_properties_overlay)
        self.view_controller.main_ui.val_coordinate_y_image_3.valueChanged.connect(self.change_properties_overlay)
        self.view_controller.main_ui.val_crop_top_image_3.valueChanged.connect(self.change_properties_cropping)
        self.view_controller.main_ui.val_crop_bottom_image_3.valueChanged.connect(self.change_properties_cropping)
        self.view_controller.main_ui.val_crop_left_image_3.valueChanged.connect(self.change_properties_cropping)
        self.view_controller.main_ui.val_crop_right_image_3.valueChanged.connect(self.change_properties_cropping)

    def change_properties_optical_center(self):
        """
        This change_properties_center_image_3_event function will be used to control alpha & beta
        each action of the part image 3 in the user interface frame
        """
        self.view_controller.model.properties_image["Image_3"]["alpha"] = self.view_controller.main_ui.val_alpha_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["beta"] = self.view_controller.main_ui.val_beta_image_3.value()
        self.view_controller.controller.process_generating_anypoint_image(2)
        self.view_controller.show_to_window.show_overlay_and_birds_view()
        if self.view_controller.model.list_frame_video:
            self.view_controller.controller.update_properties_anypoint()
            self.view_controller.show_to_window.showing_video_result()

    def change_properties_anypoint(self):
        """
        The change_properties_anypoint_image_3 function will be used control zoom & rotate
        each acton of the part image 3 in the user interface frame
        """
        self.view_controller.model.properties_image["Image_3"]["zoom"] = self.view_controller.main_ui.val_zoom_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["rotate"] = self.view_controller.main_ui.val_rotate_image_3.value()
        self.view_controller.controller.process_generating_anypoint_image(2)
        self.view_controller.show_to_window.show_overlay_and_birds_view()
        if self.view_controller.model.list_frame_video:
            self.view_controller.controller.update_properties_anypoint()
            self.view_controller.show_to_window.showing_video_result()

    def change_properties_overlay(self):
        """
        The change_properties_overlay_image_3 function will be used control shift_x & shift_y
        each acton of the part image 3 in the user interface frame
        """
        if self.view_controller.model.total_camera_used == 4:
            if self.view_controller.main_ui.radio_button_select_center.isChecked():
                self.view_controller.main_ui.val_coordinate_x_image_3.setMaximum(0)
        self.view_controller.model.properties_image["Image_3"]["shift_x"] = self.view_controller.main_ui.val_coordinate_x_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["shift_y"] = self.view_controller.main_ui.val_coordinate_y_image_3.value()
        self.view_controller.show_to_window.show_overlay_and_birds_view()

    def change_properties_cropping(self):
        """
        The change_properties_cropping_image_3 function will be used control crop_top, crop_bottom,
        crop_left & crop_right each acton of the part image 3 in the user interface frame
        """
        self.view_controller.model.properties_image["Image_3"]["crop_top"] = self.view_controller.main_ui.val_crop_top_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["crop_bottom"] = self.view_controller.main_ui.val_crop_bottom_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["crop_left"] = self.view_controller.main_ui.val_crop_left_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["crop_right"] = self.view_controller.main_ui.val_crop_right_image_3.value()
        self.view_controller.show_to_window.show_overlay_and_birds_view()
                
    def update_properties(self):
        """
        The update_properties_image_3 function. The data is come from user interface control by user and will
        store on the model class
        """
        self.view_controller.model.properties_image["Image_3"] = {}
        self.view_controller.model.properties_image["Image_3"]["alpha"] = self.view_controller.main_ui.val_alpha_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["beta"] = self.view_controller.main_ui.val_beta_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["zoom"] = self.view_controller.main_ui.val_zoom_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["rotate"] = self.view_controller.main_ui.val_rotate_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["shift_x"] = self.view_controller.main_ui.val_coordinate_x_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["shift_y"] = self.view_controller.main_ui.val_coordinate_y_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["crop_top"] = self.view_controller.main_ui.val_crop_top_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["crop_bottom"] = self.view_controller.main_ui.val_crop_bottom_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["crop_left"] = self.view_controller.main_ui.val_crop_left_image_3.value()
        self.view_controller.model.properties_image["Image_3"]["crop_right"] = self.view_controller.main_ui.val_crop_right_image_3.value()

    def load_config(self):
        """
        Load config from file and put value in user interface
        """
        self.block_signal()
        self.view_controller.main_ui.val_alpha_image_3.setValue(self.view_controller.model.properties_image["Image_3"]["alpha"])
        self.view_controller.main_ui.val_beta_image_3.setValue(self.view_controller.model.properties_image["Image_3"]["beta"])
        self.view_controller.main_ui.val_zoom_image_3.setValue(self.view_controller.model.properties_image["Image_3"]["zoom"])
        self.view_controller.main_ui.val_rotate_image_3.setValue(self.view_controller.model.properties_image["Image_3"]["rotate"])
        self.view_controller.main_ui.val_coordinate_x_image_3.setValue(self.view_controller.model.properties_image["Image_3"]["shift_x"])
        self.view_controller.main_ui.val_coordinate_y_image_3.setValue(self.view_controller.model.properties_image["Image_3"]["shift_y"])
        self.view_controller.main_ui.val_crop_top_image_3.setValue(self.view_controller.model.properties_image["Image_3"]["crop_top"])
        self.view_controller.main_ui.val_crop_bottom_image_3.setValue(self.view_controller.model.properties_image["Image_3"]["crop_bottom"])
        self.view_controller.main_ui.val_crop_left_image_3.setValue(self.view_controller.model.properties_image["Image_3"]["crop_left"])
        self.view_controller.main_ui.val_crop_right_image_3.setValue(self.view_controller.model.properties_image["Image_3"]["crop_right"])
        self.unblock_signal()

    def block_signal(self):
        """
        Block signal ui when value change
        """
        self.view_controller.main_ui.val_alpha_image_3.blockSignals(True)
        self.view_controller.main_ui.val_beta_image_3.blockSignals(True)
        self.view_controller.main_ui.val_zoom_image_3.blockSignals(True)
        self.view_controller.main_ui.val_rotate_image_3.blockSignals(True)
        self.view_controller.main_ui.val_coordinate_x_image_3.blockSignals(True)
        self.view_controller.main_ui.val_coordinate_y_image_3.blockSignals(True)
        self.view_controller.main_ui.val_crop_top_image_3.blockSignals(True)
        self.view_controller.main_ui.val_crop_bottom_image_3.blockSignals(True)
        self.view_controller.main_ui.val_crop_left_image_3.blockSignals(True)
        self.view_controller.main_ui.val_crop_right_image_3.blockSignals(True)

    def unblock_signal(self):
        """
        Unlock signal ui when value change
        """
        self.view_controller.main_ui.val_alpha_image_3.blockSignals(False)
        self.view_controller.main_ui.val_beta_image_3.blockSignals(False)
        self.view_controller.main_ui.val_zoom_image_3.blockSignals(False)
        self.view_controller.main_ui.val_rotate_image_3.blockSignals(False)
        self.view_controller.main_ui.val_coordinate_x_image_3.blockSignals(False)
        self.view_controller.main_ui.val_coordinate_y_image_3.blockSignals(False)
        self.view_controller.main_ui.val_crop_top_image_3.blockSignals(False)
        self.view_controller.main_ui.val_crop_bottom_image_3.blockSignals(False)
        self.view_controller.main_ui.val_crop_left_image_3.blockSignals(False)
        self.view_controller.main_ui.val_crop_right_image_3.blockSignals(False)
