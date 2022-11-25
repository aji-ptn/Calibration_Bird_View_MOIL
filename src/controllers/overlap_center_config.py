import cv2
from . import crop_gradient_center_config  # import crop_region
from .gradient_class import create_blending


def find_overlap_front_left_center(image, shift_x, shift_y, properties_image):
    """

    Args:
        image:
        shift_x:
        shift_y:
        properties_image:

    Returns:

    """
    if shift_y[1] - properties_image["Image_2"]["crop_top"] > 0:
        # crop left and right front is still some problems exist
        pos_y_bg_start = image[0].shape[0] - shift_y[1] + properties_image["Image_2"]["crop_top"]
        pos_y_bg_finish = image[0].shape[0]
        pos_x_bg_start = 0
        pos_x_bg_finish = image[1].shape[1] - 500 + shift_x[1] - properties_image["Image_1"]["crop_left"]

        pos_y_fg_start = 0
        pos_y_fg_finish = shift_y[1] - properties_image["Image_2"]["crop_top"]
        pos_x_fg_start = 500 - shift_x[1] + properties_image["Image_1"]["crop_left"]
        pos_x_fg_finish = pos_x_fg_start + image[1].shape[1]

        if shift_x[1] > 500:
            pos_x_bg_start = abs(500 - shift_x[1])
            pos_x_bg_finish = pos_x_bg_start + image[1].shape[1]

            pos_x_fg_start = 0
            pos_x_fg_finish = image[1].shape[1]

        bg_image = image[0][pos_y_bg_start: pos_y_bg_finish, pos_x_bg_start:pos_x_bg_finish]
        fg_image = image[1][pos_y_fg_start: pos_y_fg_finish, pos_x_fg_start:pos_x_fg_finish]
        overlay = cv2.addWeighted(bg_image, 0.5, fg_image, 0.5, 0)
        # try:
        #     bg_image = crop_gradient_center_config.crop_region(bg_image, "front_left")
        #     fg_image = crop_gradient_center_config.crop_region(fg_image, "left_front")
        #     blending = create_blending(bg_image, fg_image)
        # except:
        #     blending = None

    else:
        overlay = None
        # blending = None
        bg_image = None
        fg_image = None

    return overlay, bg_image, fg_image


def find_overlap_front_right_center(image, shift_x, shift_y, properties_image):
    """

    Args:
        image:
        shift_x:
        shift_y:
        properties_image:

    Returns:

    """
    if shift_y[2] - properties_image["Image_3"]["crop_top"] > 0:
        pos_y_bg_start = image[0].shape[0] - shift_y[2] + properties_image["Image_3"]["crop_top"]
        pos_y_bg_finish = image[0].shape[0]
        pos_x_bg_start = image[0].shape[1] - image[2].shape[1] + properties_image["Image_1"]["crop_right"] + 500 + \
                         shift_x[2]
        pos_x_bg_finish = image[0].shape[1]

        pos_y_fg_start = 0
        pos_y_fg_finish = shift_y[2] - properties_image["Image_3"]["crop_top"]
        pos_x_fg_start = 0
        pos_x_fg_finish = image[2].shape[1] - 500 - shift_x[2] - properties_image["Image_1"]["crop_right"]

        if shift_x[2] < -500:
            pos_x_bg_start = image[0].shape[1] - image[2].shape[1] - abs(500 + shift_x[2])
            pos_x_bg_finish = pos_x_bg_start + image[2].shape[1]

            pos_x_fg_start = 0
            pos_x_fg_finish = image[2].shape[1]

        bg_image = image[0][pos_y_bg_start: pos_y_bg_finish, pos_x_bg_start:pos_x_bg_finish]
        fg_image = image[2][pos_y_fg_start: pos_y_fg_finish, pos_x_fg_start:pos_x_fg_finish]
        overlay = cv2.addWeighted(bg_image, 0.5, fg_image, 0.5, 0)
        # try:
        #     bg_image = crop_gradient_center_config.crop_region(bg_image, "front_right")
        #     fg_image = crop_gradient_center_config.crop_region(fg_image, "right_front")
        #     blending = create_blending(bg_image, fg_image)
        # except:
        #     blending = None

    else:
        overlay = None
        # blending = None
        bg_image = None
        fg_image = None

    return overlay, bg_image, fg_image


def rear_image_overlap(image, shift_x, shift_y, properties_image):
    """

    Args:
        image:
        shift_x:
        shift_y:
        properties_image:

    Returns:

    """
    total_off_img_2 = properties_image["Image_2"]["crop_top"] + properties_image["Image_2"]["crop_bottom"] + shift_y[1]
    total_off_img_3 = properties_image["Image_3"]["crop_top"] + properties_image["Image_3"]["crop_bottom"] + shift_y[2]
    offset = total_off_img_2 - total_off_img_3

    # Rear left image begin here ##############################################################################
    pos_y_left_start = image[1].shape[0] - shift_y[3]
    pos_y_left_finish = image[1].shape[0]
    pos_x_left_start = 500 - shift_x[1] + shift_x[3] + properties_image["Image_4"]["crop_left"]
    pos_x_left_finish = image[1].shape[1]

    pos_y_rear_left_start = 0
    pos_y_rear_left_finish = shift_y[3]
    pos_x_rear_left_start = 0
    pos_x_rear_left_finish = image[1].shape[1] - 500 + shift_x[1] - shift_x[3] - properties_image["Image_4"][
        "crop_left"]

    if shift_x[1] - shift_x[3] > 500:
        pos_x_left_start = 0
        pos_x_left_finish = image[1].shape[1]

        pos_x_rear_left_start = abs(500 - shift_x[1]) - shift_x[3]
        pos_x_rear_left_finish = abs(500 - shift_x[1]) - shift_x[3] + image[1].shape[1]

    # Begin for right image ###########################################################################################
    pos_y_right_start = image[2].shape[0] - shift_y[3]  # + properties_image["Image_3"]["crop_top"]
    pos_y_right_finish = image[2].shape[0]
    pos_x_right_start = 0
    pos_x_right_finish = image[2].shape[1] - 500 - shift_x[2] + shift_x[3] - properties_image["Image_4"]["crop_right"]

    pos_y_rear_right_start = 0
    pos_y_rear_right_finish = shift_y[3]  # - properties_image["Image_3"]["crop_top"]
    pos_x_rear_right_start = image[3].shape[1] - image[2].shape[1] + 500 + shift_x[2] - shift_x[3] + \
                             properties_image["Image_4"]["crop_right"]
    pos_x_rear_right_finish = image[3].shape[1]

    # if shift_x[2] < -500:
    #     pos_x_right_start = 0
    #     pos_x_right_finish = image[2].shape[1]
    #
    #     pos_x_rear_right_start = image[3].shape[1] - image[2].shape[1] - abs(500 + shift_x[2]) - shift_x[3]
    #     pos_x_rear_right_finish = pos_x_rear_right_start + image[2].shape[1]

    if total_off_img_2 > total_off_img_3:
        pos_y_right_start = image[2].shape[0] - shift_y[3] - abs(offset) - \
                            properties_image["Image_3"]["crop_top"] + \
                            properties_image["Image_2"]["crop_top"]

        pos_y_rear_right_finish = shift_y[3] + abs(offset) + \
                                  properties_image["Image_3"]["crop_top"] - \
                                  properties_image["Image_2"]["crop_top"]

    elif total_off_img_2 < total_off_img_3:
        pos_y_left_start = image[1].shape[0] - shift_y[3] - abs(offset) - \
                           properties_image["Image_2"]["crop_top"] + \
                           properties_image["Image_3"]["crop_top"]
        pos_y_rear_left_finish = shift_y[3] + abs(offset) + \
                                 properties_image["Image_2"]["crop_top"] - \
                                 properties_image["Image_3"]["crop_top"]

    left_image = image[1][pos_y_left_start: pos_y_left_finish, pos_x_left_start:pos_x_left_finish]
    rear_left_image = image[3][pos_y_rear_left_start: pos_y_rear_left_finish,
                      pos_x_rear_left_start:pos_x_rear_left_finish]
    overlay_left_rear = cv2.addWeighted(left_image, 0.5, rear_left_image, 0.5, 0)

    # try:
    #     left_image = crop_gradient_center_config.crop_region(left_image, "left_rear")
    #     rear_image = crop_gradient_center_config.crop_region(rear_left_image, "rear_left")
    #     blending_left_rear = create_blending(left_image, rear_image)
    # except:
    #     blending_left_rear = None
    #     left_image = None
    #     rear_left_image = None
    try:
        right_image = image[2][pos_y_right_start: pos_y_right_finish, pos_x_right_start:pos_x_right_finish]
        rear_right_image = image[3][pos_y_rear_right_start: pos_y_rear_right_finish, pos_x_rear_right_start:
                                                                                     pos_x_rear_right_finish]
        overlay_right_rear = cv2.addWeighted(right_image, 0.5, rear_right_image, 0.5, 0)
    except:
        overlay_right_rear = None
        right_image = None
        rear_right_image = None

    # try:
    #     right_image = crop_gradient_center_config.crop_region(right_image, "right_rear")
    #     rear_image = crop_gradient_center_config.crop_region(rear_right_image, "rear_right")
    #     blending_right_rear = create_blending(right_image, rear_image)
    # except:
    #     blending_right_rear = None
    #     right_image = None
    #     rear_image = None

    # blending_left_rear, blending_right_rear = None, None

    return overlay_left_rear, overlay_right_rear, left_image, rear_left_image, right_image, rear_right_image

