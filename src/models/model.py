
class Model:
    def __init__(self):
        super().__init__()
        # properties data of calibration
        self.__total_camera_used = None
        self.__camera_placement = None
        self.__properties_image = {}

        # data alignment properties
        self.__list_icx = []
        self.__list_icy = []
        self.__list_reverse_alignment = []

        # image data config
        self.__list_original_image = []
        self.__list_original_image_with_fov = [None] * 4
        self.__list_reverse_image = []
        self.__list_anypoint_image = []
        self.__list_crop_anypoint_image_point = []
        self.__list_perspective_image = []
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

    # data alignment properties)
    @property
    def list_icx(self):
        return self.__list_icx

    @list_icx.setter
    def list_icx(self, value):
        self.__list_icx = value

    @property
    def list_icy(self):
        return self.__list_icy

    @list_icy.setter
    def list_icy(self, value):
        self.__list_icy = value

    @property
    def list_reverse_alignment(self):
        return self.__list_reverse_alignment

    @list_reverse_alignment.setter
    def list_reverse_alignment(self, value):
        self.__list_reverse_alignment = value

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
    def list_crop_anypoint_image_point(self):
        return self.__list_crop_anypoint_image_point

    @list_crop_anypoint_image_point.setter
    def list_crop_anypoint_image_point(self, value):
        self.__list_crop_anypoint_image_point = value

    # __list_perspective_image
    @property
    def list_perspective_image(self):
        return self.__list_perspective_image

    @list_perspective_image.setter
    def list_perspective_image(self, value):
        self.__list_perspective_image = value

    @property
    def list_image_crop_anypoint(self):
        return self.__list_image_crop_anypoint

    @list_image_crop_anypoint.setter
    def list_image_crop_anypoint(self, value):
        self.__list_image_crop_anypoint = value

    @property
    def list_original_image_with_fov(self):
        return self.__list_original_image_with_fov

    @list_original_image_with_fov.setter
    def list_original_image_with_fov(self, value):
        self.__list_original_image_with_fov = value

    @property
    def list_reverse_image(self):
        return self.__list_reverse_image

    @list_reverse_image.setter
    def list_reverse_image(self, value):
        self.__list_reverse_image = value

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
