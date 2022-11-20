import numpy as np
from .overlap_corner_config import *


def merge_image_6_camera_corner_config(image_crop, shift_x, shift_y):
    # create canvas image
    height = max(image_crop[0].shape[0], image_crop[1].shape[0]) \
             + max(image_crop[2].shape[0], image_crop[3].shape[0]) \
             + max(image_crop[4].shape[0], image_crop[5].shape[0]) - min(shift_y[4], shift_y[5])
    width = max((image_crop[0].shape[1] + image_crop[1].shape[1]),
                (image_crop[2].shape[1] + image_crop[3].shape[1]),
                (image_crop[4].shape[1] + image_crop[5].shape[1]))
    merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)

    # determine position image 1
    pos_x_0 = shift_x[0]
    pos_y_0 = abs(shift_y[1]) + shift_y[0] if shift_y[1] <= 0 else shift_y[0]

    # determine position image 2
    if shift_x[1] < 0:
        shift_x[1] = 0
    pos_x_1 = image_crop[0].shape[1] - shift_x[1] + shift_x[0]  # initial position in width image_crop[0]
    pos_y_1 = 0 if shift_y[1] <= 0 else shift_y[1]

    # update the information of shift x from image 1 and image 2
    shift_y[0] = pos_y_0
    shift_y[1] = pos_y_1

    # determine position image 3
    pos_x_2 = shift_x[2]
    if shift_y[2] < 0:
        shift_y[2] = 0
    pos_y_2 = image_crop[0].shape[0] - shift_y[2]

    # determine position image 4
    pos_x_3 = width - image_crop[3].shape[1] - shift_x[3]
    pos_y_3 = image_crop[1].shape[0] - shift_y[3]

    # determine position image 5
    pos_x_4 = shift_x[4]
    pos_y_4 = image_crop[0].shape[0] + image_crop[2].shape[0] - shift_y[4]

    # determine position image 6
    pos_x_5 = width - image_crop[5].shape[1] - shift_x[5]
    pos_y_5 = image_crop[1].shape[0] + image_crop[3].shape[0] - shift_y[5]

    if shift_x[2] < 0 and shift_x[4] >= 0:  # if value x in image 3 is minus
        width = abs(shift_x[2]) + max((image_crop[0].shape[1] + image_crop[1].shape[1]),
                                      (image_crop[2].shape[1] + image_crop[3].shape[1]),
                                      (image_crop[4].shape[1] + image_crop[5].shape[1]))
        merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)
        pos_x_0 = shift_x[0] + abs(shift_x[2])
        pos_x_1 = image_crop[0].shape[1] - shift_x[1] + shift_x[0] + abs(shift_x[2])
        pos_x_2 = 0
        pos_x_3 = width - image_crop[3].shape[1] - shift_x[3]
        pos_x_4 = shift_x[4] + abs((shift_x[2]))
        pos_x_5 = width - image_crop[5].shape[1] - shift_x[5]

    elif shift_x[4] < 0 and shift_x[2] >= 0:  # if value x in image 5 is minus
        width = abs(shift_x[4]) + max((image_crop[0].shape[1] + image_crop[1].shape[1]),
                                      (image_crop[2].shape[1] + image_crop[3].shape[1]),
                                      (image_crop[4].shape[1] + image_crop[5].shape[1]))
        merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)
        pos_x_0 = shift_x[0] + abs(shift_x[4])
        pos_x_1 = image_crop[0].shape[1] - shift_x[1] + shift_x[0] + abs(shift_x[4])
        pos_x_2 = shift_x[2] + abs(shift_x[4])
        pos_x_3 = width - image_crop[3].shape[1] - shift_x[3]
        pos_x_4 = 0
        pos_x_5 = width - image_crop[5].shape[1] - shift_x[5]

    elif shift_x[2] < 0 and shift_x[4] < 0:
        if shift_x[2] < shift_x[4]:
            width = abs(shift_x[2]) + max((image_crop[0].shape[1] + image_crop[1].shape[1]),
                                          (image_crop[2].shape[1] + image_crop[3].shape[1]),
                                          (image_crop[4].shape[1] + image_crop[5].shape[1]))
            merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)
            pos_x_0 = shift_x[0] + abs(shift_x[2])
            pos_x_1 = image_crop[0].shape[1] - shift_x[1] + shift_x[0] + abs(shift_x[2])
            pos_x_2 = 0
            pos_x_3 = width - image_crop[3].shape[1] - shift_x[3]
            pos_x_4 = shift_x[4] + abs((shift_x[2]))
            pos_x_5 = width - image_crop[5].shape[1] - shift_x[5]
        elif shift_x[4] < shift_x[2]:
            width = abs(shift_x[4]) + max((image_crop[0].shape[1] + image_crop[1].shape[1]),
                                          (image_crop[2].shape[1] + image_crop[3].shape[1]),
                                          (image_crop[4].shape[1] + image_crop[5].shape[1]))
            merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)
            pos_x_0 = shift_x[0] + abs(shift_x[4])
            pos_x_1 = image_crop[0].shape[1] - shift_x[1] + shift_x[0] + abs(shift_x[4])
            pos_x_2 = shift_x[2] + abs(shift_x[4])
            pos_x_3 = width - image_crop[3].shape[1] - shift_x[3]
            pos_x_4 = 0
            pos_x_5 = width - image_crop[5].shape[1] - shift_x[5]

    if shift_x[3] < 0 and shift_x[5] >= 0:  # if value x in image 4 is minus
        width = width + abs(shift_x[3])
        merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)

        pos_x_3 = width - image_crop[3].shape[1]

    if shift_x[5] < 0 and shift_x[3] >= 0:  # if value x in image 6 is minus
        width = width + abs(shift_x[5])
        merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)

        pos_x_5 = width - image_crop[5].shape[1]

    if shift_x[3] < 0 and shift_x[5] < 0:
        if shift_x[3] < shift_x[5]:
            width = width + abs(shift_x[3])
            merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)

            pos_x_3 = width - image_crop[3].shape[1]
        else:
            width = width + abs(shift_x[5])
            merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)

            pos_x_5 = width - image_crop[5].shape[1]

    # merge image
    merge_image_canvas[pos_y_0:pos_y_0 + image_crop[0].shape[0],
    pos_x_0:pos_x_0 + image_crop[0].shape[1]] = image_crop[0]

    merge_image_canvas[pos_y_1:pos_y_1 + image_crop[1].shape[0],
    pos_x_1:pos_x_1 + image_crop[1].shape[1]] = image_crop[1]

    merge_image_canvas[pos_y_4:pos_y_4 + image_crop[4].shape[0],
    pos_x_4:pos_x_4 + image_crop[4].shape[1]] = image_crop[4]

    merge_image_canvas[pos_y_5:pos_y_5 + image_crop[5].shape[0],
    pos_x_5:pos_x_5 + image_crop[5].shape[1]] = image_crop[5]

    merge_image_canvas[pos_y_2:pos_y_2 + image_crop[2].shape[0],
    pos_x_2:pos_x_2 + image_crop[2].shape[1]] = image_crop[2]

    merge_image_canvas[pos_y_3:pos_y_3 + image_crop[3].shape[0],
    pos_x_3:pos_x_3 + image_crop[3].shape[1]] = image_crop[3]

    bird_view = merge_image_canvas.copy()

    # image overlay
    pos_x, overlap_front, gradient = find_overlap_image_front(image_crop, shift_x, shift_y)
    if overlap_front is not None:
        if shift_x[2] < 0:
            pos_x = pos_x_1
        merge_image_canvas[pos_y_0 + pos_y_1:pos_y_0 + pos_y_1 + overlap_front.shape[0],
        pos_x:pos_x + overlap_front.shape[1]] = overlap_front
        if gradient is not None:
            bird_view[pos_y_0 + pos_y_1:pos_y_0 + pos_y_1 + gradient.shape[0],
            pos_x:pos_x + gradient.shape[1]] = gradient

    overlap_rear, gradient_rear = find_overlap_image_rear(image_crop, shift_x, shift_y, total_cam=6)
    if overlap_rear is not None:
        pos_y = max(pos_y_4, pos_y_5)
        pos_x = pos_x_5
        merge_image_canvas[pos_y:pos_y + overlap_rear.shape[0],
        pos_x: pos_x + overlap_rear.shape[1]] = overlap_rear
        if gradient_rear is not None:
            bird_view[pos_y:pos_y + gradient_rear.shape[0],
            pos_x: pos_x + gradient_rear.shape[1]] = gradient_rear

    # overlap for image front and left (center)
    pos_y, overlap_left, gradient = find_overlap_image_front_left(image_crop, shift_x, shift_y, total_cam=6)
    if overlap_left is not None:
        pos_x = abs(shift_x[2])
        if shift_x[2] < 0 and shift_x[4] < 0:
            if shift_x[2] < shift_x[4]:
                pos_x = abs(shift_x[2])
            else:
                pos_x = abs(shift_x[4])

        if shift_y[0] > 0:
            # when the image 1 is moving from the position
            pos_y = pos_y + shift_y[0]
        merge_image_canvas[pos_y:pos_y + overlap_left.shape[0],
        pos_x:pos_x + overlap_left.shape[1]] = overlap_left
        if gradient is not None:
            bird_view[pos_y:pos_y + gradient.shape[0],
            pos_x:pos_x + gradient.shape[1]] = gradient

    # overlap for image front and right (center)
    pos_y, overlap_right, gradient = find_overlap_image_front_right_6_view(image_crop, shift_x, shift_y)
    if overlap_right is not None:
        pos_x = pos_x_3
        if shift_y[1] > 0:
            pos_y = pos_y_3
        merge_image_canvas[pos_y:pos_y + overlap_right.shape[0],
        pos_x:pos_x + overlap_right.shape[1]] = overlap_right
        if gradient is not None:
            bird_view[pos_y:pos_y + gradient.shape[0],
            pos_x:pos_x + gradient.shape[1]] = gradient

    overlap_rear_left, blending = find_overlap_image_rear_left_6_view(image_crop, shift_x, shift_y)
    if overlap_rear_left is not None:
        pos_x_rear_left = pos_x_4
        pos_y_rear_left = pos_y_4
        if shift_x[2] > shift_x[4]:
            pos_x_rear_left = pos_x_2
        if overlap_rear_left is not None:
            merge_image_canvas[pos_y_rear_left:pos_y_rear_left + overlap_rear_left.shape[0],
            pos_x_rear_left:pos_x_rear_left + overlap_rear_left.shape[1]] = overlap_rear_left
        if blending is not None:
            bird_view[pos_y_rear_left:pos_y_rear_left + blending.shape[0],
            pos_x_rear_left:pos_x_rear_left + blending.shape[1]] = blending

    overlap_rear_right, blending = find_overlap_image_rear_right_6_view(image_crop, shift_x, shift_y)
    if overlap_rear_right is not None:
        pos_x_rear_right = pos_x_3
        pos_y_rear_right = pos_y_5
        if overlap_rear_right is not None:
            merge_image_canvas[pos_y_rear_right:pos_y_rear_right + overlap_rear_right.shape[0],
            pos_x_rear_right:pos_x_rear_right + overlap_rear_right.shape[1]] = overlap_rear_right
        if blending is not None:
            bird_view[pos_y_rear_right:pos_y_rear_right + blending.shape[0],
            pos_x_rear_right:pos_x_rear_right + blending.shape[1]] = blending

    try:
        merge_image_canvas = merge_image_canvas[0:merge_image_canvas.shape[0],
                             0 : merge_image_canvas.shape[1] - min(shift_x[1], shift_x[3], shift_x[5])]
    except:
        print("crop error")
    try:
        bird_view = bird_view[max(shift_y[1], shift_y[0]):bird_view.shape[0] - abs(abs(shift_y[4]) - abs(shift_y[5])),
                    max(pos_x_2, pos_x_4, pos_x_0): bird_view.shape[1] - max(shift_x[1], shift_x[3], shift_x[5])]
    except:
        print("crop error")

    return merge_image_canvas, bird_view
