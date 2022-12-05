
class Model_data:
    def __init__(self):
        super().__init__()
        # properties data of calibration
        self.__total_camera_used = 4
        self.__camera_placement = None
        self.__properties_image = {}

        # image data config
        self.__list_original_image = []
        self.__list_anypoint_image = []
        self.__union_original_image = None
        self.__overlap_image = None
        self.__bird_view_image = None

        # video data config
        self.__list_frame_video = []
        self.__list_anypoint_video = []
        self.__union_frame_video = None
        self.__bird_view_video = None

        self.__zoom_control = 0

        self.__list_image_crop_anypoint = None

    # zoom together
    @property
    def zoom_control(self):
        return self.__zoom_control

    @zoom_control.setter
    def zoom_control(self, value):
        self.__zoom_control = value

    # properties data of calibration #################################################
    @property
    def properties_image(self):
        return self.__properties_image

    @properties_image.setter
    def properties_image(self, value):
        self.__properties_image = value

    @property
    def camera_placement(self):
        return self.__camera_placement

    @camera_placement.setter
    def camera_placement(self, value):
        self.__camera_placement = value

    @property
    def total_camera_used(self):
        return self.__total_camera_used

    @total_camera_used.setter
    def total_camera_used(self, value):
        self.__total_camera_used = value

    # image data config #################################################
    @property
    def list_original_image(self):
        return self.__list_original_image

    @list_original_image.setter
    def list_original_image(self, value):
        self.__list_original_image = value

    @property
    def list_image_crop_anypoint(self):
        return self.__list_image_crop_anypoint

    @list_image_crop_anypoint.setter
    def list_image_crop_anypoint(self, value):
        self.__list_image_crop_anypoint = value

    @property
    def list_anypoint_image(self):
        return self.__list_anypoint_image

    @list_anypoint_image.setter
    def list_anypoint_image(self, value):
        self.__list_anypoint_image = value

    @property
    def union_original_image(self):
        return self.__union_original_image

    @union_original_image.setter
    def union_original_image(self, value):
        self.__union_original_image = value

    @property
    def overlap_image(self):
        return self.__overlap_image

    @overlap_image.setter
    def overlap_image(self, value):
        self.__overlap_image = value

    @property
    def bird_view_image(self):
        return self.__bird_view_image

    @bird_view_image.setter
    def bird_view_image(self, value):
        self.__bird_view_image = value

    # data video start here #############################################
    @property
    def list_frame_video(self):
        return self.__list_frame_video

    @list_frame_video.setter
    def list_frame_video(self, value):
        self.__list_frame_video = value

    @property
    def list_anypoint_video(self):
        return self.__list_anypoint_video

    @list_anypoint_video.setter
    def list_anypoint_video(self, value):
        print("update anypoint _here")
        self.__list_anypoint_video = value

    @property
    def union_frame_video(self):
        return self.__union_frame_video

    @union_frame_video.setter
    def union_frame_video(self, value):
        self.__union_frame_video = value

    @property
    def bird_view_video(self):
        return self.__bird_view_video

    @bird_view_video.setter
    def bird_view_video(self, value):
        self.__bird_view_video = value
