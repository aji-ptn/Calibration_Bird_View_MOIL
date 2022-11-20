from PyQt6 import QtGui, QtCore, QtWidgets
import cv2


def select_file(parent, title, dir_path, file_filter):
    """
    Find the file path from the directory computer.

    Args:
        parent (): The parent windows to show dialog always in front of user interface
        title: the title window of open dialog
        file_filter: determine the specific file want to search
        dir_path: Navigate to specific directory

    return:
        file_path: location
    """
    option = QtWidgets.QFileDialog.Option.DontUseNativeDialog
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(parent, title, dir_path,
                                                         file_filter, options=option)
    return file_path


def calculate_ratio_image(label, image):
    """
    This function is to Calculate the initial ratio of the image.

    Args:
        label: the label for showing image on user interface
        image: image object

    Returns:
        ratio_x : ratio width between image and ui window.
        ratio_y : ratio height between image and ui window.
        center : find the center image on window user interface.
    """
    h = label.height()
    w = label.width()
    height, width = image.shape[:2]
    print(h, w)
    print(height, width)
    ratio_x = width / w
    ratio_y = height / h
    return ratio_x, ratio_y


# def select_camera_type(parameter_path):
#     """
#     This function allows a user to choose what parameter will be used. this function will open a dialog,
#     and you can select the parameter available from Combobox.
#
#     return:
#         cls.__camera_type : load camera type
#
#     - Example:
#
#     .. code-block:: python
#
#         type_camera = MoilUtils.selectCameraType()
#     """
#     window_select_camera_type = SelectCameraType()
#     window_select_camera_type.set_camera_parameter_path(parameter_path)
#     camera_type = window_select_camera_type.select_camera_type()
#     return camera_type


# def selectCameraSource():
#     """
#     This is a function will be used to select camera source for open camera in user interface frame
#
#     Returns:
#         winOpenCam.camera_source: load camera
#     """
#     openCamSource = QtWidgets.QDialog()
#     winOpenCam = CameraSource(openCamSource)
#     openCamSource.exec()
#     return winOpenCam.camera_source


def show_image_to_label(label, image, width, angle=0, plusIcon=False):
    """
    This function Display an image to the label widget on the user interface. It requires some arguments
    such as image, label name and image width. suppose you don't like to draw a center point icon (+)
    you can change the plusIcon argument to become False.

    Args:
        label: The label will contain image to show in your user interface
        image: Image that want to show on user interface
        width: the width of result image, this value will calculate the height following the ratio.
        angle: the angle of image
        plusIcon: Drawing the plus icon on the image, by default this will be False.
                    if you want to draw you have to change to be True.

    Returns:
        Showing image on the label

    - Example:

    .. code-block:: python

        image = MoilUtils.showImageToLabel(label, image, 400, 0, False)
    """

    height = calculate_height(image, width)
    image = resize_image(image, width)
    image = rotate_image(image, angle)
    if plusIcon:
        # draw plus icon on image and show to label
        h, w = image.shape[:2]
        w1 = round((w / 2) - 10)
        h1 = round(h / 2)
        w2 = round((w / 2) + 10)
        h2 = round(h / 2)
        w3 = round(w / 2)
        h3 = round((h / 2) - 10)
        w4 = round(w / 2)
        h4 = round((h / 2)) + 10
        cv2.line(image, (w1, h1), (w2, h2), (0, 255, 0), 1)
        cv2.line(image, (w3, h3), (w4, h4), (0, 255, 0), 1)

    label.setMinimumSize(QtCore.QSize(width, height))
    label.setMaximumSize(QtCore.QSize(width, height))
    image = QtGui.QImage(image.data, image.shape[1], image.shape[0],
                         QtGui.QImage.Format.Format_RGB888).rgbSwapped()
    label.setPixmap(QtGui.QPixmap.fromImage(image))


def rotate_image(src, angle, center=None, scale=1.0):
    """
    Rotation of images are among the most basic operations under the broader class of
    Affine transformations. This function will return the image after turning clockwise
    or anticlockwise depending on the angle given.

    Args:
        src: original image
        angle: the value angle for turn the image
        center: determine the specific coordinate to rotate image
        scale: scale image

    Returns:
        dst image: rotated image

    - Example:

    .. code-block:: python

        image = rotate_image(image, 90)
    """
    h, w = src.shape[:2]
    if center is None:
        center = (w / 2, h / 2)
    m = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(src, m, (w, h))
    return rotated


def resize_image(image, width):
    """
    Changing the dimensions of image according to the size width given (it use cv2.resize function from OpenCV).
    It will keep the aspect ratio of the original image.

    Args:
        image: image original
        width: image width we want

    Returns:
        result: image has been resize

    - Example:

    .. code-block:: python

        image = resize_image(image, 140)
    """
    h, w = image.shape[:2]
    r = width / float(w)
    hi = round(h * r)
    result = cv2.resize(image, (width, hi),
                        interpolation=cv2.INTER_AREA)
    return result


def calculate_height(image, width):
    """
    Return the height value of an image by providing the width value. This high
    value is calculated by keeping the aspect ratio of the image.

    Args:
        image: original image
        width: size image we want

    Returns:
        height: height image

    - Example:

    .. code-block:: python

        height = calculate_height(image, 140)
    """

    h, w = image.shape[:2]
    r = width / float(w)
    height = round(h * r)
    return height


def draw_point(image, coordinatePoint, radius=5):
    """
    Drawing point on the image.

    Args:
        image ():
        coordinatePoint ():
        radius ():

    Returns:

    """

    if coordinatePoint is not None:
        w, h = image.shape[:2]
        if h >= 1000:
            cv2.circle(image, coordinatePoint, radius, (200, 5, 200), 30, -1)
        else:
            cv2.circle(image, coordinatePoint, radius, (200, 5, 200), -1)
    return image
