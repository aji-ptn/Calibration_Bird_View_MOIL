import cv2


def find_overlapping_front_left(image_1, image_2, pos_1, pos_2):
    pos_x_bg_start = pos_1[0] - pos_2[0]
    pos_x_bg_finish = pos_x_bg_start + image_2.shape[1]
    pos_y_bg_start = pos_1[1] - pos_2[1]
    pos_y_bg_finish = image_1.shape[0]

    pos_x_fg_start = 0
    pos_x_fg_finish = image_2.shape[1]
    pos_y_fg_start = 0
    pos_y_fg_finish = image_1.shape[0] - pos_y_bg_start

    if pos_2[1] > pos_1[1]:
        pos_y_bg_start = 0
        pos_y_bg_finish = image_1.shape[0]
        pos_y_fg_start = pos_2[1] - pos_1[1]
        pos_y_fg_finish = image_1.shape[0] + pos_y_fg_start

    if pos_2[0] > pos_1[0]:
        pos_x_bg_start = 0
        pos_x_bg_finish = image_2.shape[1] + pos_1[0] - pos_2[0]
        pos_x_fg_start = pos_2[0] - pos_1[0]
        pos_x_fg_finish = image_2.shape[1]

    try:
        bg_image = image_1[pos_y_bg_start: pos_y_bg_finish, pos_x_bg_start:pos_x_bg_finish]
        fg_image = image_2[pos_y_fg_start: pos_y_fg_finish, pos_x_fg_start:pos_x_fg_finish]
        overlap = cv2.addWeighted(bg_image, 0.5, fg_image, 0.5, 0)
    except:
        overlap = None
        bg_image = None
        fg_image = None
    return overlap, bg_image, fg_image


def find_overlapping_front_right(image_1, image_2, pos_1, pos_2, crop_left):
    pos_x_bg_start = pos_1[0] - pos_2[0]
    pos_x_bg_finish = pos_x_bg_start + image_2.shape[1]
    pos_y_bg_start = pos_1[1] - pos_2[1]
    pos_y_bg_finish = image_1.shape[0]

    pos_x_fg_start = 0
    pos_x_fg_finish = image_2.shape[1]
    pos_y_fg_start = 0
    pos_y_fg_finish = image_1.shape[0] - pos_y_bg_start

    if pos_2[1] > pos_1[1]:
        pos_y_bg_start = 0
        pos_y_bg_finish = image_1.shape[0]
        pos_y_fg_start = pos_2[1] - pos_1[1]
        pos_y_fg_finish = image_1.shape[0] + pos_y_fg_start

    if pos_1[0] - pos_2[0] + image_2.shape[1] > image_1.shape[1]:
        end_3_x = pos_1[0] - pos_2[0] + image_2.shape[1] - image_1.shape[1] + crop_left
        pos_x_bg_finish = image_2.shape[1] + pos_1[0] - pos_2[0] - crop_left
        pos_x_fg_finish = image_2.shape[1] - end_3_x

    try:
        bg_image = image_1[pos_y_bg_start: pos_y_bg_finish, pos_x_bg_start:pos_x_bg_finish]
        fg_image = image_2[pos_y_fg_start: pos_y_fg_finish, pos_x_fg_start:pos_x_fg_finish]
        overlap = cv2.addWeighted(bg_image, 0.5, fg_image, 0.5, 0)
    except:
        overlap = None
        bg_image = None
        fg_image = None
    return overlap, bg_image, fg_image


def find_overlapping_rear_left(image_2, image_2_crop, image_4, image_4_crop, pos_2, pos_2_lf, pos_1_fl, pos_4):
    pos_x_bg_start = pos_2[0] - pos_4[0]
    pos_x_bg_finish = image_2.shape[1]
    pos_y_bg_start = pos_2[1] - pos_4[1]
    pos_y_bg_finish = image_4.shape[0] + pos_y_bg_start

    pos_x_fg_start = 0
    pos_x_fg_finish = image_2.shape[1] - pos_x_bg_start
    pos_y_fg_start = 0
    pos_y_fg_finish = image_4.shape[0]
    if image_4.shape[0] + pos_y_bg_start > image_2.shape[0]:
        pos_y_bg_finish = image_2.shape[0]
        pos_y_fg_finish = image_4.shape[0] - ((image_4.shape[0] + pos_y_bg_start) - image_2.shape[0])
    if pos_2[0] < pos_4[0]:
        pos_x_bg_start = 0
        pos_x_fg_start = pos_4[0] - pos_2[0]
        pos_x_fg_finish = pos_x_fg_start + image_2.shape[1]
    if image_2.shape[1] - (pos_2[0] - pos_1_fl[0]) == image_2_crop.shape[1]:
        pos_x_bg_start = pos_2_lf[0] - pos_1_fl[0]
        pos_x_fg_start = pos_4[0] - (pos_1_fl[0] + pos_2[0] - pos_2_lf[0])
        pos_x_fg_finish = pos_x_fg_start + image_2.shape[1] - pos_x_bg_start

    if pos_x_bg_start < 0:
        pos_x_bg_start = 0

        # print(pos_x_bg_start, pos_x_bg_finish, pos_y_bg_start, pos_y_bg_finish)
        # print(pos_x_fg_start, pos_x_fg_finish, pos_y_fg_start, pos_y_fg_finish)
    try:
        bg_image = image_2[pos_y_bg_start: pos_y_bg_finish, pos_x_bg_start:pos_x_bg_finish]
        fg_image = image_4[pos_y_fg_start: pos_y_fg_finish, pos_x_fg_start:pos_x_fg_finish]
        # cv2.imwrite("bg_image.jpg", bg_image)
        # cv2.imwrite("fg_image.jpg", fg_image)
        # cv2.imwrite("image_2_crop.jpg", image_2_crop)
        # cv2.imwrite("image_4_crop.jpg", image_4_crop)
        overlap = cv2.addWeighted(bg_image, 0.5, fg_image, 0.5, 0)
    except:
        overlap = None
        bg_image = None
        fg_image = None
    return overlap, bg_image, fg_image


def find_overlapping_rear_right(image_3, image_4, pos_3_rif, pos_4_rel, pos_2_lre, pos_2_lf, pos_1_fri, pos_1_fl):
    pos_x_bg_start = 0
    pos_x_bg_finish = image_3.shape[1]
    pos_y_bg_start = - pos_1_fri[1] + pos_2_lre[1] - pos_4_rel[1] + pos_1_fl[1] + pos_3_rif[1] - pos_2_lf[1]
    pos_y_bg_finish = image_4.shape[0] + pos_y_bg_start

    pos_x_fg_start = pos_1_fri[0] - pos_2_lre[0] + pos_4_rel[0] - pos_1_fl[0] - pos_3_rif[0] + pos_2_lf[0]
    pos_x_fg_finish = pos_x_fg_start + image_3.shape[1]
    pos_y_fg_start = 0
    pos_y_fg_finish = image_4.shape[0]

    if (pos_1_fri[1] - pos_3_rif[1] + image_3.shape[0]) - (pos_1_fl[1] + pos_2_lre[1] - pos_2_lf[0] - pos_4_rel[1] + image_4.shape[0]) < 0:
        # print("hereee")
        pos_y_bg_finish = image_3.shape[0]
        # pos_y_fg_finish = image_4.shape[0] - abs((pos_1_fri[1] - pos_3_rif[1] + image_3.shape[0]) - (pos_1_fl[1] + pos_2_lre[1] - pos_2_lf[0] - pos_4_rel[1] + image_4.shape[0])) - 88
        pos_y_fg_finish = pos_y_bg_finish - pos_y_bg_start
    if (pos_1_fl[0] + pos_2_lre[0] - pos_2_lf[0]) < pos_4_rel[0]:
        # print("here")
        pos_x_bg_finish = image_4.shape[1] - (pos_1_fri[0] - pos_3_rif[0])
        pos_x_fg_start = pos_1_fri[0] - pos_3_rif[0]
        # pos_x_fg_start = 0
        pos_x_fg_finish = image_4.shape[1]

    # if pos_2[1] < pos_4[1]:
    #     pos_x_bg_start = 0
    #     pos_x_fg_start = pos_4[0] - pos_2[0]
    #     pos_x_fg_finish = pos_x_fg_start + image_2.shape[1]

    # print(pos_x_bg_start, pos_x_bg_finish, pos_y_bg_start, pos_y_bg_finish)
    # print(pos_x_fg_start, pos_x_fg_finish, pos_y_fg_start, pos_y_fg_finish)

    try:
        bg_image = image_3[pos_y_bg_start: pos_y_bg_finish, pos_x_bg_start:pos_x_bg_finish]
        fg_image = image_4[pos_y_fg_start: pos_y_fg_finish, pos_x_fg_start:pos_x_fg_finish]
        # cv2.imwrite("bg_image.jpg", bg_image)
        # cv2.imwrite("fg_image.jpg", fg_image)
        overlap = cv2.addWeighted(bg_image, 0.5, fg_image, 0.5, 0)
    except:
        overlap = None
        bg_image = None
        fg_image = None
    return overlap, bg_image, fg_image
