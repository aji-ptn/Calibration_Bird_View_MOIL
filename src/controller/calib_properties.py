from .configuration_image_1 import ConfigurationImage1
from .configuration_image_2 import ConfigurationImage2
from .configuration_image_3 import ConfigurationImage3
from .configuration_image_4 import ConfigurationImage4
from .view_additional_function import select_file


class CalibProperties:
    def __init__(self, view_controller):
        self.view_controller = view_controller
        self.list_properties = []

        self.config_image_1 = ConfigurationImage1(self.view_controller)
        self.config_image_2 = ConfigurationImage2(self.view_controller)
        self.config_image_3 = ConfigurationImage3(self.view_controller)
        self.config_image_4 = ConfigurationImage4(self.view_controller)

        self.view_controller.main_ui.button_save_config.clicked.connect(self.view_controller.controller.save_config_to_file)
        # self.view_controller.main_ui.button_save_config.clicked.connect(self.view_controller.controller.save_image_calibration)
        self.view_controller.main_ui.button_load_config.clicked.connect(self.onclick_load_config)

    def onclick_load_config(self):
        """
        This function is for select file configuration from directory
        Returns:
        If True, value from configuration will fill the user interface
        """
        config_path = select_file(self.view_controller, "Select config !!", "../data_config",
                                  "config file (*.yaml)")
        if config_path:
            self.view_controller.controller.load_config(config_path)
            self.config_image_1.load_config()
            self.config_image_2.load_config()
            self.config_image_3.load_config()
            self.config_image_4.load_config()
            self.view_controller.control_widget.initial_toolbox_configuration()

    def initialize_properties(self):
        """
            This image is for initialise configuration properties image
        """
        self.list_properties_all_image()
        self.view_controller.controller.initialize_image_data()
        self.view_controller.controller.moildev = []
        self.view_controller.model.list_original_image = []

    def list_properties_all_image(self):
        """
         This function is for create list of properties image
        """
        self.list_properties = [self.config_image_1.update_properties,
                                self.config_image_2.update_properties,
                                self.config_image_3.update_properties,
                                self.config_image_4.update_properties]
