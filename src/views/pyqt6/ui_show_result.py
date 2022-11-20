from .view_additional_function import show_image_to_label


class UiShowResult:
    def __init__(self, view_controller):
        self.view_controller = view_controller
        self.width_result_image = 720
        self.width_result_video = 720
        self.view_controller.main_ui.button_zoom_in.clicked.connect(self.zoom_in)
        self.view_controller.main_ui.button_zoom_out.clicked.connect(self.zoom_out)
        self.view_controller.main_ui.button_zoom_in_video.clicked.connect(self.zoom_in_video)
        self.view_controller.main_ui.button_zoom_out_video.clicked.connect(self.zoom_out_video)

    def show_overlay_and_birds_view(self):
        self.view_controller.controller.update_overlay_and_birds_view_image()
        image_overlay = self.view_controller.model.overlap_image
        image_birds_view = self.view_controller.model.bird_view_image
        if image_overlay is not None:
            show_image_to_label(self.view_controller.main_ui.label_window_overlay_image, image_overlay,
                                self.width_result_image)
            show_image_to_label(self.view_controller.main_ui.label_window_birds_view, image_birds_view,
                                self.width_result_image)

            self.view_controller.toolbox_activation()

    def show_image_to_label(self):
        """

        Returns:

        """
        self.view_controller.controller.update_union_original_image()
        image = self.view_controller.model.union_original_image
        if image is not None:
            show_image_to_label(self.view_controller.main_ui.label_8, image, 720)

    def showing_video_result(self):
        # try:
        self.view_controller.controller.control_video.next_frame()
        if self.view_controller.main_ui.button_change_view.isChecked():
            status = "original"
            show_image_to_label(self.view_controller.main_ui.label, self.view_controller.model.union_frame_video,
                                self.width_result_video)
        else:
            status = "birds_view"
            show_image_to_label(self.view_controller.main_ui.label, self.view_controller.model.bird_view_video,
                                self.width_result_video)
        self.view_controller.set_icon.set_icon_change_mode_view_video(status)

        # except:
        #     self.view_controller.main_ui.btn_play_pause.setChecked(False)
        #     self.view_controller.set_icon.set_icon_video_play_pause("begin")
        #     print("Have error in media source")

    def zoom_in(self):
        try:
            if self.width_result_image > 1200:
                pass
            else:
                self.width_result_image += 40
            self.show_overlay_and_birds_view()
        except:
            pass

    def zoom_out(self):
        try:
            if self.width_result_image < 400:
                pass

            else:
                self.width_result_image -= 40
            self.show_overlay_and_birds_view()

        except:
            pass

    def zoom_in_video(self):
        if self.width_result_video > 1200:
            pass
        else:
            self.width_result_video += 40
        self.showing_video_result()

    def zoom_out_video(self):
        if self.width_result_video < 400:
            pass

        else:
            self.width_result_video -= 40
        self.showing_video_result()
