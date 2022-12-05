import cv2
import numpy as np
from .overlap_center_config import *
from .gradient_class import create_blending
from .crop_gradient_center_config import crop_for_gradient_front_left, crop_for_gradient_front_right, \
    crop_for_gradient_rear_left, crop_for_gradient_rear_right, crop_region


def merge_image_4_camera_center_config(image_crop, properties_image, shift_x, shift_y, gradient_mode, sources="Image"):
    keys = list(properties_image)

    # create canvas for showing image
    height = image_crop[0].shape[0] \
             + min(image_crop[1].shape[0] - shift_y[1] + properties_image[keys[1]]["crop_top"],
                   image_crop[2].shape[0] - shift_y[2] + properties_image[keys[2]]["crop_top"]) \
             + image_crop[3].shape[0] - shift_y[3]

    width = max(image_crop[0].shape[1], image_crop[3].shape[1]) + 1000

    merge_image_canvas = np.zeros([height, width, 3], dtype=np.uint8)

    # determine the position of image on the canvas
    pos_x_0 = 500 + properties_image[keys[0]]["crop_left"]
    pos_y_0 = 0

    pos_x_1 = shift_x[1]
    pos_y_1 = image_crop[0].shape[0] - shift_y[1] + properties_image[keys[1]]["crop_top"]

    pos_x_2 = width - image_crop[2].shape[1] + shift_x[2]
    pos_y_2 = image_crop[0].shape[0] - shift_y[2] + properties_image[keys[2]]["crop_top"]

    pos_x_3 = 500 + properties_image[keys[3]]["crop_left"] + shift_x[3]
    pos_y_3 = image_crop[0].shape[0] + min(image_crop[1].shape[0] - shift_y[1] +
                                           properties_image[keys[1]]["crop_top"],
                                           image_crop[2].shape[0] - shift_y[2] +
                                           properties_image[keys[2]]["crop_top"]) - shift_y[3]

    # merge the image to the canvas
    if gradient_mode == "H":
        merge_image_canvas[pos_y_1:pos_y_1 + image_crop[1].shape[0],
        pos_x_1:pos_x_1 + image_crop[1].shape[1]] = image_crop[1]

        merge_image_canvas[pos_y_2:pos_y_2 + image_crop[2].shape[0],
        pos_x_2:pos_x_2 + image_crop[2].shape[1]] = image_crop[2]

        merge_image_canvas[pos_y_0:pos_y_0 + image_crop[0].shape[0],
        pos_x_0:pos_x_0 + image_crop[0].shape[1]] = image_crop[0]

        merge_image_canvas[pos_y_3:pos_y_3 + image_crop[3].shape[0],
        pos_x_3:pos_x_3 + image_crop[3].shape[1]] = image_crop[3]
    else:
        merge_image_canvas[pos_y_0:pos_y_0 + image_crop[0].shape[0],
        pos_x_0:pos_x_0 + image_crop[0].shape[1]] = image_crop[0]

        merge_image_canvas[pos_y_3:pos_y_3 + image_crop[3].shape[0],
        pos_x_3:pos_x_3 + image_crop[3].shape[1]] = image_crop[3]

        merge_image_canvas[pos_y_1:pos_y_1 + image_crop[1].shape[0],
        pos_x_1:pos_x_1 + image_crop[1].shape[1]] = image_crop[1]

        merge_image_canvas[pos_y_2:pos_y_2 + image_crop[2].shape[0],
        pos_x_2:pos_x_2 + image_crop[2].shape[1]] = image_crop[2]

    bird_view = merge_image_canvas.copy()
    # image overlay
    overlap_front_left, front_left_ov, left_front_ov = find_overlap_front_left_center(image_crop, shift_x, shift_y,
                                                                                      properties_image)
    if overlap_front_left is not None:
        if shift_x[1] - shift_x[3] > 500:
            pos_x_0 = shift_x[1]
        merge_image_canvas[pos_y_1:pos_y_1 + overlap_front_left.shape[0],
        pos_x_0: pos_x_0 + overlap_front_left.shape[1]] = overlap_front_left

        pos_fl_x = 0
        pos_fl_y = 0
        if gradient_mode != "O":
            if gradient_mode == "D":
                pos_fl_x, pos_fl_y, front_left_ov, left_front_ov = crop_for_gradient_front_left(front_left_ov,
                                                                                                left_front_ov)
            front_left_ov = crop_region(front_left_ov, "front_left", gradient_mode)
            left_front_ov = crop_region(left_front_ov, "left_front", gradient_mode)
            try:
                blending_front_left = create_blending(front_left_ov, left_front_ov)
            except:
                blending_front_left = overlap_front_left
        else:
            blending_front_left = overlap_front_left
        try:
            bird_view[pos_y_1 + pos_fl_y:pos_y_1 + pos_fl_y + blending_front_left.shape[0],
            pos_x_0 + pos_fl_x: pos_x_0 + pos_fl_x + blending_front_left.shape[1]] = blending_front_left
        except:
            pass

    overlap_front_right, front_right_ov, right_front_ov = find_overlap_front_right_center(image_crop, shift_x, shift_y,
                                                                                          properties_image)
    if overlap_front_right is not None:
        merge_image_canvas[pos_y_2:pos_y_2 + overlap_front_right.shape[0],
        pos_x_2: pos_x_2 + overlap_front_right.shape[1]] = overlap_front_right

        pos_fr_y = 0
        if gradient_mode != "O":
            if gradient_mode == "D":
                _, pos_fr_y, front_right_ov, right_front_ov = crop_for_gradient_front_right(front_right_ov,
                                                                                            right_front_ov)
            front_right_ov = crop_region(front_right_ov, "front_right", gradient_mode)
            right_front_ov = crop_region(right_front_ov, "right_front", gradient_mode)
            try:
                blending_front_right = create_blending(front_right_ov, right_front_ov)
            except:
                blending_front_right = overlap_front_right
        else:
            blending_front_right = overlap_front_right
        try:
            bird_view[pos_y_2 + pos_fr_y:pos_y_2 + pos_fr_y + blending_front_right.shape[0],
            pos_x_2: pos_x_2 + blending_front_right.shape[1]] = blending_front_right
        except:
            pass

    overlap_left_rear, overlap_right_rear, left_rear_ov, rear_left_ov, right_rear_ov, rear_right_ov = rear_image_overlap \
        (image_crop, shift_x,
         shift_y,
         properties_image)

    if overlap_left_rear is not None:
        if shift_x[1] - shift_x[3] > 500:
            pos_x_3 = pos_x_1
        merge_image_canvas[pos_y_3:pos_y_3 + overlap_left_rear.shape[0],
        pos_x_3: pos_x_3 + overlap_left_rear.shape[1]] = overlap_left_rear

        pos_fl_x = 0
        if gradient_mode != "O":
            if gradient_mode == "D":
                pos_fl_x, _, left_rear_ov, rear_left_ov = crop_for_gradient_rear_left(left_rear_ov, rear_left_ov)
            left_rear_ov = crop_region(left_rear_ov, "left_rear", gradient_mode)
            rear_left_ov = crop_region(rear_left_ov, "rear_left", gradient_mode)
            try:
                blending_rear_left = create_blending(left_rear_ov, rear_left_ov)
            except:
                blending_rear_left = overlap_left_rear
        else:
            blending_rear_left = overlap_left_rear
        try:
            bird_view[pos_y_3:pos_y_3 + blending_rear_left.shape[0],
            pos_x_3 + pos_fl_x: pos_x_3 + pos_fl_x + blending_rear_left.shape[1]] = blending_rear_left
        except:
            pass

    if overlap_right_rear is not None:
        merge_image_canvas[pos_y_3:pos_y_3 + overlap_right_rear.shape[0],
        pos_x_2: pos_x_2 + overlap_right_rear.shape[1]] = overlap_right_rear

        if gradient_mode != "O":
            if gradient_mode == "D":
                _, _, right_rear_ov, rear_right_ov = crop_for_gradient_rear_right(right_rear_ov, rear_right_ov)
            right_rear_ov = crop_region(right_rear_ov, "right_rear", gradient_mode)
            rear_right_ov = crop_region(rear_right_ov, "rear_right", gradient_mode)
            try:
                blending_rear_right = create_blending(right_rear_ov, rear_right_ov)
            except:
                blending_rear_right = overlap_right_rear
        else:
            blending_rear_right = overlap_right_rear
        try:
            bird_view[pos_y_3:pos_y_3 + blending_rear_right.shape[0],
            pos_x_2: pos_x_2 + blending_rear_right.shape[1]] = blending_rear_right
        except:
            pass

    try:
        bird_view = bird_view[0:0 + merge_image_canvas.shape[0],
                    max(500, shift_x[1], 500 + shift_x[3]): merge_image_canvas.shape[1] - (max(500, abs(shift_x[2]),
                                                                                               500 + shift_x[3]))]

        # bird_view = bird_view[image_crop[0].shape[0] - min(shift_y[1], shift_y[2]):image_crop[0].shape[0] - min(shift_y[1], shift_y[2]) + merge_image_canvas.shape[0],
        #             max(500, shift_x[1], 500 + shift_x[3]): merge_image_canvas.shape[1] - (
        #                 max(500, abs(shift_x[2]), 500 + shift_x[3]))]
    except:
        print("crop error")

    return merge_image_canvas, bird_view
