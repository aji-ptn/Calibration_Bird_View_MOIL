import datetime
import os

import cv2
import yaml
from .model_data import Model_data
from .additional_function import *
from .merge_original_image import merge_original_image
from .process_bird_view_4_cam_center_config import merge_image_4_camera_center_config
from .controller_video import ControllerVideo


class MainModel:
    def __init__(self):
        """
        This is object constructor of class MainModel
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
        self.model_data = Model_data()
        self.moildev = []
        self.image_reverse = []
        self.control_video = ControllerVideo(self)
        self.zoom_value = 0
        self.mode_calib = "Normal"
        self.config_file = "../data_config/config.yaml"

    def save_image_calibration(self):
        """
        Save image Calibration
        Returns:

        """
        x = datetime.datetime.now()
        print("saved")
        time = x.strftime("%Y_%m_%d_%H_%M_%S")
        cv2.imwrite("../saved/image_saved/overlap_" + time + ".jpg", self.model_data.overlap_image)
        cv2.imwrite("../saved/image_saved/bird_view_" + time + ".jpg", self.model_data.bird_view_image)
        i = 0
        for undis, pers, in zip(self.model_data.list_anypoint_image,
                                self.model_data.list_image_crop_anypoint):
            cv2.imwrite("../saved/image_saved/undis_point" + str(i) + ".jpg", undis)
            cv2.imwrite("../saved/image_saved/pers_point" + str(i) + ".jpg", pers)
            i += 1

    def initialize_image_data(self):
        """
        Initialization image data parameter
        Returns:

        """
        self.map_x_panorama = [None] * self.model_data.total_camera_used
        self.map_y_panorama = [None] * self.model_data.total_camera_used
        self.map_x_reverse = [None] * self.model_data.total_camera_used
        self.map_y_reverse = [None] * self.model_data.total_camera_used
        self.map_x_anypoint = [None] * self.model_data.total_camera_used
        self.map_y_anypoint = [None] * self.model_data.total_camera_used
        self.model_data.list_alpha = [0] * 2
        self.model_data.list_beta = [0] * 2
        self.model_data.list_reverse_image = [None] * self.model_data.total_camera_used

        self.reverse_image = [None] * self.model_data.total_camera_used

        self.model_data.list_anypoint_image = [None] * self.model_data.total_camera_used

    def list_image_data(self, filepath_image):
        """
        List of image original
        Args:
            filepath_image: path of the images

        Returns:

        """
        print(filepath_image)
        self.model_data.list_original_image.append(read_image(filepath_image))

    def list_moildev_object(self, filepath_parameter):
        """
        Create moildev object
        Args:
            filepath_parameter: path of moildev parameters

        Returns:

        """
        print(filepath_parameter)
        self.moildev.append(connect_to_moildev(filepath_parameter))
        print(self.moildev)

    # #################################### change_mode blending image
    def change_gradient_mode_(self, mode="H"):
        """

        Args:
            mode: blending mode. - H = Horizontal - V = Vertical

        Returns:

        """
        self.gradient_mode = mode

    def update_overlay_and_birds_view_image(self):
        self.model_data.overlap_image, self.model_data.bird_view_image = self.process_birds_view_image()

    def update_union_original_image(self):
        self.model_data.union_original_image = merge_original_image(self.model_data.list_original_image)

    def process_generating_anypoint_image(self, i):
        """
        Process image to anypoint
        """
        keys = list(self.model_data.properties_image)
        rotate = self.model_data.properties_image[keys[i]]["rotate"]
        zoom = self.model_data.properties_image[keys[i]]["zoom"]
        alpha = self.model_data.properties_image[keys[i]]["alpha"]
        beta = self.model_data.properties_image[keys[i]]["beta"]

        original_image = self.model_data.list_original_image[i]

        map_x_anypoint, map_y_anypoint = self.moildev[i].maps_anypoint_car(alpha, beta, rotate, zoom)
        path_map_x_anypoint = "../data_config/map_x_anypoint_image_" + str(i) + ".npy"
        path_map_y_anypoint = "../data_config/map_y_anypoint_image_" + str(i) + ".npy"
        np.save(path_map_x_anypoint, map_x_anypoint)
        np.save(path_map_y_anypoint, map_y_anypoint)
        self.model_data.properties_image[keys[i]]["map_x_anypoint"] = path_map_x_anypoint
        self.model_data.properties_image[keys[i]]["map_y_anypoint"] = path_map_y_anypoint
        self.model_data.list_anypoint_image[i] = remap_image(original_image, map_x_anypoint, map_y_anypoint)

    def update_properties_anypoint(self):
        keys = list(self.model_data.properties_image)
        for i in range(self.model_data.total_camera_used):
            self.map_x_anypoint[i] = (np.load(self.model_data.properties_image[keys[i]]["map_x_anypoint"]))
            self.map_y_anypoint[i] = (np.load(self.model_data.properties_image[keys[i]]["map_y_anypoint"]))

    def process_generating_anypoint_video(self, i):
        """
        This function will be used to generate a reverse image based on map x, and map y in the
        user interface frame
        Args:
            map x, y panorama
            map x, y reverse
            map x, y anypoint
        """
        anypoint_image = remap_image(self.model_data.list_frame_video[i],
                                     self.map_x_anypoint[i],
                                     self.map_y_anypoint[i])

        self.model_data.list_anypoint_video[i] = anypoint_image

    def process_birds_view_image(self, source="Image"):
        if source == "Image":
            image = self.model_data.list_anypoint_image
        elif source == "video":
            image = self.model_data.list_anypoint_video
        #
        # for i, anypoint in enumerate(self.model_data.list_anypoint_image):
        #     cv2.imwrite("anypoint" + str(i) + ".jpg", anypoint)

        keys = list(self.model_data.properties_image)
        shift_x = [self.model_data.properties_image[keys[0]]["shift_x"],
                   self.model_data.properties_image[keys[1]]["shift_x"],
                   self.model_data.properties_image[keys[2]]["shift_x"],
                   self.model_data.properties_image[keys[3]]["shift_x"]]
        shift_y = [self.model_data.properties_image[keys[0]]["shift_y"],
                   self.model_data.properties_image[keys[1]]["shift_y"],
                   self.model_data.properties_image[keys[2]]["shift_y"],
                   self.model_data.properties_image[keys[3]]["shift_y"]]
        image_crop = [self.cropping_anypoint_image(image[0], 0)]

        image_1 = cv2.rotate(image[1], cv2.ROTATE_90_COUNTERCLOCKWISE)
        image_crop.append(self.cropping_anypoint_image(image_1, 1))
        image_2 = cv2.rotate(image[2], cv2.ROTATE_90_CLOCKWISE)
        image_crop.append(self.cropping_anypoint_image(image_2, 2))
        image_3 = cv2.rotate(image[3], cv2.ROTATE_180)
        image_crop.append(self.cropping_anypoint_image(image_3, 3))
        self.model_data.list_image_crop_anypoint = image_crop
        # for i, image in enumerate(image_crop):
        #     cv2.imwrite("image_crop" + str(i) + ".jpg", image)

        if self.mode_calib == "Normal":
            merge_image_canvas, bird_view = merge_image_4_camera_center_config(image_crop,
                                                                               self.model_data.properties_image,
                                                                               shift_x, shift_y,
                                                                               self.gradient_mode, source)

        else:
            merge_image_canvas = None
            bird_view = None
            print("src not enough for further process")

        return merge_image_canvas, bird_view

    def cropping_anypoint_image(self, image, i):
        keys = list(self.model_data.properties_image)
        top = self.model_data.properties_image[keys[i]]["crop_top"]
        bottom = self.model_data.properties_image[keys[i]]["crop_bottom"]
        left = self.model_data.properties_image[keys[i]]["crop_left"]
        right = self.model_data.properties_image[keys[i]]["crop_right"]
        return image[top:image.shape[0] - bottom, left: image.shape[1] - right]

    def save_config_to_file(self):
        """
        This function is for save config file to the directory
        """
        self.save_image_calibration()
        properties_image = self.model_data.properties_image
        with open(self.config_file, "w") as outfile:
            yaml.dump(properties_image, outfile, default_flow_style=False)

    def load_config(self, config_file):
        """
        This function is for load configuration from file from
        Args:
            config_file: file from directory (*.yaml)

        Returns:

        """
        self.config_file = config_file
        with open(config_file, "r") as file:
            data_config = yaml.safe_load(file)
        self.model_data.properties_image = data_config
        self.initialize_image_data()
        self.load_maps()

    def load_maps(self):
        keys = list(self.model_data.properties_image)
        total_camera_used = self.model_data.total_camera_used
        for i in range(total_camera_used):
            self.map_x_anypoint[i] = (np.load(self.model_data.properties_image[keys[i]]["map_x_anypoint"]))
            self.map_y_anypoint[i] = (np.load(self.model_data.properties_image[keys[i]]["map_y_anypoint"]))

    def generate_maps_anypoint_mode_view(self, pitch=0, yaw=0, roll=0, zoom=4):
        self.map_x_anypoint_mode_view, self.map_y_anypoint_mode_view = self.moildev[0].maps_anypoint_car(pitch,
                                                                                                         yaw,
                                                                                                         roll,
                                                                                                         zoom)

        self.control_video.next_frame()

    def anypoint(self, i):
        if self.map_x_anypoint_mode_view is None or self.map_y_anypoint_mode_view is None:
            self.generate_maps_anypoint_mode_view(i)
        anypoint = remap_image(self.model_data.list_frame_video[i], self.map_x_anypoint_mode_view,
                               self.map_y_anypoint_mode_view)
        return anypoint

    def anypoint_right_left(self):
        map_x_anypoint, map_y_anypoint = self.moildev[1].maps_anypoint_car(0, -75, 0, 6)
        anypoint_left = remap_image(self.model_data.list_frame_video[1], map_x_anypoint, map_y_anypoint)

        map_x_anypoint, map_y_anypoint = self.moildev[2].maps_anypoint_car(0, 75, 0, 6)
        anypoint_right = remap_image(self.model_data.list_frame_video[2], map_x_anypoint, map_y_anypoint)
        height = max(anypoint_left.shape[0], anypoint_right.shape[0])
        width = anypoint_left.shape[1] + anypoint_right.shape[1] + 50
        canvas = np.zeros([height, width, 3], dtype=np.uint8)

        canvas[0:anypoint_right.shape[0], 0:0 + anypoint_right.shape[1]] = anypoint_right

        pos_x = anypoint_right.shape[1] + 50
        canvas[0:0 + anypoint_left.shape[0], pos_x:pos_x + anypoint_left.shape[1]] = anypoint_left

        return canvas
