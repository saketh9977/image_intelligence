import numpy as np

def highlight_coordinates(np_img_raw, coordinate_list):
    np_img_out = np.array(np_img_raw)
    
    for coorinates in coordinate_list:
        row_ind = coorinates[0]
        col_ind = coorinates[1]

        np_img_out[row_ind][col_ind][0] = 0
        np_img_out[row_ind][col_ind][1] = 0
        np_img_out[row_ind][col_ind][2] = 255

    return np_img_out

def change_img_color(np_img):
    num_rows, num_cols, num_channels = np.shape(np_img)

    ind_row = 0
    while ind_row < num_rows:
        ind_col = 0
        while ind_col < num_cols:
            np_img[ind_row][ind_col][0] = 255
            np_img[ind_row][ind_col][1] = 255
            np_img[ind_row][ind_col][2] = 255
            
            ind_col = ind_col + 1

        ind_row = ind_row + 1
    return np_img

def get_grayscale_img(np_img):
    np_img_grayscale = np.array(np_img)
    num_rows, num_cols, num_channels = np.shape(np_img)

    row_ind = 0
    while row_ind < num_rows:
        col_ind = 0
        while col_ind < num_cols:
            avg_ = sum(np_img[row_ind][col_ind]) / len(np_img[row_ind][col_ind])
            np_img_grayscale[row_ind][col_ind] = round(avg_)

            col_ind = col_ind + 1

        row_ind = row_ind + 1
    
    return np_img_grayscale

def get_rect_coordinates(center_row, center_col, margin):

    """
        1. returns all coordinates that fall under a rectangle whose center is (center_row, center_col) & -
            perpendicular distance from center to side is margin
        2. also returns coordinates that are not part of image, if any, when rectangle stretches beyond img
    """

    out = []

    top_left_corner_row = center_row - margin
    top_left_corner_col = center_col - margin

    top_right_corner_row = top_left_corner_row
    top_right_corner_col = center_col + margin

    bottom_left_corner_row = center_row + margin
    bottom_left_corner_col = top_left_corner_col

    bottom_right_corner_row = bottom_left_corner_row
    bottom_right_corner_col = top_right_corner_col

    row_ind = top_left_corner_row
    col_ind = top_left_corner_col
    while col_ind <= top_right_corner_col:
        out.append([row_ind, col_ind])
        col_ind = col_ind + 1

    row_ind = top_right_corner_row
    col_ind = top_right_corner_col
    while row_ind <= bottom_right_corner_row:
        out.append([row_ind, col_ind])
        row_ind = row_ind + 1

    row_ind = bottom_right_corner_row
    col_ind = bottom_right_corner_col
    while col_ind >= bottom_left_corner_col:
        out.append([row_ind, col_ind])
        col_ind = col_ind - 1

    row_ind = bottom_left_corner_row
    col_ind = bottom_left_corner_col
    while row_ind >= top_left_corner_row:
        out.append([row_ind, col_ind])
        row_ind = row_ind - 1

    return out
    

def draw_rectangle_around(np_img, center_row, center_col):
    margin = 50

    top_left_corner_row = center_row - margin
    top_left_corner_col = center_col - margin

    top_right_corner_row = top_left_corner_row
    top_right_corner_col = center_col + margin

    bottom_left_corner_row = center_row + margin
    bottom_left_corner_col = top_left_corner_col

    bottom_right_corner_row = bottom_left_corner_row
    bottom_right_corner_col = top_right_corner_col

    row_ind = top_left_corner_row
    col_ind = top_left_corner_col
    while col_ind <= top_right_corner_col:
        np_img[row_ind][col_ind][0] = 0
        np_img[row_ind][col_ind][1] = 0
        np_img[row_ind][col_ind][2] = 255
        col_ind = col_ind + 1

    row_ind = top_right_corner_row
    col_ind = top_right_corner_col
    while row_ind <= bottom_right_corner_row:
        np_img[row_ind][col_ind][0] = 0
        np_img[row_ind][col_ind][1] = 0
        np_img[row_ind][col_ind][2] = 255
        row_ind = row_ind + 1

    row_ind = bottom_right_corner_row
    col_ind = bottom_right_corner_col
    while col_ind >= bottom_left_corner_col:
        np_img[row_ind][col_ind][0] = 0
        np_img[row_ind][col_ind][1] = 0
        np_img[row_ind][col_ind][2] = 255
        col_ind = col_ind - 1

    row_ind = bottom_left_corner_row
    col_ind = bottom_left_corner_col
    while row_ind >= top_left_corner_row:
        np_img[row_ind][col_ind][0] = 0
        np_img[row_ind][col_ind][1] = 0
        np_img[row_ind][col_ind][2] = 255
        row_ind = row_ind - 1

    return np_img

def draw_circle_around(np_img, center_row, center_col):

    """
        equation of a circle with center (a, b), radius r -
        (x-a)^2 + (y-b)^2 = r^2
    """

    radius = 50
    circle_error = 30
    num_rows, num_cols, num_channels = np.shape(np_img)

    row_ind = 0
    while row_ind < num_rows:
        col_ind = 0
        while col_ind < num_cols:
            lhs = (
                ((row_ind - center_row) ** 2) +
                ((col_ind - center_col) ** 2)
            )
            rhs = radius ** 2

            if lhs == rhs or (abs(lhs-rhs) < circle_error):
                np_img[row_ind][col_ind][0] = 0
                np_img[row_ind][col_ind][1] = 0
                np_img[row_ind][col_ind][2] = 255

            col_ind = col_ind + 1

        row_ind = row_ind + 1

    return np_img