import numpy as np
from Moildev import Moildev
from ui_main import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui
import cv2


def select_file(parent, title, dir_path, file_filter):
    """
    Find the file path from the directory computer.

    Args:
        parent: The parent windows to show dialog always in front of user interface
        title: the title window of open dialog
        file_filter: determine the specific file want to search
        dir_path: Navigate to specific directory

    return:
        file_path: location
    """
    option = QFileDialog.Option.DontUseNativeDialog
    file_path, _ = QFileDialog.getOpenFileName(parent, title, dir_path,
                                               file_filter, options=option)
    return file_path


def read_image(image_path):
    """
    Method loads an image from the specified file (use the cv2.imread function to complete the task).
    If the image cannot be read (because of missing file, improper permissions, unsupported or invalid format)
    then this method returns an empty matrix.

    Args:
        image_path : The path of image file

    return:
        Image: load image

    - Example:

    .. code-block:: python

        image = read_image(image_path)
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError("`{}` cannot be loaded".format(image_path))
    return image


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


def draw_polygon(image, mapX, mapY):
    """
    Return image with a drawn polygon on it from mapX and mapY generated by maps anypoint or panorama.

    Args:
        image: Original image
        mapX: map image X from anypoint process
        mapY: map image Y from anypoint process

    return:
        image: map x, map y

    - Example:

    .. code-block:: python

        image = draw_polygon(image,mapX,mapY)
    """
    hi, wi = image.shape[:2]
    X1 = []
    Y1 = []
    X2 = []
    Y2 = []
    X3 = []
    Y3 = []
    X4 = []
    Y4 = []

    x = 0
    while x < wi:
        a = mapX[0,]
        b = mapY[0,]
        ee = mapX[-1,]
        f = mapY[-1,]

        if a[x] == 0. or b[x] == 0.:
            pass
        else:
            X1.append(a[x])
            Y1.append(b[x])

        if f[x] == 0. or ee[x] == 0.:
            pass
        else:
            Y3.append(f[x])
            X3.append(ee[x])
        x += 10

    y = 0
    while y < hi:
        c = mapX[:, 0]
        d = mapY[:, 0]
        g = mapX[:, -1]
        h = mapY[:, -1]

        # eliminate the value 0 for map X
        if d[y] == 0. or c[y] == 0.:  # or d[y] and c[y] == 0.0:
            pass
        else:
            Y2.append(d[y])
            X2.append(c[y])

        # eliminate the value 0 for map Y
        if h[y] == 0. or g[y] == 0.:
            pass
        else:
            Y4.append(h[y])
            X4.append(g[y])

        # render every 10 times, it will be like 1, 11, 21 and so on.
        y += 10

    p = np.array([X1, Y1])
    q = np.array([X2, Y2])
    r = np.array([X3, Y3])
    s = np.array([X4, Y4])
    points = p.T.reshape((-1, 1, 2))
    points2 = q.T.reshape((-1, 1, 2))
    points3 = r.T.reshape((-1, 1, 2))
    points4 = s.T.reshape((-1, 1, 2))

    # Draw polyline on original image
    # cv2.polylines(image, np.int32([points]), False, (0, 0, 255), 10)
    # cv2.polylines(image, np.int32([points2]), False, (255, 0, 0), 10)
    cv2.polylines(image, np.int32([points3]), False, (0, 255, 0), 10)
    # cv2.polylines(image, np.int32([points4]), False, (0, 255, 0), 10)
    return image


def draw_point(image, coordinate_point, radius=5):
    """
    Drawing point on the image.

    Args:
        image ():
        coordinate_point ():
        radius ():

    Returns:

    """

    if coordinate_point is not None:
        w, h = image.shape[:2]
        if h >= 1000:
            cv2.circle(image, coordinate_point, radius, (200, 5, 200), 30, -1)
        else:
            cv2.circle(image, coordinate_point, radius, (200, 5, 200), -1)
    return image


class Controller(Ui_MainWindow):
    def __init__(self, parent):
        super(Controller, self).__init__()
        self.setupUi(parent)
        self.pushButton_open_image.clicked.connect(self.open_image)
        self.spinBox_alpha.valueChanged.connect(self.create_maps)

    def open_image(self):
        media_path = select_file(None, "Select Media !!", "",
                                 "Files format (*.jpeg *.jpg *.png *.gif *.bmg)")
        if media_path:
            parameter_path = select_file(None, "Select Parameter !!", "",
                                         "Files format (*.txt *.json)")
            if parameter_path:
                self.image = read_image(media_path)
                self.moildev = Moildev.Moildev(parameter_path)
                self.create_maps()

    def create_maps(self):
        alpha = self.spinBox_alpha.value()
        rho = self.moildev.icy() - round(self.moildev.get_rho_from_alpha(alpha))
        icx = self.moildev.icx()
        image = draw_point(self.image.copy(), (icx, rho))
        self.maps_x, self.maps_y = self.moildev.maps_panorama(10, alpha)
        image = draw_polygon(image, self.maps_x, self.maps_y)
        show_image_to_label(self.lable_image, image, 800, plusIcon=True)

def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    a = Controller(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
