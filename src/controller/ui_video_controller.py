import os
import time
import cv2
import numpy as np
from PyQt6 import QtCore, QtWidgets
from .view_additional_function import select_file
from threading import Thread


class VStream:
    def __init__(self, src):
        self.capture = cv2.VideoCapture(src)
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while True:
            _, self.frame = self.capture.read()

    def get_frame(self):
        return self.frame


class UiVideoController:
    def __init__(self, view_controller):
        self.view_controller = view_controller

        self.__timer = QtCore.QTimer()
        self.__timer.timeout.connect(self.showing_to_ui)

        self.video_status = True
        self.mode_view = "birds_view"

        self.view_controller.main_ui.button_open_file_video.clicked.connect(self.select_source_video)

        self.view_controller.main_ui.btn_play_pause.clicked.connect(self.onclick_play_pause_video)
        self.view_controller.main_ui.btn_stop_video.clicked.connect(self.onclick_stop_video)
        self.view_controller.main_ui.slider_video.valueChanged.connect(self.change_value_slider)
        self.view_controller.main_ui.btn_skip_video.clicked.connect(
            self.view_controller.model.control_video.forward_video)
        self.view_controller.main_ui.btn_prev_video.clicked.connect(
            self.view_controller.model.control_video.rewind_video)

        self.view_controller.main_ui.button_save_frame.clicked.connect(self.save_frame_image)
        self.view_controller.main_ui.button_record_video.clicked.connect(self.record_bird_view_video)

    def save_frame_image(self):
        """
        To save image bird view to the directory
        Returns:

        """
        self.view_controller.model.control_video.save_bird_view_video()

    def select_source_video(self):
        """
        select video file from directory
        Returns:

        """
        list_cam_stream = [None] * 4
        self.video_status = True
        if self.view_controller.model.total_camera_used is not None:
            self.view_controller.model.control_video.initialize_video_data()
            for i in range(self.view_controller.model.total_camera_used):
                filepath_video = select_file(None, "Select video", "", "*.avi *.mp4")
                if filepath_video:
                    list_cam_stream[i] = filepath_video
                else:
                    break
            # list_cam_stream = ["../../video/sequence_video/7/video_3 1668069965.1640372_.avi",
            #                    "../../video/sequence_video/7/video_2 1668069965.1640372_.avi",
            #                    "../../video/sequence_video/7/video_4 1668069965.1640372_.avi",
            #                    "../../video/sequence_video/7/video_1 1668069965.1640372_.avi"]

            if any(elem is None for elem in list_cam_stream) is False:
                for i in range(self.view_controller.model.total_camera_used):
                    self.view_controller.model.control_video.running_video(i, list_cam_stream[i])

                self.view_controller.model.update_properties_anypoint()
                self.view_controller.model.control_video.stop_video()
                self.view_controller.model.control_video.next_frame()
                self.showing_to_ui()

    def onclick_play_pause_video(self):
        """
        This function will control the video player such as playing and pausing the video
        when clicking a button in the user interface
        """
        if self.video_status:
            if self.view_controller.main_ui.btn_play_pause.isChecked():
                self.__timer.start()
                status = "play"
            else:
                status = "pause"
                self.__timer.stop()
            self.view_controller.set_icon.set_icon_video_play_pause(status)

    def change_value_slider(self, value):
        value_max = self.view_controller.main_ui.slider_video.maximum()
        self.view_controller.model.control_video.slider_controller(value, value_max)
        self.showing_to_ui()

    def onclick_stop_video(self):
        if self.video_status:
            self.__timer.stop()
            self.view_controller.model.control_video.stop_video()
            self.showing_to_ui()
            self.view_controller.main_ui.btn_play_pause.setChecked(False)
            self.view_controller.set_icon.set_icon_video_play_pause("begin")

        else:
            self.record = False

    def showing_to_ui(self):
        self.view_controller.show_to_window.showing_video_result()
        # self.set_value_slider_video()
        # self.set_value_timer_video()

    def set_value_slider_video(self):
        value = self.view_controller.main_ui.slider_video.maximum()
        current_position = self.view_controller.model.control_video.get_value_slider_video(value)
        self.view_controller.main_ui.slider_video.blockSignals(True)
        self.view_controller.main_ui.slider_video.setValue(current_position)
        self.view_controller.main_ui.slider_video.blockSignals(False)

    def set_value_timer_video(self):
        total_minute, current_minute, total_second, current_second = self.view_controller.model.control_video.get_time_video()
        self.view_controller.main_ui.label_time_recent.setText("%02d : %02d" % (current_minute, current_second))
        self.view_controller.main_ui.label_time_end.setText("%02d : %02d" % (total_minute, total_second))

    def record_bird_view_video(self):
        if self.video_status:
            if self.view_controller.main_ui.button_record_video.isChecked():
                print("start record")
                self.view_controller.model.control_video.initial_record()
                self.view_controller.model.control_video.record = True

            else:
                print("stop record")
                self.view_controller.model.control_video.record = False
