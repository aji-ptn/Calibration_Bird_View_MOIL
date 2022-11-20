import cv2
import numpy as np

from .overlap_center_clicked import find_overlapping_front_left, find_overlapping_front_right, \
    find_overlapping_rear_left, find_overlapping_rear_right
from .crop_gradient_center_config import crop_for_gradient_front_left, crop_for_gradient_front_right, \
    crop_for_gradient_rear_left, crop_for_gradient_rear_right, crop_region
from .gradient_class import create_blending


def merge_image_4_camera_center_perspective(image_crop, destination_perspective, properties_image, gradient_mode):
    keys = list(properties_image)
    list_pos_image_1_front = destination_perspective["front"]

    list_pos_image_2_left = destination_perspective["left"]

    list_pos_image_3_right = destination_perspective["right"]

    list_pos_image_4_rear = destination_perspective["rear"]

    pos_image_1_front_left = list_pos_image_1_front[0]
    pos_image_1_front_right = list_pos_image_1_front[1]

    pos_image_2_left_front = list_pos_image_2_left[0]
    pos_image_2_left_rear = list_pos_image_2_left[3]

    pos_image_3_right_front = list_pos_image_3_right[1]
    pos_image_3_right_rear = list_pos_image_3_right[2]

    pos_image_4_rear_left = list_pos_image_4_rear[3]
    pos_image_4_rear_right = list_pos_image_4_rear[2]

    width = image_crop[0].shape[1]
    height = max(image_crop[1].shape[0], image_crop[2].shape[0]) + image_crop[3].shape[0]

    if pos_image_1_front_left[1] > pos_image_2_left_front[1] or pos_image_1_front_right[1] > pos_image_3_right_front[1]:
        dis = max(pos_image_1_front_right[1], pos_image_1_front_left[1])
        if dis == pos_image_1_front_left[1]:
            height = height + (pos_image_1_front_left[1] - pos_image_2_left_front[1])
        elif dis == pos_image_1_front_right[1]:
            height = height + (pos_image_1_front_right[1] - pos_image_3_right_front[1])

    # try with 2 images
    merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)

    if pos_image_1_front_right[0] is None or pos_image_1_front_right[0] == 0:
        pos_image_1_front_right[0] = image_crop[0].shape[1] - image_crop[2].shape[1]

    if pos_image_2_left_rear[1] is None or pos_image_2_left_rear[1] == 0:
        pos_image_2_left_rear[1] = merge_image_canvas.shape[0] - image_crop[3].shape[0]
        pos_image_4_rear_left[0] = 0

    image_1 = cv2.circle(image_crop[0].copy(), tuple(pos_image_1_front_left), radius=30, color=(0, 0, 255),
                         thickness=-1)
    image_1 = cv2.circle(image_1, tuple(pos_image_1_front_right), radius=30, color=(255, 0, 0), thickness=-1)
    image_2 = cv2.circle(image_crop[1].copy(), tuple(pos_image_2_left_front), radius=20, color=(0, 255, 0),
                         thickness=-1)
    image_2 = cv2.circle(image_2, tuple(pos_image_2_left_rear), radius=20, color=(0, 255, 0), thickness=-1)
    image_3 = cv2.circle(image_crop[2].copy(), tuple(pos_image_3_right_front), radius=20, color=(0, 255, 0),
                         thickness=-1)
    image_3 = cv2.circle(image_3, tuple(pos_image_3_right_rear), radius=20, color=(0, 255, 0), thickness=-1)
    image_4 = cv2.circle(image_crop[3].copy(), tuple(pos_image_4_rear_left), radius=20, color=(0, 255, 0), thickness=-1)
    image_4 = cv2.circle(image_4, tuple(pos_image_4_rear_right), radius=20, color=(0, 255, 0), thickness=-1)

    # draw_image_4_point(image_1, list_pos_image_1_front)
    # draw_image_4_point(image_2, list_pos_image_2_left)
    # draw_image_4_point(image_3, list_pos_image_3_right)
    # draw_image_4_point(image_4, list_pos_image_4_rear)

    # image front and image left
    shift_1_y = 0
    shift_1_x = 0
    shift_2_x = pos_image_1_front_left[0] - pos_image_2_left_front[0]
    shift_2_y = pos_image_1_front_left[1] - pos_image_2_left_front[1]

    start_2_x = 0
    start_2_y = 0
    if pos_image_2_left_front[1] > pos_image_1_front_left[1]:
        shift_2_y = 0
        start_2_y = pos_image_2_left_front[1] - pos_image_1_front_left[1]
    if pos_image_2_left_front[0] > pos_image_1_front_left[0]:
        shift_2_x = 0
        start_2_x = pos_image_2_left_front[0] - pos_image_1_front_left[0]

    # crop image 2
    image_2_crop = image_2.copy()[start_2_y:image_2.shape[0], start_2_x:image_2.shape[1]]

    # image_3 process
    shift_3_x = pos_image_1_front_right[0] - pos_image_3_right_front[0] + properties_image[keys[2]]["crop_left"]
    shift_3_y = pos_image_1_front_right[1] - pos_image_3_right_front[1]
    end_3_x = 0
    if pos_image_1_front_right[0] - pos_image_3_right_front[0] + image_3.shape[1] > image_1.shape[1]:
        end_3_x = pos_image_1_front_right[0] - pos_image_3_right_front[0] + image_3.shape[1] - image_1.shape[1] + \
                  properties_image[keys[2]]["crop_left"]

    if pos_image_3_right_front[1] > pos_image_1_front_right[1]:
        shift_3_y = 0
        start_2_y = pos_image_3_right_front[1] - pos_image_1_front_right[1]

    # crop image 3
    image_3_crop = image_3.copy()[start_2_y:image_3.shape[0], 0:image_3.shape[1] - end_3_x]

    # process image 4
    shift_4_x = pos_image_1_front_left[0] + pos_image_2_left_rear[0] - pos_image_2_left_front[0] - \
                pos_image_4_rear_left[0]
    shift_4_y = pos_image_1_front_left[1] + pos_image_2_left_rear[1] - pos_image_2_left_front[1] - \
                pos_image_4_rear_left[1]

    end_4_x = pos_image_1_front_left[0] + pos_image_2_left_rear[0] - pos_image_2_left_front[0] + image_4.shape[1] - \
              pos_image_4_rear_left[0] - image_1.shape[1]
    if end_4_x < 0:
        end_4_x = 0
    start_4_x = 0
    if pos_image_1_front_left[0] + pos_image_2_left_rear[0] - pos_image_2_left_front[0] < pos_image_4_rear_left[0]:
        start_4_x = pos_image_4_rear_left[0] - (
                pos_image_1_front_left[0] + pos_image_2_left_rear[0] - pos_image_2_left_front[0])
        shift_4_x = 0

    image_4_crop = image_4.copy()[0:image_4.shape[0], start_4_x:start_4_x + image_4.shape[1] - end_4_x]

    # merge all image
    if gradient_mode == "H":
        merge_image_canvas[shift_2_y:shift_2_y + image_2_crop.shape[0],
        shift_2_x:shift_2_x + image_2_crop.shape[1]] = image_2_crop
        merge_image_canvas[shift_3_y:shift_3_y + image_3_crop.shape[0],
        shift_3_x:shift_3_x + image_3_crop.shape[1]] = image_3_crop
        merge_image_canvas[shift_1_y:shift_1_y + image_crop[0].shape[0],
        shift_1_x:shift_1_x + image_crop[0].shape[1]] = image_1
        merge_image_canvas[shift_4_y:shift_4_y + image_4_crop.shape[0],
        shift_4_x:shift_4_x + image_4_crop.shape[1]] = image_4_crop
    else:
        merge_image_canvas[shift_1_y:shift_1_y + image_crop[0].shape[0],
        shift_1_x:shift_1_x + image_crop[0].shape[1]] = image_1
        merge_image_canvas[shift_4_y:shift_4_y + image_4_crop.shape[0],
        shift_4_x:shift_4_x + image_4_crop.shape[1]] = image_4_crop
        merge_image_canvas[shift_2_y:shift_2_y + image_2_crop.shape[0],
        shift_2_x:shift_2_x + image_2_crop.shape[1]] = image_2_crop
        merge_image_canvas[shift_3_y:shift_3_y + image_3_crop.shape[0],
        shift_3_x:shift_3_x + image_3_crop.shape[1]] = image_3_crop

    bird_view = merge_image_canvas.copy()

    overlap_front_left, front_left_ov, left_front_ov = find_overlapping_front_left(image_1, image_2,
                                                                                   pos_image_1_front_left,
                                                                                   pos_image_2_left_front)
    if overlap_front_left is not None:
        pos_ov_x = shift_2_x
        pos_ov_y = shift_2_y
        if pos_image_2_left_front[1] > pos_image_1_front_left[1]:
            pos_ov_y = 0
        if pos_image_2_left_front[0] > pos_image_1_front_left[0]:
            pos_ov_x = 0
        merge_image_canvas[pos_ov_y:pos_ov_y + overlap_front_left.shape[0],
        pos_ov_x:pos_ov_x + overlap_front_left.shape[1]] = overlap_front_left

        pos_fl_x = 0
        pos_fl_y = 0
        if gradient_mode != "O":
            if gradient_mode == "D":
                pos_fl_x, pos_fl_y, front_left_ov, left_front_ov = crop_for_gradient_front_left(front_left_ov,
                                                                                                left_front_ov)
            front_left_ov = crop_region(front_left_ov, "front_left", gradient_mode)
            left_front_ov = crop_region(left_front_ov, "left_front", gradient_mode)
            blending_front_left = create_blending(front_left_ov, left_front_ov)
        else:
            blending_front_left = overlap_front_left
        try:
            bird_view[pos_ov_y + pos_fl_y:pos_ov_y + pos_fl_y + blending_front_left.shape[0],
            pos_ov_x + pos_fl_x: pos_ov_x + pos_fl_x + blending_front_left.shape[1]] = blending_front_left
        except:
            pass

    overlap_front_right, front_right_ov, right_front_ov = find_overlapping_front_right(image_1, image_3,
                                                                                       pos_image_1_front_right,
                                                                                       pos_image_3_right_front,
                                                                                       properties_image[keys[2]]["crop_left"])
    if overlap_front_right is not None:
        pos_ov_x = shift_3_x
        pos_ov_y = shift_3_y
        if pos_image_3_right_front[1] > pos_image_1_front_right[1]:
            pos_ov_y = 0
        if pos_image_3_right_front[0] > pos_image_1_front_right[0]:
            pos_ov_x = 0
        merge_image_canvas[pos_ov_y:pos_ov_y + overlap_front_right.shape[0],
        pos_ov_x:pos_ov_x + overlap_front_right.shape[1]] = overlap_front_right

        pos_fl_y = 0
        if gradient_mode != "O":
            if gradient_mode == "D":
                _, pos_fl_y, front_right_ov, right_front_ov = crop_for_gradient_front_right(front_right_ov,
                                                                                            right_front_ov)
            front_right_ov = crop_region(front_right_ov, "front_right", gradient_mode)
            right_front_ov = crop_region(right_front_ov, "right_front", gradient_mode)
            blending_front_right = create_blending(front_right_ov, right_front_ov)
        else:
            blending_front_right = overlap_front_right
        try:
            bird_view[pos_ov_y + pos_fl_y:pos_ov_y + pos_fl_y + blending_front_right.shape[0],
            pos_ov_x: pos_ov_x + blending_front_right.shape[1]] = blending_front_right
        except:
            pass

    overlap_rear_left, left_rear_ov, rear_left_ov = find_overlapping_rear_left(image_2, image_2_crop, image_4,
                                                                               image_4_crop, pos_image_2_left_rear,
                                                                               pos_image_2_left_front,
                                                                               pos_image_1_front_left,
                                                                               pos_image_4_rear_left)
    if overlap_rear_left is not None:
        pos_ov_x = shift_4_x
        pos_ov_y = shift_4_y
        if pos_image_2_left_rear[0] < pos_image_4_rear_left[0]:
            pos_ov_x = shift_2_x
        merge_image_canvas[pos_ov_y:pos_ov_y + overlap_rear_left.shape[0],
        pos_ov_x:pos_ov_x + overlap_rear_left.shape[1]] = overlap_rear_left

        pos_fl_x = 0
        if gradient_mode != "O":
            if gradient_mode == "D":
                pos_fl_x, _, left_rear_ov, rear_left_ov = crop_for_gradient_rear_left(left_rear_ov, rear_left_ov)
            left_rear_ov = crop_region(left_rear_ov, "left_rear", gradient_mode)
            rear_left_ov = crop_region(rear_left_ov, "rear_left", gradient_mode)
            blending_rear_left = create_blending(left_rear_ov, rear_left_ov)
        else:
            blending_rear_left = overlap_rear_left
        try:
            bird_view[pos_ov_y:pos_ov_y + blending_rear_left.shape[0],
            pos_ov_x + pos_fl_x: pos_ov_x + pos_fl_x + blending_rear_left.shape[1]] = blending_rear_left
        except:
            pass

    overlap_rear_right, right_rear_ov, rear_right_ov = find_overlapping_rear_right(image_3_crop, image_4_crop,
                                                                                   pos_image_3_right_front,
                                                                                   pos_image_4_rear_left,
                                                                                   pos_image_2_left_rear,
                                                                                   pos_image_2_left_front,
                                                                                   pos_image_1_front_right,
                                                                                   pos_image_1_front_left)
    if overlap_rear_right is not None:
        pos_ov_x = shift_3_x
        pos_ov_y = shift_4_y
        merge_image_canvas[pos_ov_y:pos_ov_y + overlap_rear_right.shape[0],
        pos_ov_x:pos_ov_x + overlap_rear_right.shape[1]] = overlap_rear_right

        if gradient_mode != "O":
            if gradient_mode == "D":
                _, _, right_rear_ov, rear_right_ov = crop_for_gradient_rear_right(right_rear_ov, rear_right_ov)
            right_rear_ov = crop_region(right_rear_ov, "right_rear", gradient_mode)
            rear_right_ov = crop_region(rear_right_ov, "rear_right", gradient_mode)
            blending_rear_right = create_blending(right_rear_ov, rear_right_ov)
        else:
            blending_rear_right = overlap_rear_right
        try:
            bird_view[pos_ov_y:pos_ov_y + blending_rear_right.shape[0],
            pos_ov_x:pos_ov_x + blending_rear_right.shape[1]] = blending_rear_right
        except:
            pass

        start_x = max(shift_1_x, shift_2_x, shift_4_x)
        bird_view = bird_view[0:shift_4_y + image_4.shape[0],
                    start_x: min(shift_4_x + image_4_crop.shape[1],
                                 shift_3_x + image_3_crop.shape[1])]
    return merge_image_canvas, bird_view


def draw_image_4_point(image, list_point):
    pts = np.array(list_point, np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(image, [pts], True, (0, 255, 255), 10)
