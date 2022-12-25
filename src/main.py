import cv2
import numpy as np

import os

from edge_detector import detect_edges
from utils import highlight_coordinates, get_grayscale_img

IN_DIR = '../in'
OUT_DIR = '../out'

WHITE_LIST = [
    # 'dog-green-bg.jpeg'
    # 'black-dot.png'
    # '2-dogs-green-bg.jpeg',
    # 'girl-with-flower.png'
    'selfie.jpeg'
]

def entry_point():
    print('ii: starting...')

    valid_ext_list = [
        'png',
        'jpeg'
    ]

    for in_res in os.listdir(IN_DIR):

        if len(WHITE_LIST) != 0:
            if (in_res in WHITE_LIST) == False:
                continue

        in_res_path = os.path.join(IN_DIR, in_res)

        if os.path.isfile(in_res_path) == False:
            continue

        token_list = in_res.split('.')
        file_ext = token_list[1]

        if (file_ext in valid_ext_list) == False:
            continue
    
        print(f'processing {in_res_path}...')
        np_img = cv2.imread(in_res_path) # BGR
        np_img = get_grayscale_img(np_img)
        
        if np_img is None:
            raise Exception(f'invalid img at {in_res_path}')

        # np_img_modified = change_img_color(np_img)
        # np_img_modified = draw_rectangle_around(np_img, 80, 150)
        # np_img_modified = draw_circle_around(np_img, 80, 150)
        coordinate_list = detect_edges(np_img)
        np_img_modified = highlight_coordinates(np_img, coordinate_list)
        np_img_modified_outline = highlight_coordinates(np.zeros(np.shape(np_img)), coordinate_list)

        out_img_path = os.path.join(OUT_DIR, in_res)
        cv2.imwrite(out_img_path, np_img_modified)

        out_img_path = os.path.join(OUT_DIR, 'outline-' + in_res)
        cv2.imwrite(out_img_path, np_img_modified_outline)
        print(f'{in_res_path} processed')

    print('ii: exiting...')

if __name__ == '__main__':
    entry_point()

    