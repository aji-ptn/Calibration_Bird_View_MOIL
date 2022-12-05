import cv2
import numpy as np
from .merge_original_image import merge_original_image
# from .process_bird_view_4_cam_center_config import merge_image_4_camera_center_config
from .additional_function import remap_image
from threading import Thread
from datetime import datetime


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


class ControllerVideo:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.ret = []
        self.cap = []
        # self.video_frame_anypoint = []
        self.map_x_panorama = []
        self.map_y_panorama = []
        self.map_x_reverse = []
        self.map_y_reverse = []
        self.map_x_anypoint = []
        self.map_y_anypoint = []

        self.total_minute = 0
        self.current_minute = 0
        self.total_second = 0
        self.current_sec = 0
        self.pos_frame = 0
        self.frame_count = 0

        # for record video
        self.start_record = None
        self.record = False

        self.mode_view = "birds_view"

    def initialize_video_data(self):

        self.cap = [None] * self.main_controller.model.total_camera_used
        self.ret = [None] * self.main_controller.model.total_camera_used
        self.main_controller.model.list_anypoint_video = [None] * self.main_controller.model.total_camera_used
        self.main_controller.model.list_frame_video = [None] * self.main_controller.model.total_camera_used

    def running_video(self, i, video_path, multi_thread=False):
        if multi_thread:
            self.cap[i] = VStream(video_path)
            try:
                self.next_frame_thread()
            except:
                pass

        else:
            print(video_path)
            self.cap[i] = cv2.VideoCapture(video_path)
            try:
                # if i == 1:
                #     print(self.cap[1].set(cv2.CAP_PROP_POS_FRAMES, 2))
                # if i == 2:
                #     print(self.cap[2].set(cv2.CAP_PROP_POS_FRAMES, 2))
                # if i == 3:
                #     print(self.cap[3].set(cv2.CAP_PROP_POS_FRAMES, 2))
                    # print("this is second video")
                self.next_frame()
            except:
                pass

    # def update_properties_anypoint(self):
    #     print("here is update maps for all images")
    #     keys = list(self.main_controller.model.properties_image)
    #     for i in range(self.main_controller.model.total_camera_used):
    #         self.map_x_panorama.append(np.load(self.main_controller.model.properties_image[keys[i]]["map_x_panorama"]))
    #         self.map_y_panorama.append(np.load(self.main_controller.model.properties_image[keys[i]]["map_y_panorama"]))
    #         self.map_x_reverse.append(np.load(self.main_controller.model.properties_image[keys[i]]["map_x_reverse"]))
    #         self.map_y_reverse.append(np.load(self.main_controller.model.properties_image[keys[i]]["map_y_reverse"]))
    #         self.map_x_anypoint.append(np.load(self.main_controller.model.properties_image[keys[i]]["map_x_anypoint"]))
    #         self.map_y_anypoint.append(np.load(self.main_controller.model.properties_image[keys[i]]["map_y_anypoint"]))

    def next_frame(self):
        print(self.mode_view)
        for i, cap in enumerate(self.cap):
            self.ret[i], self.main_controller.model.list_frame_video[i] = cap.read()
            if self.mode_view == "birds_view":
                self.main_controller.process_generating_anypoint_video(i)

        if all(self.ret):
            self.__video_duration()
            if self.mode_view == "birds_view":
                _, self.main_controller.model.bird_view_video = self.main_controller.process_birds_view_image("video")
                if self.record:
                    self.start_record.write(self.main_controller.model.bird_view_video)
            elif self.mode_view == "original":
                self.main_controller.model.bird_view_video = merge_original_image(
                    self.main_controller.model.list_frame_video)
            elif self.mode_view == "rear_wide":
                self.main_controller.model.bird_view_video = self.main_controller.anypoint(3)
            elif self.mode_view == "front_wide":
                self.main_controller.model.bird_view_video = self.main_controller.anypoint(0)
            elif self.mode_view == "right_left":
                self.main_controller.model.bird_view_video = self.main_controller.anypoint_right_left()
            else:
                print("Under Development")

    def next_frame_thread(self):
        for i, cap in enumerate(self.cap):
            # self.ret[i], self.main_controller.model.list_frame_video[i] = cap.read()
            self.main_controller.model.list_frame_video[i] = cap.get_frame()
            self.main_controller.process_generating_anypoint_video(i)

        if any(elem is None for elem in self.main_controller.model.list_frame_video) is False:
            # if all(self.main_controller.model.list_frame_video):
            # self.__video_duration()
            self.main_controller.model.union_frame_video = merge_original_image(
                self.main_controller.model.list_frame_video)
            _, self.main_controller.model.bird_view_video = self.main_controller.process_birds_view_image("video")

        # if self.record:
        #     self.start_record.write(self.main_controller.model.bird_view_video)

    def stop_video(self):
        for i, cap in enumerate(self.cap):
            # self.next_frame()
            # print(int(cap.get(cv2.CAP_PROP_FRAME_COUNT) * 0.5))
            # cap.set(cv2.CAP_PROP_POS_MSEC, int(cap.get(cv2.CAP_PROP_FRAME_COUNT) * 0.5))
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.next_frame()

    def __video_duration(self):
        """
            This function is for get time of video
        Returns:

        """
        fps = self.cap[0].get(cv2.CAP_PROP_FPS)
        self.pos_frame = self.cap[0].get(cv2.CAP_PROP_POS_FRAMES)
        self.frame_count = float(self.cap[0].get(cv2.CAP_PROP_FRAME_COUNT))
        duration_sec = int(self.frame_count / fps)

        self.total_minute = int(duration_sec // 60)
        duration_sec %= 60
        self.total_second = duration_sec
        sec_pos = int(self.pos_frame / fps)
        self.current_minute = int(sec_pos // 60)
        sec_pos %= 60
        self.current_second = sec_pos

    def slider_controller(self, value, slider_maximum):
        dst = self.frame_count * value / slider_maximum
        for i in range(self.main_controller.model.total_camera_used):
            self.cap[i].set(cv2.CAP_PROP_POS_FRAMES, dst)
        self.next_frame()

    def get_time_video(self):
        return self.total_minute, self.current_minute, self.total_second, self.current_second

    def get_value_slider_video(self, value):
        current_position = self.pos_frame * (value + 1) / self.frame_count
        return current_position

    # here need to evaluate regarding the delayed updated all frame. #######################33
    def forward_video(self):
        fps = self.cap[0].get(cv2.CAP_PROP_FPS)
        position = self.pos_frame + 5 * fps
        for i in range(self.main_controller.model.total_camera_used):
            self.cap[i].set(cv2.CAP_PROP_POS_FRAMES, position)
        self.next_frame()

    def rewind_video(self):
        fps = self.cap[0].get(cv2.CAP_PROP_FPS)
        position = self.pos_frame - 5 * fps
        for i in range(self.main_controller.model.total_camera_used):
            self.cap[i].set(cv2.CAP_PROP_POS_FRAMES, position)
        self.next_frame()

    def initial_record(self):
        image = self.main_controller.model.bird_view_video.shape
        if image is not None:
            h, w, _ = image.shape
            fourcc = cv2.VideoWriter_fourcc(*'DIVX')
            now = datetime.now()
            self.start_record = cv2.VideoWriter("../saved/Videos_saved/video_round_" + str(now) + "_.avi", fourcc,
                                                15, (w, h))

    def save_bird_view_video(self):
        image = self.main_controller.model.bird_view_video
        if image is not None:
            now = datetime.now()
            cv2.imwrite("../saved/image_saved/image_" + str(now) + "_.jpg", image)
