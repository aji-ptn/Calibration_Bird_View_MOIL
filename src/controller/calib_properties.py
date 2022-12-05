from .configuration_image_1 import ConfigurationImage1
from .configuration_image_2 import ConfigurationImage2
from .configuration_image_3 import ConfigurationImage3
from .configuration_image_4 import ConfigurationImage4
from .configuration_image_5 import ConfigurationImage5
from .configuration_image_6 import ConfigurationImage6
from .view_additional_function import select_file


class CalibProperties:
    def __init__(self, view_controller):
        self.view_controller = view_controller
        self.list_properties = []

        self.config_image_1 = ConfigurationImage1(self.view_controller)
        self.config_image_2 = ConfigurationImage2(self.view_controller)
        self.config_image_3 = ConfigurationImage3(self.view_controller)
        self.config_image_4 = ConfigurationImage4(self.view_controller)
        self.config_image_5 = ConfigurationImage5(self.view_controller)
        self.config_image_6 = ConfigurationImage6(self.view_controller)

        self.view_controller.main_ui.button_save_config.clicked.connect(self.view_controller.controller.save_config_to_file)
        # self.view_controller.main_ui.button_save_config.clicked.connect(self.view_controller.controller.save_image_calibration)
        self.view_controller.main_ui.button_load_config.clicked.connect(self.onclick_load_config)

    def onclick_load_config(self):
        config_path = select_file(self.view_controller, "Select config !!", "../data_config",
                                  "config file (*.yaml)")
        if config_path:
            self.view_controller.controller.load_config(config_path)
            self.config_image_1.load_config()
            self.config_image_2.load_config()
            self.config_image_3.load_config()
            self.config_image_4.load_config()
            if self.view_controller.model.total_camera_used == 6:
                self.config_image_5.load_config()
                self.config_image_6.load_config()
            self.view_controller.control_widget.initial_toolbox_configuration()
            self.set_camera_placement()

    def set_camera_placement(self):
        camera_placement = self.view_controller.model.camera_placement
        if camera_placement == "center":
            self.view_controller.main_ui.radio_button_select_center.setChecked(True)
        else:
            self.view_controller.main_ui.radio_button_select_corner.setChecked(True)
        self.view_controller.change_mode_camera_placement()

    def initialize_properties(self):
        """

        Returns:

        """
        camera_placement = "corner" if self.view_controller.main_ui.radio_button_select_corner.isChecked() else "center"
        self.list_properties_all_image()
        # self.view_controller.model.total_camera_used = self.view_controller.model.total_camera_used
        self.view_controller.model.camera_placement = camera_placement
        self.view_controller.controller.initialize_image_data()
        self.view_controller.controller.moildev = []
        self.view_controller.model.list_original_image = []

    def list_properties_all_image(self):
        self.list_properties = [self.config_image_1.update_properties,
                                self.config_image_2.update_properties,
                                self.config_image_3.update_properties,
                                self.config_image_4.update_properties,
                                self.config_image_5.update_properties,
                                self.config_image_6.update_properties]
