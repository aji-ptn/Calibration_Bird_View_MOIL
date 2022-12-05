import numpy as np
from .overlap_corner_config import *


def merge_image_4_camera_corner_config(image_crop, shift_x, shift_y):
    # create canvas image
    height = max(image_crop[0].shape[0],
                 image_crop[1].shape[0]) + max(image_crop[2].shape[0],
                                               image_crop[3].shape[0])
    width = max((image_crop[0].shape[1] + image_crop[1].shape[1]),
                (image_crop[2].shape[1] + image_crop[3].shape[1]))
    merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)

    # determine position image 1
    pos_x_0 = shift_x[0]
    pos_y_0 = abs(shift_y[1]) + shift_y[0] if shift_y[1] <= 0 else shift_y[0]

    # determine position image 2
    pos_x_1 = image_crop[0].shape[1] - shift_x[1] + shift_x[0]
    pos_y_1 = 0 if shift_y[1] <= 0 else shift_y[1]

    # update the information of shift x from image 1 and image 2
    shift_y[0] = pos_y_0
    shift_y[1] = pos_y_1

    # determine position image 3
    pos_x_2 = shift_x[2]
    pos_y_2 = image_crop[0].shape[0] - shift_y[2]

    # determine position image 4
    pos_x_3 = width - image_crop[3].shape[1] - shift_x[3]
    pos_y_3 = image_crop[1].shape[0] - shift_y[3]

    if shift_x[2] < 0:
        width = abs(shift_x[2]) + max((image_crop[0].shape[1] + image_crop[1].shape[1]),
                                      (image_crop[2].shape[1] + image_crop[3].shape[1]))
        merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)
        pos_x_0 = shift_x[0] + abs(shift_x[2])
        pos_x_1 = image_crop[0].shape[1] - shift_x[1] + shift_x[0] + abs(shift_x[2])
        pos_x_2 = 0
        pos_x_3 = width - image_crop[3].shape[1] - shift_x[3]

    if shift_x[3] < 0:
        width = max((image_crop[0].shape[1] + image_crop[1].shape[1]),
                    (image_crop[2].shape[1] + image_crop[3].shape[1])) + abs(shift_x[3])
        merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)

        pos_x_3 = width - image_crop[3].shape[1]

    # merge image
    merge_image_canvas[pos_y_0:pos_y_0 + image_crop[0].shape[0],
    pos_x_0:pos_x_0 + image_crop[0].shape[1]] = image_crop[0]

    merge_image_canvas[pos_y_1:pos_y_1 + image_crop[1].shape[0],
    pos_x_1:pos_x_1 + image_crop[1].shape[1]] = image_crop[1]

    merge_image_canvas[pos_y_2:pos_y_2 + image_crop[2].shape[0],
    pos_x_2:pos_x_2 + image_crop[2].shape[1]] = image_crop[2]

    merge_image_canvas[pos_y_3:pos_y_3 + image_crop[3].shape[0],
    pos_x_3:pos_x_3 + image_crop[3].shape[1]] = image_crop[3]

    bird_view = merge_image_canvas.copy()
    # image overlay
    pos_x, overlap_front, _ = find_overlap_image_front(image_crop, shift_x, shift_y)
    if overlap_front is not None:
        if shift_x[2] < 0:
            pos_x = pos_x + abs(shift_x[2])
        merge_image_canvas[pos_y_0 + pos_y_1:pos_y_0 + pos_y_1 + overlap_front.shape[0],
        pos_x: pos_x + overlap_front.shape[1]] = overlap_front

    pos_y, overlap_left, _ = find_overlap_image_front_left(image_crop, shift_x, shift_y)
    if overlap_left is not None:
        pos_x = abs(shift_x[2])
        if shift_y[0] > 0:
            # when the image 1 is moving from the position
            pos_y = pos_y + shift_y[0]
        merge_image_canvas[pos_y:pos_y + overlap_left.shape[0],
        pos_x:pos_x + overlap_left.shape[1]] = overlap_left

    pos_y, overlap_right = find_overlap_image_front_right(image_crop, shift_x, shift_y)
    if overlap_right is not None:
        pos_x = width - max(image_crop[3].shape[1], image_crop[1].shape[1])
        if shift_x[3] > 0 and shift_x[1] > 0:
            x = abs(shift_x[1] - shift_x[3])
            pos_x = width - max(shift_x[3], shift_x[1]) - max(image_crop[3].shape[1],
                                                              image_crop[1].shape[1]) + x

        if shift_y[1] > 0:
            # when the image 2 is moving from the position
            pos_y = pos_y + shift_y[1]
        merge_image_canvas[pos_y:pos_y + overlap_right.shape[0],
        pos_x:pos_x + overlap_right.shape[1]] = overlap_right

    overlap_rear, gradient = find_overlap_image_rear(image_crop, shift_x, shift_y)
    if overlap_rear is not None:
        if shift_y[2] > shift_y[3]:
            # when the image 3 more higher the image 4
            pos_y_2 = image_crop[0].shape[0] - shift_y[3]
        pos_x = image_crop[3].shape[1] - (shift_x[2] + shift_x[3]) + shift_x[2]
        merge_image_canvas[pos_y_2:pos_y_2 + overlap_rear.shape[0],
        pos_x: pos_x + overlap_rear.shape[1]] = overlap_rear

    return merge_image_canvas, bird_view
