import os
import time
import cv2
import numpy as np
from PyQt5 import QtCore, QtWidgets
from .view_additional_function import select_file
from threading import Thread
from .ui_open_vidcam_controller import OpenVideoCamera


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

        self.timer_dataset = QtCore.QTimer()
        self.timer_dataset.timeout.connect(self.show_dataset)

        self.video_status = True
        self.mode_view = "birds_view"

        self.view_controller.main_ui.button_open_file_video.clicked.connect(self.select_source_video)

        self.view_controller.main_ui.btn_play_pause.clicked.connect(self.onclick_play_pause_video)
        self.view_controller.main_ui.btn_stop_video.clicked.connect(self.onclick_stop_video)
        self.view_controller.main_ui.slider_video.valueChanged.connect(self.change_value_slider)
        self.view_controller.main_ui.btn_skip_video.clicked.connect(
            self.view_controller.controller.control_video.forward_video)
        self.view_controller.main_ui.btn_prev_video.clicked.connect(
            self.view_controller.controller.control_video.rewind_video)

        # self.view_controller.main_ui.button_streaming_camera.clicked.connect(self.onclick_create_dataset)

        self.view_controller.main_ui.button_save_frame.clicked.connect(self.save_dataset_image)
        self.view_controller.main_ui.button_update_properties.clicked.connect(self.record_bird_view_video)

        self.view_controller.main_ui.button_change_mode_view.clicked.connect(self.change_mode_view_button)
        self.view_controller.main_ui.button_mode_view_original.clicked.connect(lambda: self.change_mode_view("original"))
        self.view_controller.main_ui.button_front_wide_view.clicked.connect(lambda: self.change_mode_view("front_wide"))
        self.view_controller.main_ui.button_right_left_view.clicked.connect(lambda: self.change_mode_view("right_left"))
        self.view_controller.main_ui.button_rear_wide_view.clicked.connect(lambda: self.change_mode_view("rear_wide"))

    def show_choose_video_source(self):
        windowDevice = QtWidgets.QDialog()
        ui_select_cam = OpenVideoCamera(windowDevice, self)
        windowDevice.exec_()

    def onclick_create_dataset(self):
        self.video_status = False
        self.record = False
        self.cam1 = VStream("http://10.42.0.170:8000/stream.mjpg")  # cam 1 109 front
        self.cam2 = VStream("http://10.42.0.109:8000/stream.mjpg")  # cam 2 170 right
        self.cam3 = VStream("http://10.42.0.183:8000/stream.mjpg")  # cam 3 183 left
        self.cam4 = VStream("http://10.42.0.251:8000/stream.mjpg")  # cam 4 251 rear
        time.sleep(5)

    def show_dataset(self):
        try:
            myFrame1 = self.cam1.get_frame()
            myFrame2 = self.cam2.get_frame()
            myFrame3 = self.cam3.get_frame()
            myFrame4 = self.cam4.get_frame()

            if self.record:
                print("record")
                self.out1.write(self.cam1.get_frame())
                self.out2.write(self.cam2.get_frame())
                self.out3.write(self.cam3.get_frame())
                self.out4.write(self.cam4.get_frame())

            myFrameH1 = np.hstack((myFrame1, myFrame2))
            myFrameH2 = np.hstack((myFrame3, myFrame4))
            myFrame = np.vstack((myFrameH1, myFrameH2))
            myFrame = cv2.resize(myFrame, (640, 480), cv2.INTER_AREA)
            cv2.imshow("video", myFrame)

        except:
            print("not from available")

    def run_dataset_timer(self):
        self.timer_dataset.start()

    def save_dataset_image(self):
        self.view_controller.controller.control_video.save_bird_view_video()
        # cv2.imwrite("../dataset/images/image1.jpg", self.cam1.get_frame())
        # cv2.imwrite("../dataset/images/image1.jpg", self.cam1.get_frame())
        # cv2.imwrite("../dataset/images/image2.jpg", self.cam2.get_frame())
        # cv2.imwrite("../dataset/images/image3.jpg", self.cam3.get_frame())
        # cv2.imwrite("../dataset/images/image4.jpg", self.cam4.get_frame())

    def set_record(self):
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out1 = cv2.VideoWriter("../dataset/video/video_1.avi", self.fourcc, 10, (2592, 1944))
        self.out2 = cv2.VideoWriter('../dataset/video/video_2.avi', self.fourcc, 10, (2592, 1944))
        self.out3 = cv2.VideoWriter('../dataset/video/video_3.avi', self.fourcc, 10, (2592, 1944))
        self.out4 = cv2.VideoWriter('../dataset/video/video_4.avi', self.fourcc, 10, (2592, 1944))

    # def select_stream_video(self):
    #     self.view_controller.controller.control_video.initialize_video_data()
    #     list_cam_stream = ["http://10.42.0.170:8000/stream.mjpg",
    #                        "http://10.42.0.109:8000/stream.mjpg",
    #                        "http://10.42.0.183:8000/stream.mjpg",
    #                        "http://10.42.0.251:8000/stream.mjpg"]
    #
    #     for i in range(self.view_controller.model.total_camera_used):
    #         # filepath_video = select_file(None, "Select video", "", "*.avi *.mp4")
    #         # if filepath_video:
    #         self.view_controller.controller.control_video.running_video(i, list_cam_stream[i], False)
    #         # else:
    #         #     break
    #
    #     self.view_controller.controller.update_properties_anypoint()
    #     s0elf.showing_to_ui()

    def select_source_video(self):
        self.video_status = True
        if self.view_controller.model.total_camera_used is not None:
            self.view_controller.controller.control_video.initialize_video_data()
            # list_cam_stream = ["../data_use/video/12/video_3.avi",
            #                    "../data_use/video/12/video_2.avi",
            #                    "../data_use/video/12/video_4.avi",
            #                    "../data_use/video/12/video_1.avi"]
            list_cam_stream = ["../data_use/video/sequence_video/7/video_3 1668069965.1640372_.avi",
                               "../data_use/video/sequence_video/7/video_2 1668069965.1640372_.avi",
                               "../data_use/video/sequence_video/7/video_4 1668069965.1640372_.avi",
                               "../data_use/video/sequence_video/7/video_1 1668069965.1640372_.avi"]

            # list_cam_stream = ["/home/anto/Documents/create-dataset-birds-view/Videos/video_0.avi",
            #                    "/home/anto/Documents/create-dataset-birds-view/Videos/video_1.avi",
            #                    "/home/anto/Documents/create-dataset-birds-view/Videos/video_2.avi",
            #                    "/home/anto/Documents/create-dataset-birds-view/Videos/video_3.avi"]

            # list_cam_stream = ['http://10.42.0.31:8000/stream.mjpg',
            #                 'http://10.42.0.151:8000/stream.mjpg',
            #                 'http://10.42.0.109:8000/stream.mjpg',
            #                 'http://10.42.0.251:8000/stream.mjpg']

            for i in range(self.view_controller.model.total_camera_used):
                self.view_controller.controller.control_video.running_video(i, list_cam_stream[i])

            self.view_controller.controller.update_properties_anypoint()
            # self.showing_to_ui()
            self.view_controller.controller.control_video.stop_video()
            self.view_controller.controller.control_video.next_frame()
            self.showing_to_ui()

    def onclick_play_pause_video(self):
        """
        This function will control the video player such as playing and pausing the video
        when clicking a button in the user interface
        """
        if self.video_status:
            if self.view_controller.main_ui.btn_play_pause.isChecked():
                # self.view_controller.controller.control_video.update_properties_anypoint()
                self.__timer.start()
                status = "play"
            else:
                status = "pause"
                self.__timer.stop()
            self.view_controller.set_icon.set_icon_video_play_pause(status)
        else:
            self.timer_dataset.start()

    def change_value_slider(self, value):
        value_max = self.view_controller.main_ui.slider_video.maximum()
        self.view_controller.controller.control_video.slider_controller(value, value_max)
        self.showing_to_ui()

    def onclick_stop_video(self):
        if self.video_status:
            self.__timer.stop()
            self.view_controller.controller.control_video.stop_video()
            self.showing_to_ui()
            self.view_controller.main_ui.btn_play_pause.setChecked(False)
            self.view_controller.set_icon.set_icon_video_play_pause("begin")

        else:
            self.timer_dataset.stop()
            self.record = False
            # self.cam1.capture.release()
            # self.cam2.capture.release()
            # self.cam3.capture.release()
            # self.cam4.capture.release()
            # cv2.destroyAllWindows()

    def change_mode_view(self, command):
        self.view_controller.additional_mode_view.button_addition_mode.hide()
        self.view_controller.additional_mode_view.frame_pitch_yaw_roll.hide()
        if command == "front_wide" or command == "rear_wide":
            self.view_controller.additional_mode_view.button_addition_mode.show()
        self.view_controller.controller.control_video.mode_view = command
        self.showing_to_ui()

    def change_mode_view_button(self):
        self.view_controller.additional_mode_view.button_addition_mode.hide()
        self.view_controller.additional_mode_view.frame_pitch_yaw_roll.hide()
        if self.view_controller.main_ui.button_change_mode_view.isChecked():
            self.view_controller.controller.control_video.mode_view = "original"
        else:
            self.view_controller.controller.control_video.mode_view = "birds_view"
        self.showing_to_ui()

    def showing_to_ui(self):
        self.view_controller.show_to_window.showing_video_result()
        # self.set_value_slider_video()
        # self.set_value_timer_video()

    def set_value_slider_video(self):
        value = self.view_controller.main_ui.slider_video.maximum()
        current_position = self.view_controller.controller.control_video.get_value_slider_video(value)
        self.view_controller.main_ui.slider_video.blockSignals(True)
        self.view_controller.main_ui.slider_video.setValue(current_position)
        self.view_controller.main_ui.slider_video.blockSignals(False)

    def set_value_timer_video(self):
        total_minute, current_minute, total_second, current_second = self.view_controller.controller.control_video.get_time_video()
        self.view_controller.main_ui.label_time_recent.setText("%02d : %02d" % (current_minute, current_second))
        self.view_controller.main_ui.label_time_end.setText("%02d : %02d" % (total_minute, total_second))

    def record_bird_view_video(self):
        if self.video_status:
            if self.view_controller.main_ui.button_update_properties.isChecked():
                print("start record")
                self.view_controller.controller.control_video.initial_record()
                self.view_controller.controller.control_video.record = True

            else:
                print("stop record")
                self.view_controller.controller.control_video.record = False

        else:
            self.record = True
            h = 1944
            w = 2592
            self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.out1 = cv2.VideoWriter("../dataset/video/video_1.avi", self.fourcc, 10, (w, h))
            self.out2 = cv2.VideoWriter('../dataset/video/video_2.avi', self.fourcc, 10, (w, h))
            self.out3 = cv2.VideoWriter('../dataset/video/video_3.avi', self.fourcc, 10, (w, h))
            self.out4 = cv2.VideoWriter('../dataset/video/video_4.avi', self.fourcc, 10, (w, h))
