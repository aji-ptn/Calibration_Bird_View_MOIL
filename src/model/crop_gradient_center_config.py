import cv2
import numpy as np


def crop_region(img, name, gradient_mode=None):
    """
        This function is for crop image between two images
    Args:
        img: image input
        name: command for witch image will crop
        gradient_mode: command for mode crop image

    Returns:
        image: region cropping image
    """
    if name == "front_left":
        if gradient_mode == "H":
            # -------------- Horizontal -----------------
            pts = np.array([[0, 0], [img.shape[1], 0], [img.shape[1], img.shape[0]], [0, int(img.shape[0] * 0.9)]])
        elif gradient_mode == "V":
            # --------- vertical -----------
            pts = np.array([[0, 0], [img.shape[1], 0], [img.shape[1], img.shape[0]], [int(img.shape[1] / 4), 0]])
        elif gradient_mode == "D":
            # --------- rectangle size -----
            pts = np.array([[0, 0], [img.shape[1], 0], [img.shape[1], img.shape[0]], [0, int(img.shape[0] * 0.2)]])
        image = region_bounding(img, name, pts)

    elif name == "left_front":
        if gradient_mode == "H":
            # -------------- Horizontal -----------------
            pts = np.array([[0, int(img.shape[0] * 0.7)], [img.shape[1], img.shape[0]], [0, int(img.shape[0])]])
        elif gradient_mode == "V":
            # -------------- vertical -----------------
            pts = np.array([[0, 0], [int(img.shape[1] / (3 / 2)), 0], [img.shape[1], img.shape[0]], [0, int(img.shape[0])]])
        elif gradient_mode == "D":
            # --------- rectangle size -----
            pts = np.array([[0, 0], [int(img.shape[0] * 0.2), 0], [img.shape[1], img.shape[0]], [0, int(img.shape[0])]])
        image = region_bounding(img, name, pts)

    elif name == "front_right":
        if gradient_mode == "H":
            # -------------- Horizontal -----------------
            pts = np.array([[0, 0], [img.shape[1], 0], [img.shape[1], int(img.shape[0] * 0.9)], [0, int(img.shape[0])]])
        elif gradient_mode == "V":
            # -------------- vertical -----------------
            pts = np.array([[0, 0], [img.shape[1], 0], [int(img.shape[1]/2), 0], [0, int(img.shape[0])]])
        elif gradient_mode == "D":
            # --------- rectangle size -----
            pts = np.array([[0, 0], [img.shape[1], 0], [img.shape[1], int(img.shape[0] * 0.2)], [0, int(img.shape[0])]])
        image = region_bounding(img, name, pts)

    elif name == "right_front":
        if gradient_mode == "H":
            # -------------- Horizontal -----------------
            pts = np.array([[img.shape[1], int(img.shape[0] * 0.7)], [img.shape[1], img.shape[0]], [0, img.shape[0]]])
        elif gradient_mode == "V":
            # -------------- vertical -----------------
            pts = np.array([[int(img.shape[1] / 4), 0], [img.shape[1], 0], [img.shape[1], img.shape[0]], [0, img.shape[0]]])
            # --------- rectangle size -----
        elif gradient_mode == "D":
            pts = np.array(
                [[int(img.shape[1] * 0.8), 0], [img.shape[1], 0], [img.shape[1], img.shape[0]], [0, img.shape[0]]])
        image = region_bounding(img, name, pts)

    elif name == "left_rear":
        if gradient_mode == "H":
            # -------------- Horizontal -----------------
            pts = np.array([[0, 0], [img.shape[1], 0], [0, int(img.shape[0] * 0.3)]])
        elif gradient_mode == "V":
            # -------------- vertical -----------------
            pts = np.array([[0, 0], [img.shape[1], 0], [int(img.shape[1] / (3/2)), img.shape[0]], [0, int(img.shape[0])]])
            # --------- rectangle size -----
        elif gradient_mode == "D":
            pts = np.array([[0, 0], [img.shape[1], 0], [int(img.shape[1] * 0.1), img.shape[0]], [0, img.shape[0]]])
        image = region_bounding(img, name, pts)

    elif name == "rear_left":
        if gradient_mode == "H":
            # -------------- Horizontal -----------------
            pts = np.array(
                [[0, int(img.shape[0] * 0.1)], [int(img.shape[1]), 0], [img.shape[1], img.shape[0]], [0, img.shape[0]]])
        elif gradient_mode == "V":
            # -------------- vertical -----------------
            pts = np.array([[img.shape[1], 0], [img.shape[1], img.shape[0]], [0, img.shape[0]], [int(img.shape[1]/4), img.shape[0]]])
            # --------- rectangle size -----
        elif gradient_mode == "D":
            pts = np.array(
                [[0, int(img.shape[0] * 0.8)], [int(img.shape[1]), 0], [img.shape[1], img.shape[0]], [0, img.shape[0]]])
        image = region_bounding(img, name, pts)

    elif name == "right_rear":
        if gradient_mode == "H":
            # -------------- Horizontal -----------------
            pts = np.array([[0, 0], [img.shape[1], 0], [img.shape[1], int(img.shape[0] * 0.3)]])
        elif gradient_mode == "V":
            # -------------- vertical -----------------
            pts = np.array([[0, 0], [img.shape[1], 0], [img.shape[1], img.shape[0]], [int(img.shape[1] / 4), img.shape[0]]])
            # --------- rectangle size -----
        elif gradient_mode == "D":
            pts = np.array(
                [[0, 0], [img.shape[1], 0], [img.shape[1], img.shape[0]], [int(img.shape[1] * 0.8), img.shape[0]]])
        image = region_bounding(img, name, pts)

    elif name == "rear_right":
        if gradient_mode == "H":
            # -------------- Horizontal -----------------
            pts = np.array(
                [[0, 0], [img.shape[1], int(img.shape[0] * 0.1)], [img.shape[1], img.shape[0]], [0, img.shape[0]]])
        elif gradient_mode == "V":
            # -------------- vertical -----------------
            pts = np.array(
                [[0, 0], [int(img.shape[1]/2), img.shape[0]], [img.shape[1], img.shape[0]], [0, img.shape[0]]])
        elif gradient_mode == "D":
            # --------- rectangle size -----
            pts = np.array(
                [[0, 0], [img.shape[1], int(img.shape[0] * 0.8)], [img.shape[1], img.shape[0]], [0, img.shape[0]]])
        image = region_bounding(img, name, pts)

    else:
        image = None

    return image


def region_bounding(img, name, pts):
    """
    This function is for create image cropping with black background
    Args:
        img: image input
        name: command for witch image will process
        pts: point of bounding

    Returns:
    image with black background
    """
    rect = cv2.boundingRect(pts)
    x, y, w, h = rect
    cropped = img[y:y + h, x:x + w].copy()

    pts = pts - pts.min(axis=0)

    mask = np.zeros(cropped.shape[:2], np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

    dst = cv2.bitwise_and(cropped, cropped, mask=mask)

    if name == "front_left":
        front_left_canvas = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
        front_left_canvas[0:0 + dst.shape[0], 0:0 + dst.shape[1]] = dst
        return front_left_canvas
    elif name == "left_front":
        left_front_canvas = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
        left_front_canvas[
        left_front_canvas.shape[0] - dst.shape[0]:left_front_canvas.shape[0] - dst.shape[0] + dst.shape[0],
        0:0 + dst.shape[1]] = dst
        return left_front_canvas
    elif name == "front_right":
        front_right_canvas = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
        front_right_canvas[0:0 + dst.shape[0], 0:0 + dst.shape[1]] = dst
        return front_right_canvas
    elif name == "right_front":
        right_front_canvas = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
        right_front_canvas[
        right_front_canvas.shape[0] - dst.shape[0]:right_front_canvas.shape[0] - dst.shape[0] + dst.shape[0],
        0:0 + dst.shape[1]] = dst
        return right_front_canvas
    if name == "left_rear":
        left_rear_canvas = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
        left_rear_canvas[0:0 + dst.shape[0], 0:0 + dst.shape[1]] = dst
        return left_rear_canvas
    elif name == "rear_left":
        rear_left = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
        rear_left[rear_left.shape[0] - dst.shape[0]:img.shape[0] - dst.shape[0] + dst.shape[0],
        0:0 + dst.shape[1]] = dst  # 0 is height 1 width
        return rear_left
    elif name == "right_rear":
        right_rear = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
        right_rear[0:0 + dst.shape[0], 0:0 + dst.shape[1]] = dst
        return right_rear
    elif name == "rear_right":
        rear_right = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
        rear_right[rear_right.shape[0] - dst.shape[0]:rear_right.shape[0] - dst.shape[0] + dst.shape[0],
        0:0 + dst.shape[1]] = dst  # 0 is height 1 width
        return rear_right


def crop_for_gradient_front_left(image_1, image_2):
    """
    Crop image for diagonal overlap front left
    Args:
        image_1: image front
        image_2: image left

    Returns:
        pos_x: position in image x
        pos_y: position in image y
        image_1: crop image front
        image_2: crop image left
    """
    minimum = min(image_1.shape[1], image_2.shape[1], image_1.shape[0], image_2.shape[0])
    pos_x = max(image_1.shape[1], image_2.shape[1]) - minimum
    pos_y = max(image_1.shape[0], image_2.shape[0]) - minimum
    if image_1.shape[1] != minimum:
        image_1 = image_1[0:image_1.shape[0], image_1.shape[1] - minimum:image_1.shape[1] - minimum + image_1.shape[1]]
    if image_2.shape[1] != minimum:
        image_2 = image_2[0:image_2.shape[0], image_2.shape[1] - minimum:image_1.shape[1] - minimum + image_2.shape[1]]
    if image_1.shape[0] != minimum:
        image_1 = image_1[image_1.shape[0] - minimum:image_1.shape[0] - minimum + image_1.shape[0], 0:image_1.shape[1]]
    if image_2.shape[0] != minimum:
        image_2 = image_2[image_2.shape[0] - minimum:image_2.shape[0] - minimum + image_2.shape[0], 0:image_2.shape[1]]
    return pos_x, pos_y, image_1, image_2


def crop_for_gradient_front_right(image_1, image_2):
    """
    Crop image for diagonal overlap front right
    Args:
        image_1: image front
        image_2: image right

    Returns:
        pos_x: position in image x
        pos_y: position in image y
        image_1: crop image front
        image_2: crop image right
    """
    minimum = min(image_1.shape[1], image_2.shape[1], image_1.shape[0], image_2.shape[0])
    pos_x = max(image_1.shape[1], image_2.shape[1]) - minimum
    pos_y = max(image_1.shape[0], image_2.shape[0]) - minimum
    if image_1.shape[1] != minimum:
        image_1 = image_1[0:image_1.shape[0], 0:minimum]
    if image_2.shape[1] != minimum:
        image_2 = image_2[0:image_2.shape[0], 0:minimum]
    if image_1.shape[0] != minimum:
        image_1 = image_1[0:image_1.shape[0] - minimum, 0:image_1.shape[1]]
    if image_2.shape[0] != minimum:
        image_2 = image_2[0:image_2.shape[0] - minimum, 0:image_2.shape[1]]
    return pos_x, pos_y, image_1, image_2


def crop_for_gradient_rear_left(image_1, image_2):
    """
    Crop image for diagonal overlap rear left
    Args:
        image_1: image rear
        image_2: image left

    Returns:
        pos_x: position in image x
        pos_y: position in image y
        image_1: crop image rear
        image_2: crop image left
    """
    minimum = min(image_1.shape[1], image_2.shape[1], image_1.shape[0], image_2.shape[0])
    pos_x = max(image_1.shape[1], image_2.shape[1]) - minimum
    pos_y = max(image_1.shape[0], image_2.shape[0]) - minimum
    if image_1.shape[1] != minimum:
        image_1 = image_1[0:image_1.shape[0], image_1.shape[1] - minimum:image_1.shape[1] - minimum + image_1.shape[1]]
    if image_2.shape[1] != minimum:
        image_2 = image_2[0:image_2.shape[0], image_2.shape[1] - minimum:image_2.shape[1] - minimum + image_2.shape[1]]
    if image_1.shape[0] != minimum:
        image_1 = image_1[0:image_1.shape[0], 0:image_1.shape[1] - minimum]
    if image_2.shape[0] != minimum:
        image_2 = image_2[0:image_2.shape[0], 0:image_2.shape[1] - minimum]
    return pos_x, pos_y, image_1, image_2


def crop_for_gradient_rear_right(image_1, image_2):
    """
    Crop image for diagonal overlap rear right
    Args:
        image_1: image rear
        image_2: image right

    Returns:
        pos_x: position in image x
        pos_y: position in image y
        image_1: crop image rear
        image_2: crop image right
    """
    minimum = min(image_1.shape[1], image_2.shape[1], image_1.shape[0], image_2.shape[0])
    pos_x = max(image_1.shape[1], image_2.shape[1]) - minimum
    pos_y = max(image_1.shape[0], image_2.shape[0]) - minimum
    if image_1.shape[1] != minimum:
        image_1 = image_1[0:image_1.shape[0], 0:minimum]
    if image_2.shape[1] != minimum:
        image_2 = image_2[0:image_2.shape[0], 0:minimum]
    if image_1.shape[0] != minimum:
        image_1 = image_1[0:image_1.shape[0], 0:image_1.shape[1] - minimum]
    if image_2.shape[0] != minimum:
        image_2 = image_2[0:image_2.shape[0], 0:image_2.shape[1] - minimum]
    return pos_x, pos_y, image_1, image_2
