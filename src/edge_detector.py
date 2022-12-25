import numpy as np
import cv2

from utils import highlight_coordinates, get_rect_coordinates

def get_pixel_strength(np_img, row_ind, col_ind):

    """
        returns None if the coordinate is out of img
        returns channel-wise pixel values (BGR)
    """
    out = []
    num_rows, num_cols, num_channels = np.shape(np_img)

    if row_ind >= num_rows or row_ind < 0:
        return None

    if col_ind >= num_cols or col_ind < 0:
        return None

    channel_ind = 0
    while channel_ind < num_channels:
        out.append(
            np_img[row_ind][col_ind][channel_ind]
        )
        channel_ind = channel_ind + 1

    return out


def is_pixel_part_of_an_edge(np_img, row_ind, col_ind):
    """
        1. draw a rectange around center_pixel
        2. for each rect_pixel:
            a. check if rect_pixel is part of img
            b. compute total_sum of all channels of rect_pixel (pixel_strength)
            c. if pixel strength > pixel_strength_threshold, then set high_strength_pixel = 1 for such pixel
            d. compute percentage of high strength pixels in rectange
            e. if percentage of high strength pixels is between hsp_perc_lower_bound, hsp_perc_upper_bound then, given pixel is part of an edge
    """

    rect_margin = 1
    std_threshold = 32
    pixel_strength_list_2d = []
    

    rect_coordinates = get_rect_coordinates(row_ind, col_ind, rect_margin)

    # print(f'tot_rect coordintes: {len(rect_coordinates)}')

    for coordinate_arr in rect_coordinates:
        rect_row_ind = coordinate_arr[0]
        rect_col_ind = coordinate_arr[1]

        pixel_strength_1d = get_pixel_strength(np_img, rect_row_ind, rect_col_ind)
        if pixel_strength_1d != None:
            pixel_strength_list_2d.append(pixel_strength_1d)

    if len(pixel_strength_list_2d) == 0:
        return False

    std_ = np.std(
        np.array(pixel_strength_list_2d),
        axis=0
    )
    
    if sum(std_) > std_threshold:
        return True

    return False

    # # to-do: remove this
    # rect_coordinates.append([row_ind, col_ind])
    # np_img_modified = highlight_coordinates(np_img, rect_coordinates)
    # cv2.imwrite('../data/out-2.png', np_img_modified)
    # return False


def detect_edges(np_img_raw):
    out = []
    num_rows, num_cols, num_channels = np.shape(np_img_raw)

    row_ind = 0
    while row_ind < num_rows:
        col_ind = 0
        while col_ind < num_cols:

            # # to-do: remove this
            # row_ind = 40
            # col_ind = 26
            # response = is_pixel_part_of_an_edge(np_img_raw, row_ind, col_ind)
            # return out
            
            response = is_pixel_part_of_an_edge(np_img_raw, row_ind, col_ind)
            if response == True:
                out.append([row_ind, col_ind])    

            col_ind = col_ind + 1

        row_ind = row_ind + 1

    return out