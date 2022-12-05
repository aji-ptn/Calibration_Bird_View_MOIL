

class ControlWidget:
    def __init__(self, ui_main_controller):
        self.ui_main_controller = ui_main_controller
        self.ui_main_controller.main_ui.button_show_hide_config.clicked.connect(self.hide_show_scroll_area_config)
        self.ui_main_controller.main_ui.button_show_hide_rebalance.clicked.connect(self.hide_show_scroll_area_balanced)
        self.ui_main_controller.main_ui.button_auto_level.clicked.connect(self.hide_show_alignment_window)
        self.ui_main_controller.main_ui.button_run_video.clicked.connect(self.hide_show_frame_video_viewer)
        self.ui_main_controller.main_ui.button_change_mode_view.clicked.connect(self.control_mode_view)

        self.initial_hide_button()

    def initial_hide_button(self):
        self.ui_main_controller.main_ui.frame_rebalance_image.hide()
        self.ui_main_controller.main_ui.frame_birds_view.hide()
        self.ui_main_controller.main_ui.frame_video_viewer.hide()
        self.ui_main_controller.main_ui.line_main_view.hide()
        self.ui_main_controller.main_ui.frame_mode_view.hide()
        self.ui_main_controller.main_ui.frame_radio_button_alligment_image_2.hide()
        self.ui_main_controller.main_ui.frame_radio_button_alligment_image_3.hide()
        self.ui_main_controller.main_ui.frame_radio_button_alligment_image_4.hide()

    def control_mode_view(self):
        if self.ui_main_controller.main_ui.button_change_mode_view.isChecked():
            self.ui_main_controller.main_ui.frame_mode_view.show()
        else:
            self.ui_main_controller.main_ui.frame_mode_view.hide()

    def initial_toolbox_configuration(self):
        if self.ui_main_controller.model.total_camera_used == 4:
            self.ui_main_controller.main_ui.toolbox_configuration.setItemEnabled(4, False)
            self.ui_main_controller.main_ui.toolbox_configuration.setItemEnabled(5, False)
        elif self.ui_main_controller.model.total_camera_used == 6:
            self.ui_main_controller.main_ui.toolbox_configuration.setItemEnabled(4, True)
            self.ui_main_controller.main_ui.toolbox_configuration.setItemEnabled(5, True)
        else:
            print("Under development")

    def hide_show_frame_video_viewer(self):
        if self.ui_main_controller.main_ui.button_run_video.isChecked():
            self.ui_main_controller.main_ui.button_auto_level.setChecked(False)
            self.ui_main_controller.main_ui.frame_original_image.hide()
            self.ui_main_controller.main_ui.frame_video_viewer.show()
            self.ui_main_controller.main_ui.frame_radio_button_alligment_image_2.hide()
            self.ui_main_controller.main_ui.frame_radio_button_alligment_image_3.hide()
            self.ui_main_controller.main_ui.frame_radio_button_alligment_image_4.hide()
            self.ui_main_controller.main_ui.label_title_frame_rebalance.setText("Video Viewer")
            self.ui_main_controller.main_ui.frame_rebalance_image.hide()

        else:
            self.ui_main_controller.main_ui.frame_original_image.show()
            self.ui_main_controller.main_ui.frame_rebalance_image.hide()
            self.ui_main_controller.main_ui.frame_video_viewer.hide()
            self.ui_main_controller.main_ui.label_title_frame_rebalance.setText("Original Image")

    def hide_show_alignment_window(self):
        if self.ui_main_controller.main_ui.button_auto_level.isChecked():
            self.ui_main_controller.main_ui.button_run_video.setChecked(False)
            self.ui_main_controller.main_ui.frame_original_image.hide()
            self.ui_main_controller.main_ui.frame_video_viewer.hide()
            self.ui_main_controller.main_ui.frame_rebalance_image.show()
            self.ui_main_controller.main_ui.frame_radio_button_alligment_image_2.show()
            self.ui_main_controller.main_ui.frame_radio_button_alligment_image_3.show()
            self.ui_main_controller.main_ui.frame_radio_button_alligment_image_4.show()
            self.ui_main_controller.main_ui.label_title_frame_rebalance.setText("Alignment of the images")

        else:
            self.ui_main_controller.main_ui.frame_original_image.show()
            self.ui_main_controller.main_ui.frame_video_viewer.hide()
            self.ui_main_controller.main_ui.frame_rebalance_image.hide()
            self.ui_main_controller.main_ui.frame_radio_button_alligment_image_2.hide()
            self.ui_main_controller.main_ui.frame_radio_button_alligment_image_3.hide()
            self.ui_main_controller.main_ui.frame_radio_button_alligment_image_4.hide()
            self.ui_main_controller.main_ui.label_title_frame_rebalance.setText("Original Image")

    def hide_show_scroll_area_config(self):
        if self.ui_main_controller.main_ui.scroll_area_config.isHidden():
            self.ui_main_controller.main_ui.scroll_area_config.show()
            self.ui_main_controller.main_ui.frame.show()
            status_view = True
        else:
            self.ui_main_controller.main_ui.scroll_area_config.hide()
            self.ui_main_controller.main_ui.frame.hide()
            status_view = False
        self.ui_main_controller.set_icon.icon_hide_show_config(status_view)

    def hide_show_scroll_area_balanced(self):
        if self.ui_main_controller.main_ui.scroll_area_rebalance.isHidden():
            self.ui_main_controller.main_ui.frame_3.show()
            self.ui_main_controller.main_ui.frame_birds_view.hide()
            self.ui_main_controller.main_ui.line_main_view.hide()
            self.ui_main_controller.main_ui.scroll_area_rebalance.show()
            status_view = True
        else:
            self.ui_main_controller.main_ui.line_main_view.show()
            self.ui_main_controller.main_ui.scroll_area_rebalance.hide()
            self.ui_main_controller.main_ui.frame_birds_view.show()
            self.ui_main_controller.main_ui.frame_3.hide()
            status_view = False
        self.ui_main_controller.set_icon.icon_hide_show_adjust_level(status_view)
