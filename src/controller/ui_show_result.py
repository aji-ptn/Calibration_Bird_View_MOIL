import cv2
import numpy as np

from .view_additional_function import show_image_to_label


class UiShowResult:
    def __init__(self, view_controller):
        self.view_controller = view_controller
        self.width_overlay_image = 720
        self.width_bird_view_image = 720
        self.width_result_video = 720

        # self.view_controller.main_ui.button_zoom_in_overlay.clicked.connect(self.zoom_in)
        # self.view_controller.main_ui.button_zoom_out_overlay.clicked.connect(self.zoom_out)

        self.view_controller.main_ui.button_zoom_in_overlay.clicked.connect(self.zoom_in_overlay)
        self.view_controller.main_ui.button_zoom_out_overlay.clicked.connect(self.zoom_out_overlay)
        self.view_controller.main_ui.button_zoom_in_birds_view.clicked.connect(self.zoom_in_bird_view)
        self.view_controller.main_ui.button_zoom_out_birds_view.clicked.connect(self.zoom_out_bird_view)

        self.view_controller.main_ui.button_zoom_in_video.clicked.connect(self.zoom_in_video)
        self.view_controller.main_ui.button_zoom_out_video.clicked.connect(self.zoom_out_video)

    def show_overlay_and_birds_view(self):
        self.view_controller.model.update_overlay_and_birds_view_image()
        image_overlay = self.view_controller.model.model_data.overlap_image
        image_birds_view = self.view_controller.model.model_data.bird_view_image
        if image_overlay is not None:
            show_image_to_label(self.view_controller.main_ui.label_window_overlay_image, image_overlay,
                                self.width_overlay_image)
            show_image_to_label(self.view_controller.main_ui.label_window_birds_view, image_birds_view,
                                self.width_bird_view_image)

    def show_image_to_label(self):
        """

        Returns:

        """
        self.view_controller.model.update_union_original_image()
        image = self.view_controller.model.model_data.union_original_image
        if image is not None:
            show_image_to_label(self.view_controller.main_ui.label_8, image, 720)

    def showing_video_result(self):
        # if mode_view == "birds_view":
        self.view_controller.model.control_video.next_frame()
        show_image_to_label(self.view_controller.main_ui.label, self.view_controller.model.bird_view_video,
                            self.width_result_video)

        # elif mode_view == "original":
        #     self.view_controller.model.control_video.next_frame(mode_view)
        #     show_image_to_label(self.view_controller.main_ui.label, self.view_controller.model.union_frame_video,
        #                         self.width_result_video)

    def adjust_gamma(self, image, gamma=1.0):
        # build a lookup table mapping the pixel values [0, 255] to
        # their adjusted gamma values
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255
                          for i in np.arange(0, 256)]).astype("uint8")
        # apply gamma correction using the lookup table
        return cv2.LUT(image, table)

        # except:
        #     self.view_controller.main_ui.btn_play_pause.setChecked(False)
        #     self.view_controller.set_icon.set_icon_video_play_pause("begin")
        #     print("Have error in media source")

    def zoom_in_overlay(self):
        try:
            if self.width_overlay_image > 1200:
                pass
            else:
                self.width_overlay_image += 40
            self.show_overlay_and_birds_view()
        except:
            pass

    def zoom_out_overlay(self):
        try:
            if self.width_overlay_image < 400:
                pass

            else:
                self.width_overlay_image -= 40
            self.show_overlay_and_birds_view()

        except:
            pass

    def zoom_in_bird_view(self):
        try:
            if self.width_bird_view_image > 1200:
                pass
            else:
                self.width_bird_view_image += 40
            self.show_overlay_and_birds_view()
        except:
            pass

    def zoom_out_bird_view(self):
        try:
            if self.width_bird_view_image < 400:
                pass

            else:
                self.width_bird_view_image -= 40
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
