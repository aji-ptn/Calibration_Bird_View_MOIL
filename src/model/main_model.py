import datetime
import os

import cv2
import yaml
from .model_data import Model_data
from .additional_function import *
from .merge_original_image import merge_original_image
from .process_bird_view_4_cam_center_clicked import merge_image_4_camera_center_clicked
from .process_bird_view_4_cam_center_perspective import merge_image_4_camera_center_perspective
from .process_bird_view_4_cam_center_config import merge_image_4_camera_center_config
from .process_bird_view_4_cam_corner_config import merge_image_4_camera_corner_config
from .process_bird_view_6_cam_corner import merge_image_6_camera_corner_config
from .controller_video import ControllerVideo
from .perspective_process import PerspectiveView


class MainModel:
    def __init__(self):
        """

        """
        super().__init__()

        self.map_y_anypoint_mode_view = None
        self.map_x_anypoint_mode_view = None
        self.reverse_image = []

        self.map_y_anypoint = None
        self.map_x_anypoint = None
        self.map_y_reverse = None
        self.map_y_panorama = None
        self.map_x_reverse = None
        self.map_x_panorama = None
        self.gradient_mode = "H"  # "V" "D"
        self.show_fov = False
        self.model = Model_data()
        self.moildev = []
        self.image_reverse = []
        self.control_video = ControllerVideo(self)
        self.control_perspective = PerspectiveView(self)
        self.zoom_value = 0
        self.mode_calib = "Normal"
        self.config_file = "../data_config/config.yaml"

    def fill_image_crop_anypoint_point(self):
        self.model.list_crop_anypoint_image_point = []
        for i, image in enumerate(self.model.list_anypoint_image):
            if i == 1:
                image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
            elif i == 2:
                image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            elif i == 3:
                image = cv2.rotate(image, cv2.ROTATE_180)
            self.model.list_crop_anypoint_image_point.append(image.copy())

    def save_image_calibration(self):
        x = datetime.datetime.now()
        print("saved")
        time = x.strftime("%Y_%m_%d_%H_%M_%S")
        cv2.imwrite("../saved/image_saved/overlap_" + time + ".jpg", self.model.overlap_image)
        cv2.imwrite("../saved/image_saved/bird_view_" + time + ".jpg", self.model.bird_view_image)

    def change_slider_zoom(self, value):
        self.model.zoom_control = value

    def change_zoom_plus(self):
        value = int(self.model.zoom_control)
        if value < 30:
            self.model.zoom_control = value + 1

    def change_zoom_minus(self):
        value = int(self.model.zoom_control)
        if value > 0:
            self.model.zoom_control = value - 1

    def initialize_image_data(self):
        self.map_x_panorama = [None] * self.model.total_camera_used
        self.map_y_panorama = [None] * self.model.total_camera_used
        self.map_x_reverse = [None] * self.model.total_camera_used
        self.map_y_reverse = [None] * self.model.total_camera_used
        self.map_x_anypoint = [None] * self.model.total_camera_used
        self.map_y_anypoint = [None] * self.model.total_camera_used
        self.model.list_icx = [0] * 2
        self.model.list_icy = [0] * 2
        self.model.list_reverse_image = [None] * self.model.total_camera_used

        self.reverse_image = [None] * self.model.total_camera_used

        self.model.list_anypoint_image = [None] * self.model.total_camera_used

    def list_image_data(self, filepath_image):
        """

        Args:
            filepath_image:

        Returns:

        """
        print(filepath_image)
        self.model.list_original_image.append(read_image(filepath_image))

    def list_moildev_object(self, filepath_parameter):
        """

        Args:
            filepath_parameter:

        Returns:

        """
        print(filepath_parameter)
        self.moildev.append(connect_to_moildev(filepath_parameter))
        print(self.moildev)

    # #################################### change_mode blending image
    def change_gradient_mode(self, mode="H"):
        """

        Args:
            mode (): blending mode. - H = Horizontal - V = Vertical

        Returns:

        """
        self.gradient_mode = mode

    def show_fov_image(self, mode=False):
        self.show_fov = mode

    def update_overlay_and_birds_view_image(self):
        self.model.overlap_image, self.model.bird_view_image = self.process_birds_view_image()

    def update_union_original_image(self):
        self.model.union_original_image = merge_original_image(self.model.list_original_image)

    # def generate_reverse_alignment(self, i, image_number):
    #     icx = self.model.list_icx[i]
    #     icy = self.model.list_icy[i]
    #     alpha, beta = self.moildev[image_number].get_alpha_beta(icx, icy)
    #     map_x_panorama, map_y_panorama = self.moildev[image_number].maps_panorama_rotation(110, alpha, beta)
    #     panorama_image = remap_image(self.model.list_original_image[image_number], map_x_panorama, map_y_panorama)
    #     map_x_reverse, map_y_reverse = self.moildev[image_number].maps_reverse(110, beta)
    #     self.model.list_reverse_alignment[i] = remap_image(panorama_image, map_x_reverse, map_y_reverse)

    # def process_generating_reverse_image(self, i):
    #     """
    #     Process image to reverse
    #     """
    #     keys = list(self.model.properties_image)
    #     icx = self.model.properties_image[keys[i]]["icx"]
    #     icy = self.model.properties_image[keys[i]]["icy"]
    #     alpha, beta = self.moildev[i].get_alpha_beta(icx, icy)
    #     map_x_panorama, map_y_panorama = self.moildev[i].maps_panorama_rotation(110, alpha, beta)
    #     path_map_x_panorama = "../data_config/map_x_panorama_image_" + str(i) + ".npy"
    #     path_map_y_panorama = "../data_config/map_y_panorama_image_" + str(i) + ".npy"
    #
    #     np.save(path_map_x_panorama, map_x_panorama)
    #     np.save(path_map_y_panorama, map_y_panorama)
    #     self.model.properties_image[keys[i]]["map_x_panorama"] = path_map_x_panorama
    #     self.model.properties_image[keys[i]]["map_y_panorama"] = path_map_y_panorama
    #
    #     if self.show_fov:
    #         if any(elem is None for elem in self.model.list_original_image_with_fov):
    #             self.create_line_fov()
    #         panorama_image = remap_image(self.model.list_original_image_with_fov[i], map_x_panorama, map_y_panorama)
    #     else:
    #         panorama_image = remap_image(self.model.list_original_image[i], map_x_panorama, map_y_panorama)
    #     map_x_reverse, map_y_reverse = self.moildev[i].maps_reverse(110, beta)
    #
    #     self.reverse_image[i] = remap_image(panorama_image, map_x_reverse, map_y_reverse)
    #     if self.model.list_reverse_image[i] is None:
    #         self.model.list_reverse_image[i] = self.reverse_image[i]
    #
    #     path_map_x_reverse = "../data_config/map_x_reverse_image_" + str(i) + ".npy"
    #     path_map_y_reverse = "../data_config/map_y_reverse_image_" + str(i) + ".npy"
    #     np.save(path_map_x_reverse, map_x_reverse)
    #     np.save(path_map_y_reverse, map_y_reverse)
    #
    #     self.model.properties_image[keys[i]]["map_x_reverse"] = path_map_x_reverse
    #     self.model.properties_image[keys[i]]["map_y_reverse"] = path_map_y_reverse
    #     self.process_generating_anypoint_image(i)

    def process_generating_anypoint_image(self, i):
        """
        Process image to anypoint
        """
        keys = list(self.model.properties_image)
        rotate = self.model.properties_image[keys[i]]["rotate"]
        zoom = self.model.properties_image[keys[i]]["zoom"]
        alpha = self.model.properties_image[keys[i]]["icx"]
        beta = self.model.properties_image[keys[i]]["icy"]

        original_image = self.model.list_original_image[i]

        map_x_anypoint, map_y_anypoint = self.moildev[i].maps_anypoint_car(alpha, beta, rotate, zoom)
        path_map_x_anypoint = "../data_config/map_x_anypoint_image_" + str(i) + ".npy"
        path_map_y_anypoint = "../data_config/map_y_anypoint_image_" + str(i) + ".npy"
        np.save(path_map_x_anypoint, map_x_anypoint)
        np.save(path_map_y_anypoint, map_y_anypoint)
        self.model.properties_image[keys[i]]["map_x_anypoint"] = path_map_x_anypoint
        self.model.properties_image[keys[i]]["map_y_anypoint"] = path_map_y_anypoint
        self.model.list_anypoint_image[i] = remap_image(original_image, map_x_anypoint, map_y_anypoint)

    def reverseForAlignment(self, alpha, beta, i):
        map_x_panorama, map_y_panorama = self.moildev[i].maps_panorama_rotation(110, alpha[i], beta[i])
        panorama_image = remap_image(self.model.list_original_image[i], map_x_panorama, map_y_panorama)
        map_x_reverse, map_y_reverse = self.moildev[i].maps_reverse(110, beta[i])
        self.model.list_reverse_image[i] = remap_image(panorama_image, map_x_reverse, map_y_reverse)

    def update_properties_anypoint(self):
        keys = list(self.model.properties_image)
        for i in range(self.model.total_camera_used):
            self.map_x_anypoint[i] = (np.load(self.model.properties_image[keys[i]]["map_x_anypoint"]))
            self.map_y_anypoint[i] = (np.load(self.model.properties_image[keys[i]]["map_y_anypoint"]))

    def process_generating_anypoint_video(self, i):
        """
        This function will be used to generate a reverse image based on map x, and map y in the
        user interface frame
        Args:
            map x, y panorama
            map x, y reverse
            map x, y anypoint
        """
        anypoint_image = remap_image(self.model.list_frame_video[i],
                                     self.map_x_anypoint[i],
                                     self.map_y_anypoint[i])

        self.model.list_anypoint_video[i] = anypoint_image

    def create_line_fov(self):
        for i in range(self.model.total_camera_used):
            maps_x, maps_y = self.moildev[i].maps_panorama(10, 90)
            image = draw_polygon_fov(self.model.list_original_image[i].copy(), maps_x, maps_y)
            self.model.list_original_image_with_fov[i] = image

    def process_birds_view_image(self, source="Image"):
        if source == "Image":
            image = self.model.list_anypoint_image
        elif source == "video":
            image = self.model.list_anypoint_video
        else:
            image = self.model.list_crop_anypoint_image_point

        for i, anypoint in enumerate(self.model.list_anypoint_image):
            cv2.imwrite("anypoint" + str(i) + ".jpg", anypoint)

        if self.mode_calib == "Point":
            image_crop = self.control_perspective.process_perspective(image)
            merge_image_canvas, bird_view = merge_image_4_camera_center_perspective(image_crop,
                                                                                    self.control_perspective.data_dst,
                                                                                    self.model.properties_image,
                                                                                    self.gradient_mode)

        elif self.mode_calib == "Normal":
            keys = list(self.model.properties_image)
            shift_x = [self.model.properties_image[keys[0]]["shift_x"],
                       self.model.properties_image[keys[1]]["shift_x"],
                       self.model.properties_image[keys[2]]["shift_x"],
                       self.model.properties_image[keys[3]]["shift_x"]]
            shift_y = [self.model.properties_image[keys[0]]["shift_y"],
                       self.model.properties_image[keys[1]]["shift_y"],
                       self.model.properties_image[keys[2]]["shift_y"],
                       self.model.properties_image[keys[3]]["shift_y"]]
            image_crop = [self.cropping_anypoint_image(image[0], 0)]

            if self.model.total_camera_used == 4:
                if self.model.camera_placement == "center":
                    image_1 = cv2.rotate(image[1], cv2.ROTATE_90_COUNTERCLOCKWISE)
                    image_crop.append(self.cropping_anypoint_image(image_1, 1))
                    image_2 = cv2.rotate(image[2], cv2.ROTATE_90_CLOCKWISE)
                    image_crop.append(self.cropping_anypoint_image(image_2, 2))
                    image_3 = cv2.rotate(image[3], cv2.ROTATE_180)
                    image_crop.append(self.cropping_anypoint_image(image_3, 3))
                    self.model.list_image_crop_anypoint = image_crop
                    for i, image in enumerate(image_crop):
                        cv2.imwrite("image_crop" + str(i) + ".jpg", image)

                    if self.mode_calib == "Normal":
                        merge_image_canvas, bird_view = merge_image_4_camera_center_config(image_crop,
                                                                                           self.model.properties_image,
                                                                                           shift_x, shift_y,
                                                                                           self.gradient_mode, source)
                    elif self.mode_calib == "Point":
                        merge_image_canvas, bird_view = merge_image_4_camera_center_clicked(image_crop,
                                                                                            self.model.properties_image,
                                                                                            self.gradient_mode)
                    # except:
                    #     merge_image_canvas = None
                    #     bird_view = None

                else:
                    # corner config 4 camera merge image algorithm
                    image_crop.append(self.cropping_anypoint_image(image[1], 1))
                    image_crop.append(
                        self.cropping_anypoint_image(cv2.rotate(image[2], cv2.ROTATE_180), 2))
                    image_crop.append(
                        self.cropping_anypoint_image(cv2.rotate(image[3], cv2.ROTATE_180), 3))

                    merge_image_canvas, bird_view = merge_image_4_camera_corner_config(image_crop,
                                                                                       shift_x, shift_y)

            elif self.model.total_camera_used == 6:
                shift_x.append(self.model.properties_image[keys[4]]["shift_x"])
                shift_x.append(self.model.properties_image[keys[5]]["shift_x"])
                shift_y.append(self.model.properties_image[keys[4]]["shift_y"])
                shift_y.append(self.model.properties_image[keys[5]]["shift_y"])

                if self.model.camera_placement == "center":
                    image_1 = image[1]
                    image_1 = cv2.rotate(image_1, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    image_2 = image[2]
                    image_2 = cv2.rotate(image_2, cv2.ROTATE_90_CLOCKWISE)
                    image_3 = image[3]
                    image_3 = cv2.rotate(image_3, cv2.ROTATE_180)
                    image_4 = image[4]
                    image_5 = image[5]

                    merge_image_canvas = None
                    bird_view = None
                else:
                    """
                    Corner configuration for 6 cameras used
                    """
                    image_crop.append(self.cropping_anypoint_image(image[1], 1))
                    image_crop.append(self.cropping_anypoint_image(cv2.rotate(image[2],
                                                                              cv2.ROTATE_90_COUNTERCLOCKWISE), 2))
                    image_crop.append(self.cropping_anypoint_image(cv2.rotate(image[3],
                                                                              cv2.ROTATE_90_CLOCKWISE), 3))
                    image_crop.append(self.cropping_anypoint_image(cv2.rotate(image[4], cv2.ROTATE_180), 4))
                    image_crop.append(self.cropping_anypoint_image(cv2.rotate(image[5], cv2.ROTATE_180), 5))

                    merge_image_canvas, bird_view = merge_image_6_camera_corner_config(image_crop, shift_x, shift_y)

        else:
            merge_image_canvas = None
            bird_view = None
            print("src not enough for further process")

        return merge_image_canvas, bird_view

    def cropping_anypoint_image(self, image, i):
        keys = list(self.model.properties_image)
        top = self.model.properties_image[keys[i]]["crop_top"]
        bottom = self.model.properties_image[keys[i]]["crop_bottom"]
        left = self.model.properties_image[keys[i]]["crop_left"]
        right = self.model.properties_image[keys[i]]["crop_right"]
        return image[top:image.shape[0] - bottom, left: image.shape[1] - right]

    def save_config_to_file(self):
        self.save_image_calibration()
        properties_image = self.model.properties_image
        properties_image["camera_used"] = self.model.total_camera_used
        properties_image["camera_placement"] = self.model.camera_placement
        # try:
        #     del properties_image["Image_1"]["icx"]
        #     del properties_image["Image_1"]["icy"]
        #     del properties_image["Image_1"]["zoom"]
        #     del properties_image["Image_2"]["icx"]
        #     del properties_image["Image_2"]["icy"]
        #     del properties_image["Image_2"]["zoom"]
        #     del properties_image["Image_3"]["icx"]
        #     del properties_image["Image_3"]["icy"]
        #     del properties_image["Image_3"]["zoom"]
        #     del properties_image["Image_4"]["icx"]
        #     del properties_image["Image_4"]["icy"]
        #     del properties_image["Image_4"]["zoom"]
        #     del properties_image["Image_5"]["icx"]
        #     del properties_image["Image_5"]["icy"]
        #     del properties_image["Image_5"]["zoom"]
        #     del properties_image["Image_6"]["icx"]
        #     del properties_image["Image_6"]["icy"]
        #     del properties_image["Image_6"]["zoom"]
        #
        # except:
        #     pass
        # with open("../data_config/config.yaml", "w") as outfile:
        with open(self.config_file, "w") as outfile:
            yaml.dump(properties_image, outfile, default_flow_style=False)

    def load_config(self, config_file):
        self.config_file = config_file
        with open(config_file, "r") as file:
            data_config = yaml.safe_load(file)

        self.model.total_camera_used = data_config["camera_used"]
        self.model.camera_placement = data_config["camera_placement"]
        self.model.properties_image = data_config
        self.initialize_image_data()
        self.load_maps()

    def load_maps(self):
        keys = list(self.model.properties_image)
        total_camera_used = self.model.total_camera_used
        for i in range(total_camera_used):
            # self.map_x_panorama[i] = (np.load(self.model.properties_image[keys[i]]["map_x_panorama"]))
            # self.map_y_panorama[i] = (np.load(self.model.properties_image[keys[i]]["map_y_panorama"]))
            # self.map_x_reverse[i] = (np.load(self.model.properties_image[keys[i]]["map_x_reverse"]))
            # self.map_y_reverse[i] = (np.load(self.model.properties_image[keys[i]]["map_y_reverse"]))
            self.map_x_anypoint[i] = (np.load(self.model.properties_image[keys[i]]["map_x_anypoint"]))
            self.map_y_anypoint[i] = (np.load(self.model.properties_image[keys[i]]["map_y_anypoint"]))

    def generate_maps_anypoint_mode_view(self, pitch=0, yaw=0, roll=0, zoom=4):
        self.map_x_anypoint_mode_view, self.map_y_anypoint_mode_view = self.moildev[0].maps_anypoint_car(pitch,
                                                                                                         yaw,
                                                                                                         roll,
                                                                                                         zoom)

        self.control_video.next_frame()

    def anypoint(self, i):
        if self.map_x_anypoint_mode_view is None or self.map_y_anypoint_mode_view is None:
            self.generate_maps_anypoint_mode_view(i)
        anypoint = remap_image(self.model.list_frame_video[i], self.map_x_anypoint_mode_view,
                               self.map_y_anypoint_mode_view)
        return anypoint

    def anypoint_right_left(self):
        map_x_anypoint, map_y_anypoint = self.moildev[1].maps_anypoint_car(0, -75, 0, 6)
        anypoint_left = remap_image(self.model.list_frame_video[1], map_x_anypoint, map_y_anypoint)

        map_x_anypoint, map_y_anypoint = self.moildev[2].maps_anypoint_car(0, 75, 0, 6)
        anypoint_right = remap_image(self.model.list_frame_video[2], map_x_anypoint, map_y_anypoint)
        height = max(anypoint_left.shape[0], anypoint_right.shape[0])
        width = anypoint_left.shape[1] + anypoint_right.shape[1] + 50
        canvas = np.zeros([height, width, 3], dtype=np.uint8)

        canvas[0:anypoint_right.shape[0], 0:0 + anypoint_right.shape[1]] = anypoint_right

        pos_x = anypoint_right.shape[1] + 50
        canvas[0:0 + anypoint_left.shape[0], pos_x:pos_x + anypoint_left.shape[1]] = anypoint_left

        return canvas
