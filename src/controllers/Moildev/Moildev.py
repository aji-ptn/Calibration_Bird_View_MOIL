import math
import json
import cv2
import numpy as np
from . import MoilCV
import warnings


class Moildev(object):
    def __init__(self, file_camera_parameter=None, camera_type=None, **kwarg):
        """
        This is the initial configuration that you need to provide the camera parameter. The camera parameter is the
        result from calibration camera by MOIL laboratory. before the successive functions can work correctly,
        configuration is necessary in the beginning of program.
        Args:
            file_camera_parameter (): *.json file
            camera_type = the name of the camera type used (use if yore pass the parameter using *.json file)
            cameraName = the name of the camera used
            cameraFov = camera field of view (FOV)
            sensor_width = size of sensor width
            sensor_height = size of sensor height
            Icx = center image in x-axis
            Icy = center image in y-axis
            ratio = the value of the ratio image
            imageWidth = the size of width image
            imageHeight = the size of height image
            calibrationRatio = the value of calibration ratio
            parameter0 .. parameter5= intrinsic fisheye camera parameter get from calibration

        for more detail, please reference https://github.com/MoilOrg/moildev
        """
        super(Moildev, self).__init__()
        self.__alpha_to_rho_table = []
        self.__rho_to_alpha_table = []

        self.__camera_name = None
        self.__camera_fov = None
        self.__sensor_width = None
        self.__sensor_height = None
        self.__Icx = None
        self.__Icy = None
        self.__ratio = None
        self.__image_width = None
        self.__image_height = None
        self.__calibration_ratio = None
        self.__parameter_0 = None
        self.__parameter_1 = None
        self.__parameter_2 = None
        self.__parameter_3 = None
        self.__parameter_4 = None
        self.__parameter_5 = None

        if file_camera_parameter is None:
            if kwarg == {}:
                print("Pass the argument with camera parameter file with json extension (*.json) "
                      "Or Given list of Parameter,\nsee detail documentation here https://github.com/MoilOrg/moildev")

            else:
                for key, value in kwarg.items():
                    if key == "camera_name":
                        self.__camera_name = value
                    elif key == "camera_fov":
                        self.__camera_fov = value
                    elif key == "sensor_width":
                        self.__sensor_width = value
                    elif key == "sensor_height":
                        self.__sensor_height = value
                    elif key == "icx":
                        self.__Icx = value
                    elif key == "icy":
                        self.__Icy = value
                    elif key == "ratio":
                        self.__ratio = value
                    elif key == "image_width":
                        self.__image_width = value
                    elif key == "image_height":
                        self.__image_height = value
                    elif key == "calibration_ratio":
                        self.__calibration_ratio = value
                    elif key == "parameter_0":
                        self.__parameter_0 = value
                    elif key == "parameter_1":
                        self.__parameter_1 = value
                    elif key == "parameter_2":
                        self.__parameter_2 = value
                    elif key == "parameter_3":
                        self.__parameter_3 = value
                    elif key == "parameter_4":
                        self.__parameter_4 = value
                    elif key == "parameter_5":
                        self.__parameter_5 = value

                if self.__camera_name is None or \
                        self.__camera_fov is None or \
                        self.__sensor_width is None or \
                        self.__sensor_height is None or \
                        self.__Icx is None or \
                        self.__Icy is None or \
                        self.__ratio is None or \
                        self.__image_width is None or \
                        self.__image_height is None or \
                        self.__calibration_ratio is None or \
                        self.__parameter_0 is None or \
                        self.__parameter_1 is None or \
                        self.__parameter_2 is None or \
                        self.__parameter_3 is None or \
                        self.__parameter_4 is None or \
                        self.__parameter_5 is None:
                    warnings.warn("You're not passing the complete parameter. please refer to the documentation here "
                                  "https://github.com/MoilOrg/moildev ")

                else:
                    self.__init_alpha_rho_table()
                    self.__import_moildev()
        else:
            self.__setCamera_parameter(file_camera_parameter, camera_type)
            if self.__camera_name is not None:
                self.__init_alpha_rho_table()
                self.__import_moildev()

    def __setCamera_parameter(self, parameter, cameraType):
        """
        Set up the configuration of the camera parameter
        Args:
            parameter (): the *.json file
            cameraType (): type of the camera

        Returns:
            None
        """
        with open(parameter) as f:
            data = json.load(f)
            if cameraType in data.keys():
                self.__camera_name = data[cameraType]["cameraName"]
                self.__camera_fov = data[cameraType]["cameraFov"] if "cameraFov" in data[cameraType].keys() else 220
                self.__sensor_width = data[cameraType]['cameraSensorWidth']
                self.__sensor_height = data[cameraType]['cameraSensorHeight']
                self.__Icx = data[cameraType]['iCx']
                self.__Icy = data[cameraType]['iCy']
                self.__ratio = data[cameraType]['ratio']
                self.__image_width = data[cameraType]['imageWidth']
                self.__image_height = data[cameraType]['imageHeight']
                self.__calibration_ratio = data[cameraType]['calibrationRatio']
                self.__parameter_0 = data[cameraType]['parameter0']
                self.__parameter_1 = data[cameraType]['parameter1']
                self.__parameter_2 = data[cameraType]['parameter2']
                self.__parameter_3 = data[cameraType]['parameter3']
                self.__parameter_4 = data[cameraType]['parameter4']
                self.__parameter_5 = data[cameraType]['parameter5']

            else:
                if "cameraName" in data.keys() and cameraType is None:
                    with open(parameter) as file:
                        data = json.load(file)
                        self.__camera_name = data["cameraName"]
                        self.__camera_fov = data["cameraFov"] if "cameraFov" in data.keys() else 220
                        self.__sensor_width = data['cameraSensorWidth']
                        self.__sensor_height = data['cameraSensorHeight']
                        self.__Icx = data['iCx']
                        self.__Icy = data['iCy']
                        self.__ratio = data['ratio']
                        self.__image_width = data['imageWidth']
                        self.__image_height = data['imageHeight']
                        self.__calibration_ratio = data['calibrationRatio']
                        self.__parameter_0 = data['parameter0']
                        self.__parameter_1 = data['parameter1']
                        self.__parameter_2 = data['parameter2']
                        self.__parameter_3 = data['parameter3']
                        self.__parameter_4 = data['parameter4']
                        self.__parameter_5 = data['parameter5']

                else:
                    warnings.warn("Please Check your parameter file. \n"
                                  "If file has multiple camera parameter, typing the name of camera!!\n"
                                  "see detail documentation here https://github.com/MoilOrg/moildev\n"
                                  "or you can email to 'haryanto@o365.mcut.edu.tw'")

    def __init_alpha_rho_table(self):
        """
        Create list for initial alpha to rho(height image).

        Returns:
            Initial alpha and rho table.
        """
        for i in range(1800):
            alpha = i / 10 * math.pi / 180
            self.__alpha_to_rho_table.append(
                (self.__parameter_0 *
                 alpha *
                 alpha *
                 alpha *
                 alpha *
                 alpha *
                 alpha +
                 self.__parameter_1 *
                 alpha *
                 alpha *
                 alpha *
                 alpha *
                 alpha +
                 self.__parameter_2 *
                 alpha *
                 alpha *
                 alpha *
                 alpha +
                 self.__parameter_3 *
                 alpha *
                 alpha *
                 alpha +
                 self.__parameter_4 *
                 alpha *
                 alpha +
                 self.__parameter_5 *
                 alpha) *
                self.__calibration_ratio)
            i += 1

        i = 0
        index = 0
        while i < 1800:
            while index < self.__alpha_to_rho_table[i]:
                self.__rho_to_alpha_table.append(i)
                index += 1
            i += 1

        while index < 3600:
            self.__rho_to_alpha_table.append(i)
            index += 1

    def __import_moildev(self):
        """
        Create moildev instance from Moildev SDK share object library.

        Returns:
            Moildev object (private attribute for this class)
        """
        self.__moildev = MoilCV.MoilCV(
            self.__camera_name,
            self.__sensor_width,
            self.__sensor_height,
            self.__Icx,
            self.__Icy,
            self.__ratio,
            self.__image_width,
            self.__image_height,
            self.__calibration_ratio,
            self.__parameter_0,
            self.__parameter_1,
            self.__parameter_2,
            self.__parameter_3,
            self.__parameter_4,
            self.__parameter_5)

        self.__map_x = np.zeros(
            (self.__image_height,
             self.__image_width),
            dtype=np.float32)
        self.__map_y = np.zeros(
            (self.__image_height ,
             self.__image_width),
            dtype=np.float32)
        self.__res = self.__create_map_result_image()

    def __create_map_result_image(self):
        """
        Create Maps image from zeroes matrix for result image.

        Returns:
            Zeroes matrix same size with original image to stored data from result image.
        """
        size = self.__image_height, self.__image_width, 3
        return np.zeros(size, dtype=np.uint8)

    @classmethod
    def version(cls):
        """
        Showing the version of the library and the new feature updated.

        Returns:
            Moildev version
        """
        MoilCV.version()

    def camera_name(self):
        """
        Get camera name.

        Returns:
            Camera name (string)
        """
        return self.__camera_name

    def camera_fov(self):
        """
        Get Field of View Camera.

        Returns:
            FoV camera (int)
        """
        return self.__camera_fov

    def icx(self):
        """
        Get center image from width image.

        Returns:
            Image center X (int)
        """
        return self.__Icx

    def icy(self):
        """
        Get center image from height image.

        Returns:
            Image center Y(int)
        """
        if self.__Icy is not None:
            return self.__Icy

    def image_width(self):
        """
        Get the size width of the image.

        Returns:
            image width(int)
        """
        return self.__image_width

    def image_height(self):
        """
        Get the size height of the image.

        Returns:
            image height(int)
        """
        return self.__image_height

    def maps_anypoint(self, alpha, beta, zoom, mode=1):
        """The purpose is to generate a pair of X-Y Maps for the specified alpha, beta and zoom parameters,
        the result X-Y Maps can be used later to remap the original fisheye image to the target angle image.

        Args:
            alpha (): value of zenith distance(float).
            beta (): value of azimuthal distance based on cartography system(float)
            zoom (): value of zoom(float)
            mode (): selection anypoint mode(1 or 2)

        Returns:
            mapX: the mapping matrices X
            mapY: the mapping matrices Y

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        if mode == 1:
            if beta < 0:
                beta = beta + 360
            if alpha < -90 or alpha > 90 or beta < 0 or beta > 360:
                alpha = 0
                beta = 0

            else:
                alpha = -90 if alpha < -90 else alpha
                alpha = 90 if alpha > 90 else alpha
                beta = 0 if beta < 0 else beta
                beta = 360 if beta > 360 else beta
            self.__moildev.AnyPointM(
                self.__map_x, self.__map_y, alpha, beta, zoom)

        else:
            if alpha < - 90 or alpha > 90 or beta < -90 or beta > 90:
                alpha = 0
                beta = 0

            else:
                alpha = -90 if alpha < -90 else alpha
                alpha = 90 if alpha > 90 else alpha
                beta = -90 if beta < -90 else beta
                beta = 90 if beta > 90 else beta
            self.__moildev.AnyPointM2(
                self.__map_x, self.__map_y, alpha, beta, zoom)
        return self.__map_x, self.__map_y

    def maps_anypoint_car(self, pitch, yaw, roll, zoom):
        """

        Args:
            pitch:
            yaw:
            roll:
            zoom:

        Returns:

        """
        self.__moildev.CarAnyPoint(self.__map_x, self.__map_y, pitch, yaw, roll, zoom)
        return self.__map_x, self.__map_y

    def maps_panorama(self, alpha_min, alpha_max):
        """
        To generate a pair of X-Y Maps for alpha within 0 ... alpha_max degree, the result X-Y Maps can be used later
        to generate a panorama image from the original fisheye image.

        Args:
            alpha_min (): the minimum alpha degree given
            alpha_max (): the maximum alpha degree given. The recommended value is half of camera FOV. For example, use
                          90 for a 180 degree fisheye images and use 110 for a 220 degree fisheye images.

        Returns:
            mapX: the mapping matrices X
            mapY: the mapping matrices Y

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        self.__moildev.Panorama(self.__map_x, self.__map_y, alpha_min, alpha_max)
        return self.__map_x, self.__map_y

    def maps_panorama_rotation(self, alpha_max, iC_alpha_degree, iC_beta_degree):
        """
        To generate a pair of X-Y Maps for alpha within 0..alpha_max degree, the result X-Y Maps can be used later
        to generate a panorama image from the original fisheye image. The panorama image centered at the 3D
        direction with alpha = iC_alpha_degree and beta = iC_beta_degree.

        Args:
            alpha_max : max of alpha. The recommended value is half of camera FOV. For example, use
                        90 for a 180 degree fisheye images and use 110 for a 220 degree fisheye images.
            iC_alpha_degree : alpha angle of panorama center.
            iC_beta_degree : beta angle of panorama center.

        Returns:
            New mapX and mapY.

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        self.__moildev.PanoramaM_Rt(self.__map_x, self.__map_y, alpha_max, iC_alpha_degree, iC_beta_degree)
        return self.__map_x, self.__map_y

    def maps_reverse(self, alpha_max, iC_beta_degree):
        """
        Create maps for reverse image. this can work using input panorama rotation image

        Args:
            alpha_max: max of alpha. The recommended value is half of camera FOV. For example, use
                        90 for a 180 degree fisheye images and use 110 for a 220 degree fisheye images.
            iC_beta_degree : beta angle of panorama center.

        Returns:
            maps_x_reverse, maps_y_reverse

        """
        self.__moildev.revPanoramaMaps(self.__map_x, self.__map_y, alpha_max, iC_beta_degree)
        return self.__map_x, self.__map_y

    def anypoint(self, image, alpha, beta, zoom, mode=1):
        """
        Generate anypoint view image. for mode 1, the result rotation is betaOffset degree rotation around the
        Z-axis(roll) after alphaOffset degree rotation around the X-axis(pitch). for mode 2, The result rotation
        is thetaY degree rotation around the Y-axis(yaw) after thetaX degree rotation around the X-axis(pitch).

        Args:
            image (): src image given
            alpha (): the alpha offset that corespondent to the pitch rotation
            beta (): the beta offset that corespondent to the yaw rotation
            zoom (): decimal zoom factor, normally 1..12
            mode (): the mode view selected

        Returns:
            anypoint image

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        map_x, map_y = self.maps_anypoint(alpha, beta, zoom, mode)
        image = cv2.remap(image, map_x, map_y, cv2.INTER_CUBIC)
        return image

    def panorama(self, image, alpha_min, alpha_max):
        """
        The panorama image centered at the 3D direction with alpha = iC_alpha_degree and beta = iC_beta_degree.

        Args:
            image: image src given
            alpha_min:
            alpha_max:

        Returns:
            Panorama view image

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        map_x, map_y = self.maps_panorama(alpha_min, alpha_max)
        image = cv2.remap(image, map_x, map_y, cv2.INTER_CUBIC)
        return image

    def reverse(self, image, alpha_max, iC_alpha_degree, iC_beta_degree):
        """
        To generate the image reverse image from panorama that can change the focus direction from the original
        images. The panorama reverse image centered at the 3D direction with alpha_max = max of alpha and beta =
        iC_beta_degree.

        Args:
            image: input image
            alpha_max: max of alpha. The recommended value is half of camera FOV. For example, use
                    90 for a 180 degree fisheye images and use 110 for a 220 degree fisheye images.
            iC_alpha_degree: alpha angle of panorama center
            iC_beta_degree: beta angle of panorama center

        Returns:
            reverse image

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        self.__moildev.PanoramaM_Rt(self.__map_x, self.__map_y, alpha_max, iC_alpha_degree, iC_beta_degree)
        result = cv2.remap(image, self.__map_x, self.__map_y, cv2.INTER_CUBIC)
        self.__moildev.revPanorama(result, self.__res, alpha_max, iC_beta_degree)
        return self.__res

    def new_reverse(self, image, alpha_max, iC_alpha_degree, iC_beta_degree):
        """
        New function for change the optical point of fisheye image. using this function, it will improve
        the speed of the computation processing more than 30%

        Args:
            image: input image
            alpha_max: max of alpha. The recommended value is half of camera FOV. For example, use
                    90 for a 180 degree fisheye images and use 110 for a 220 degree fisheye images.
            iC_alpha_degree: alpha angle of panorama center
            iC_beta_degree: beta angle of panorama center

        Returns:
            reverse image

        """
        self.__moildev.PanoramaM_Rt(self.__map_x, self.__map_y, alpha_max, iC_alpha_degree, iC_beta_degree)
        result = cv2.remap(image, self.__map_x, self.__map_y, cv2.INTER_CUBIC)
        self.__moildev.revPanoramaMaps(self.__map_x, self.__map_y, alpha_max, iC_beta_degree)
        rev_image = cv2.remap(result, self.__map_x, self.__map_y, cv2.INTER_CUBIC)
        return rev_image

    def get_alpha_from_rho(self, rho):
        """
        Get the alpha from rho image.

        Args:
            rho: the value of rho given

        Returns:
            alpha
        """
        if rho >= 0:
            return self.__rho_to_alpha_table[rho] / 10
        else:
            return -self.__rho_to_alpha_table[-rho] / 10

    def get_rho_from_alpha(self, alpha):
        """
        Get rho image from alpha given.

        Args:
            alpha: the value of alpha given

        Returns:
            rho image

        """
        return self.__alpha_to_rho_table[round(alpha * 10)]

    def get_alpha_beta(self, coordinateX, coordinateY, mode=1):
        """
        Get the alpha beta from specific coordinate image.

        Args:
            coordinateX:
            coordinateY:
            mode:

        Returns:
            alpha, beta

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        delta_x = coordinateX - self.__Icx
        delta_y = -(coordinateY - self.__Icy)
        if mode == 1:
            r = round(math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2)))
            alpha = self.get_alpha_from_rho(r)
            if coordinateX == self.__Icy:
                angle = 0
            else:
                angle = (math.atan2(delta_y, delta_x) * 180) / math.pi
            beta = 90 - angle
        else:
            alpha = self.get_alpha_from_rho(delta_y)
            beta = self.get_alpha_from_rho(delta_x)
        return alpha, beta
