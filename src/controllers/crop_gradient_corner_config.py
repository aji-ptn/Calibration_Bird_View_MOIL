import cv2
import numpy as np


def crop_region(img, name):
    if name == "horizontal_left":
        pts = np.array([[0, 0], [img.shape[1], 0], [int(img.shape[1]*(3/4)), 0], [int(img.shape[1]*(3/4)), img.shape[0]], [0, img.shape[0]]])
        image = region_bounding(img, name, pts)

    elif name == "horizontal_right":
        pts = np.array([[0, 0], [int(img.shape[1]*0.3), 0], [int(img.shape[1]*0.3), img.shape[0]], [img.shape[1], img.shape[0]], [img.shape[1], 0]])
        image = region_bounding(img, name, pts)

    elif name == "vertical_up":
        pts = np.array([[0, 0], [img.shape[1], 0], [img.shape[1], img.shape[0]], [img.shape[1], int(img.shape[0]*(3/4))], [0, int(img.shape[0]*(3/4))]])
        image = region_bounding(img, name, pts)

    elif name == "vertical_bottom":
        pts = np.array([[0, 0], [0, int(img.shape[0]*0.3)], [img.shape[1], int(img.shape[0]*0.3)], [img.shape[1], img.shape[0]], [0, img.shape[0]]])
        image = region_bounding(img, name, pts)

    elif name == "front_left":
        pts = np.array([[0, 0], [img.shape[1], 0], [img.shape[1], img.shape[0]], [0, int(img.shape[0] * 0.8)]])
        image = region_bounding(img, name, pts)

    elif name == "left_front":
        pts = np.array([[0, int(img.shape[0] / 2)], [img.shape[1], img.shape[0]], [0, int(img.shape[0])]])
        image = region_bounding(img, name, pts)

    elif name == "front_right":
        pts = np.array([[0, 0], [img.shape[1], 0], [img.shape[1], int(img.shape[0] * 0.8)], [0, int(img.shape[0])]])
        image = region_bounding(img, name, pts)

    elif name == "right_front":
        pts = np.array([[img.shape[1], int(img.shape[0] / 2)], [img.shape[1], img.shape[0]], [0, img.shape[0]]])
        image = region_bounding(img, name, pts)

    elif name == "left_rear":
        pts = np.array([[0, 0], [img.shape[1], 0], [0, int(img.shape[0] / 2)]])
        image = region_bounding(img, name, pts)

    elif name == "rear_left":
        pts = np.array(
            [[0, int(img.shape[0] * 0.2)], [int(img.shape[1]), 0], [img.shape[1], img.shape[0]], [0, img.shape[0]]])
        image = region_bounding(img, name, pts)

    elif name == "right_rear":
        pts = np.array([[0, 0], [img.shape[1], 0], [img.shape[1], int(img.shape[0] / 2)]])
        image = region_bounding(img, name, pts)

    elif name == "rear_right":
        pts = np.array([[0, 0], [img.shape[1], int(img.shape[0] * 0.2)], [img.shape[1], img.shape[0]], [0, img.shape[0]]])
        image = region_bounding(img, name, pts)

    else:
        image = None

    return image


def region_bounding(img, name, pts):
    rect = cv2.boundingRect(pts)
    x, y, w, h = rect
    cropped = img[y:y + h, x:x + w].copy()

    pts = pts - pts.min(axis=0)

    mask = np.zeros(cropped.shape[:2], np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

    dst = cv2.bitwise_and(cropped, cropped, mask=mask)

    if name == "horizontal_left":
        canvas = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
        canvas[0:0 + dst.shape[0], 0:0 + dst.shape[1]] = dst
        return canvas
    elif name == "horizontal_right":
        canvas = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
        canvas[0:0 + dst.shape[0], 0:0 + dst.shape[1]] = dst
        return canvas
    elif name == "vertical_up":
        canvas = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
        canvas[0:0 + dst.shape[0], 0:0 + dst.shape[1]] = dst
        return canvas
    elif name == "vertical_bottom":
        canvas = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
        canvas[0:0 + dst.shape[0], 0:0 + dst.shape[1]] = dst
        return canvas
    elif name == "front_left":
        front_left_canvas = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
        front_left_canvas[0:0 + dst.shape[0], 0:0 + dst.shape[1]] = dst
        return front_left_canvas
    elif name == "front_right":
        front_right_canvas = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
        front_right_canvas[0:0 + dst.shape[0], 0:0 + dst.shape[1]] = dst
        return front_right_canvas
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
    elif name == "left_rear":
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
