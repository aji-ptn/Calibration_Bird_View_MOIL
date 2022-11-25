from .ui_py.total_camera_ui import Ui_Dialog
from PyQt5 import QtWidgets
from .view_additional_function import select_file


class UiImageController:
    def __init__(self, view_controller):
        self.view_controller = view_controller
        self.view_controller.main_ui.button_open_image.clicked.connect(self.select_source_image)

    def select_source_image(self):
        """
        The select_source_image function will open a dialog to search the file image from the directory.
        """
        self.show_choose_total_camera()
        if self.view_controller.model.total_camera_used is not None:
            self.view_controller.calib_properties.initialize_properties()
            self.view_controller.control_widget.initial_toolbox_configuration()

            # image = ["/home/aji/Documents/MyGithub/OpenCV_bird_view_main/11192022/123/image3.jpg",
            #          "/home/aji/Documents/MyGithub/OpenCV_bird_view_main/11192022/123/image2.jpg",
            #          "/home/aji/Documents/MyGithub/OpenCV_bird_view_main/11192022/123/image4.jpg",
            #          "/home/aji/Documents/MyGithub/OpenCV_bird_view_main/11192022/123/image1.jpg"]
            # parameters = [
            #     "../parameters/20220803_entaniya_vr220_12_2592x1944_moil230_heru.json",
            #     "../parameters/20220818_entaniya_vr220_14_2592x1944_moil230_heru_andy.json",
            #     "../parameters/20220803_entaniya_vr220_11_2592x1944_moil230_heru.json",
            #     "../parameters/20220818_entaniya_vr220_13_2592x1944_moil230_heru.json"]

            image = ["/home/aji/Documents/MyGithub/calib_bird_view_MOIL/1/front_true_.jpg",
                     "/home/aji/Documents/MyGithub/calib_bird_view_MOIL/1/left_true_.jpg",
                     "/home/aji/Documents/MyGithub/calib_bird_view_MOIL/1/right_true_.jpg",
                     "/home/aji/Documents/MyGithub/calib_bird_view_MOIL/1/back_true_.jpg"]

            parameters = ["/home/aji/Documents/MyGithub/calib_bird_view_MOIL/parameters/20220706_entaniya_vr220_1_2592x1944_moil230_andy.json",
                          "/home/aji/Documents/MyGithub/calib_bird_view_MOIL/parameters/20220706_entaniya_vr220_1_2592x1944_moil230_andy.json",
                          "/home/aji/Documents/MyGithub/calib_bird_view_MOIL/parameters/20220706_entaniya_vr220_1_2592x1944_moil230_andy.json",
                          "/home/aji/Documents/MyGithub/calib_bird_view_MOIL/parameters/20220706_entaniya_vr220_1_2592x1944_moil230_andy.json"]

            for i in range(self.view_controller.model.total_camera_used):
                # filepath_image = select_file(None, "Select Image !!", "",
                #                              "Image Files (*.jpeg *.jpg *.png *.gif *.bmg)")
                #
                # if filepath_image:
                #     filepath_parameter = select_file(None, "Select Parameter Camera !!", "",
                #                                      "Parameter Files (*.json *.txt)")
                #
                #     if filepath_parameter:
                # self.view_controller.controller.list_image_data(filepath_image)
                self.view_controller.controller.list_image_data(image[i])
                self.view_controller.controller.list_moildev_object(parameters[i])
                # self.view_controller.controller.list_moildev_object(filepath_parameter)
                # self.update_icx_icy_image(i)
                self.view_controller.calib_properties.list_properties[i]()
                self.view_controller.controller.process_generating_anypoint_image(i)
                self.view_controller.toolbox_activation()
                self.view_controller.show_to_window.show_image_to_label()

            if len(self.view_controller.model.list_original_image) == self.view_controller.model.total_camera_used:
                self.view_controller.show_to_window.show_overlay_and_birds_view()
                self.view_controller.model.list_reverse_alignment = self.view_controller.model.list_reverse_image
            else:
                print("Not enough image resources")

    def set_total_camera(self, ui_total_cam):
        self.view_controller.model.total_camera_used = int(ui_total_cam.comboBox.currentText())

    def show_choose_total_camera(self):
        self.view_controller.model.total_camera_used = None
        windowDevice = QtWidgets.QDialog()
        ui_total_cam = Ui_Dialog()
        ui_total_cam.setupUi(windowDevice)
        ui_total_cam.buttonBox.accepted.connect(lambda: self.set_total_camera(ui_total_cam))
        windowDevice.exec()

    def update_icx_icy_image(self, i):
        if i == 0:
            self.view_controller.calib_properties.config_image_1.update_icx_icy()
        elif i == 1:
            self.view_controller.calib_properties.config_image_2.update_icx_icy()
        elif i == 2:
            self.view_controller.calib_properties.config_image_3.update_icx_icy()
        elif i == 3:
            self.view_controller.calib_properties.config_image_4.update_icx_icy()
        elif i == 4:
            self.view_controller.calib_properties.config_image_5.update_icx_icy()
        elif i == 5:
            self.view_controller.calib_properties.config_image_6.update_icx_icy()
