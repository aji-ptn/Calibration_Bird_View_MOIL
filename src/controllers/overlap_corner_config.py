import cv2
from .crop_gradient_corner_config import crop_region  # import crop_region
from .gradient_class import create_blending


def find_overlap_image_front_left(image, shift_x, shift_y, total_cam=4):
    """
    corner
    Args:
        total_cam:
        image:
        shift_x:
        shift_y:

    Returns:

    """
    if shift_y[0] > 0 or shift_y[2] > 0:
        pos_y_bg_start = image[0].shape[0] - shift_y[0] - shift_y[2]
        pos_y_bg_finish = image[0].shape[0]
        pos_x_bg_start = shift_x[2]
        pos_x_bg_finish = shift_x[2] + min(image[0].shape[1], image[2].shape[1])

        pos_y_fg_start = 0
        pos_y_fg_finish = shift_y[0] + shift_y[2]
        pos_x_fg_start = 0
        pos_x_fg_finish = min(image[0].shape[1], image[2].shape[1]) - shift_x[2]
        if total_cam == 6:
            pos_x_fg_finish = pos_x_bg_finish
        if shift_x[2] < 0:
            pos_x_bg_start = 0
            pos_x_bg_finish = min(image[0].shape[1], image[2].shape[1]) - abs(shift_x[2])

            pos_x_fg_start = abs(shift_x[2])
            pos_x_fg_finish = abs(shift_x[2]) + min(image[0].shape[1], image[2].shape[1])

        try:
            bg_image = image[0][pos_y_bg_start:pos_y_bg_finish, pos_x_bg_start:pos_x_bg_finish]
            fg_image = image[2][pos_y_fg_start:pos_y_fg_finish, pos_x_fg_start:pos_x_fg_finish]
            overlap = cv2.addWeighted(bg_image, 0.5, fg_image, 0.5, 0)
        except:
            overlap = None

        try:
            bg_image = crop_region(bg_image, "front_left")
            fg_image = crop_region(fg_image, "left_front")
            blending = create_blending(bg_image, fg_image)
        except:
            blending = None

    else:
        pos_y_bg_start = None
        overlap = None
        blending = None
    return pos_y_bg_start, overlap, blending


def find_overlap_image_front_right(image, shift_x, shift_y):
    if shift_y[1] > 0 or shift_y[3] > 0:
        x = abs(shift_x[1] - shift_x[3])
        pos_y_bg_start = image[1].shape[0] - shift_y[1] - shift_y[3]
        pos_y_bg_finish = image[1].shape[0]
        pos_x_bg_start = x
        pos_x_bg_finish = x + min(image[1].shape[1], image[3].shape[1])

        pos_y_fg_start = 0
        pos_y_fg_finish = shift_y[1] + shift_y[3]
        pos_x_fg_start = 0
        pos_x_fg_finish = min(image[1].shape[1], image[3].shape[1]) - x
        if (shift_x[1] - shift_x[3]) < 0:
            # image 4 more left than image 2
            pos_x_bg_start = 0
            pos_x_bg_finish = min(image[1].shape[1], image[3].shape[1]) - abs(shift_x[1] - shift_x[3])

            pos_x_fg_start = abs(shift_x[1] - shift_x[3])
            pos_x_fg_finish = abs(shift_x[1] - shift_x[3]) + min(image[1].shape[1], image[3].shape[1])

        # produce the roi of overlapping
        try:
            bg_image = image[1][pos_y_bg_start:pos_y_bg_finish, pos_x_bg_start:pos_x_bg_finish]
            fg_image = image[3][pos_y_fg_start:pos_y_fg_finish, pos_x_fg_start:pos_x_fg_finish]
            overlap = cv2.addWeighted(bg_image, 0.5, fg_image, 0.5, 0)
        except:
            overlap = None

    else:
        pos_y_bg_start = None
        overlap = None
    return pos_y_bg_start, overlap


def find_overlap_image_front_right_6_view(image, shift_x, shift_y):
    if shift_y[1] > 0 or shift_y[3] > 0:
        x = abs(shift_x[1] - shift_x[3])
        pos_y_bg_start = image[1].shape[0] - shift_y[1] - shift_y[3]
        pos_y_bg_finish = image[1].shape[0]
        pos_x_bg_start = image[1].shape[1] - image[3].shape[1] + x
        pos_x_bg_finish = pos_x_bg_start + min(image[1].shape[1], image[3].shape[1])

        pos_y_fg_start = 0
        pos_y_fg_finish = shift_y[1] + shift_y[3]
        pos_x_fg_start = 0
        pos_x_fg_finish = min(image[1].shape[1], image[3].shape[1]) - x

        if (shift_x[1] - shift_x[3]) < 0:
            pos_x_bg_start = image[1].shape[1] - image[3].shape[1] - x
            pos_x_bg_finish = pos_x_bg_start + min(image[1].shape[1], image[3].shape[1])

            pos_x_fg_start = 0
            pos_x_fg_finish = (image[3].shape[1])

        try:
            bg_image = image[1][pos_y_bg_start:pos_y_bg_finish, pos_x_bg_start:pos_x_bg_finish]
            fg_image = image[3][pos_y_fg_start:pos_y_fg_finish, pos_x_fg_start:pos_x_fg_finish]
            overlap = cv2.addWeighted(bg_image, 0.5, fg_image, 0.5, 0)
        except:
            overlap = None

        try:
            bg_image = crop_region(bg_image, "front_right")
            fg_image = crop_region(fg_image, "right_front")
            gradient = create_blending(bg_image, fg_image)
        except:
            gradient = None

    else:
        pos_y_bg_start = None
        overlap = None
        gradient = None
    return pos_y_bg_start, overlap, gradient


def find_overlap_image_front(image, shift_x, shift_y):
    """
    corner
    Args:
        image:
        shift_x:
        shift_y:

    Returns:

    """
    if shift_x[1] > 0:
        pos_y_bg_start = max(shift_y[0], shift_y[1])
        pos_y_bg_finish = pos_y_bg_start + min(image[0].shape[0], image[1].shape[0])
        pos_x_bg_start = image[0].shape[1] - shift_x[1]
        pos_x_bg_finish = image[0].shape[1]

        pos_y_fg_start = 0
        pos_y_fg_finish = min(image[0].shape[0], image[1].shape[0]) - max(shift_y[0], shift_y[1])
        pos_x_fg_start = 0
        pos_x_fg_finish = shift_x[1]
        if shift_y[0] > 0:
            pos_y_bg_start = 0
            pos_y_bg_finish = min(image[0].shape[0], image[1].shape[0]) - max(shift_y[0], shift_y[1])

            pos_y_fg_start = max(shift_y[0], shift_y[1])
            pos_y_fg_finish = max(shift_y[0], shift_y[1]) + min(image[0].shape[0], image[1].shape[0])

        # produce the roi of overlapping
        try:
            bg_image = image[0][pos_y_bg_start:pos_y_bg_finish, pos_x_bg_start:pos_x_bg_finish]
            fg_image = image[1][pos_y_fg_start:pos_y_fg_finish, pos_x_fg_start:pos_x_fg_finish]
            overlap = cv2.addWeighted(bg_image, 0.5, fg_image, 0.5, 0)
        except:
            overlap = None

        try:
            bg_image = crop_region(bg_image, "horizontal_left")
            fg_image = crop_region(fg_image, "horizontal_right")
            gradient = create_blending(bg_image, fg_image)
        except:
            gradient = None

    else:
        pos_x_bg_start = None
        overlap = None
        gradient = None
    return pos_x_bg_start, overlap, gradient


def find_overlap_image_rear(image, shift_x, shift_y, total_cam=4):
    """

    Args:
        image:
        shift_x:
        shift_y:
        total_cam:

    Returns:

    """
    bg_image = image[2]
    bg_shift_Y = shift_y[2]
    bg_shift_x = shift_x[2]

    fg_image = image[3]
    fg_shift_x = shift_x[3]
    fg_shift_Y = shift_y[3]

    if total_cam == 6:
        bg_image = image[4]
        bg_shift_Y = shift_y[4]
        bg_shift_x = shift_x[4]

        fg_image = image[5]
        fg_shift_x = shift_x[5]
        fg_shift_Y = shift_y[5]

    if (bg_shift_x + fg_shift_x) > 0:
        pos_y_bg_start = abs(bg_shift_Y - fg_shift_Y)
        pos_y_bg_finish = pos_y_bg_start + min(bg_image.shape[0], fg_image.shape[0])
        pos_x_bg_start = bg_image.shape[1] - bg_shift_x - fg_shift_x
        pos_x_bg_finish = bg_image.shape[1]

        pos_y_fg_start = 0
        pos_y_fg_finish = min(bg_image.shape[0], fg_image.shape[0]) - abs(bg_shift_Y - fg_shift_Y)
        pos_x_fg_start = 0
        pos_x_fg_finish = bg_shift_x + fg_shift_x
        if fg_shift_Y > bg_shift_Y:
            # image 3 lower than image 4
            pos_y_bg_start = 0
            pos_y_bg_finish = min(bg_image.shape[0], fg_image.shape[0]) - abs(bg_shift_Y - fg_shift_Y)

            pos_y_fg_start = abs(bg_shift_Y - fg_shift_Y)
            pos_y_fg_finish = abs(bg_shift_Y - fg_shift_Y) + min(bg_image.shape[0], fg_image.shape[0])

        try:
            # produce the roi of overlapping
            bg_image = bg_image[pos_y_bg_start:pos_y_bg_finish, pos_x_bg_start:pos_x_bg_finish]
            fg_image = fg_image[pos_y_fg_start:pos_y_fg_finish, pos_x_fg_start:pos_x_fg_finish]
            overlap = cv2.addWeighted(bg_image, 0.5, fg_image, 0.5, 0)
        except:
            overlap = None
        try:
            bg_image = crop_region(bg_image, "horizontal_left")
            fg_image = crop_region(fg_image, "horizontal_right")
            gradient = create_blending(bg_image, fg_image)
        except:
            gradient = None

        if bg_shift_x < 0:
            print(" i am hre for image shift minus")
            overlap = None

    else:
        overlap = None
        gradient = None
    return overlap, gradient


def find_overlap_image_rear_left_6_view(image, shift_x, shift_y):
    """
    this is for 6 view
    Args:
        image:
        shift_x:
        shift_y:

    Returns:

    """
    # if shift_y[2] > 0 or shift_y[4] > 0:
    if (shift_y[4] - shift_y[2]) > 0:
        pos_y_bg_start = image[2].shape[0] - abs(shift_y[4] - shift_y[2])
        pos_y_bg_finish = image[2].shape[0]
        pos_x_bg_start = shift_x[4] - shift_x[2]
        pos_x_bg_finish = image[2].shape[1] + pos_x_bg_start

        pos_y_fg_start = 0
        pos_y_fg_finish = abs(shift_y[4] - shift_y[2])
        pos_x_fg_start = 0
        pos_x_fg_finish = image[2].shape[1] - pos_x_bg_start

        if shift_x[2] > shift_x[4]:
            pos_x_bg_start = 0
            pos_x_bg_finish = image[2].shape[1]

            pos_x_fg_start = shift_x[2] - shift_x[4]
            pos_x_fg_finish = image[2].shape[1] + pos_x_fg_start
        try:
            bg_image = image[2][pos_y_bg_start:pos_y_bg_finish, pos_x_bg_start:pos_x_bg_finish]
            fg_image = image[4][pos_y_fg_start:pos_y_fg_finish, pos_x_fg_start:pos_x_fg_finish]
            overlap = cv2.addWeighted(bg_image, 0.5, fg_image, 0.5, 0)
        except:
            overlap = None

        try:
            bg_image = crop_region(bg_image, "left_rear")
            fg_image = crop_region(fg_image, "rear_left")
            blending = create_blending(bg_image, fg_image)
        except:
            blending = None

    else:
        overlap = None
        blending = None
    return overlap, blending


def find_overlap_image_rear_right_6_view(image, shift_x, shift_y):
    """
    this is for 6 view
    Args:
        image:
        shift_x:
        shift_y:

    Returns:

    """
    if (shift_y[5] - shift_y[3]) > 0:
        pos_y_bg_start = image[3].shape[0] - abs(shift_y[5] - shift_y[3])
        pos_y_bg_finish = image[3].shape[0]
        pos_x_bg_start = 0
        pos_x_bg_finish = image[3].shape[1]

        pos_y_fg_start = 0
        pos_y_fg_finish = abs(shift_y[5] - shift_y[3])
        pos_x_fg_start = image[5].shape[1] - image[3].shape[1] - abs(shift_x[5] - shift_x[3])
        pos_x_fg_finish = pos_x_fg_start + image[3].shape[1]

        if shift_x[5] > shift_x[3]:
            pos_x_bg_start = 0
            pos_x_bg_finish = image[2].shape[1] - abs(shift_x[5] - shift_x[3])

            pos_x_fg_start = image[5].shape[1] - image[2].shape[1] + abs(shift_x[5] - shift_x[3])
            pos_x_fg_finish = image[5].shape[1]

        try:
            bg_image = image[3][pos_y_bg_start:pos_y_bg_finish, pos_x_bg_start:pos_x_bg_finish]
            fg_image = image[5][pos_y_fg_start:pos_y_fg_finish, pos_x_fg_start:pos_x_fg_finish]
            overlap = cv2.addWeighted(bg_image, 0.5, fg_image, 0.5, 0)
        except:
            overlap = None

        try:
            bg_image = crop_region(bg_image, "right_rear")
            fg_image = crop_region(fg_image, "rear_right")
            blending = create_blending(bg_image, fg_image)
        except:
            blending = None

    else:
        overlap = None
        blending = None
    return overlap, blending
