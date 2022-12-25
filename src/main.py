import cv2

from edge_detector import detect_edges
from utils import highlight_coordinates

IN_IMG = '../data/rects-circles.png' 
OUT_IMG = '../data/out.png'


    

def entry_point():
    print('ii: starting...')

    
    np_img = cv2.imread(IN_IMG) # BGR
    # print(type(np_img))
    # print(np.shape(np_img))
    # print(np.shape(np_img[0][0]))
    # print(np_img)

    # np_img_modified = change_img_color(np_img)
    # np_img_modified = draw_rectangle_around(np_img, 80, 150)
    # np_img_modified = draw_circle_around(np_img, 80, 150)
    coordinate_list = detect_edges(np_img)
    np_img_modified = highlight_coordinates(np_img, coordinate_list)

    cv2.imwrite(OUT_IMG, np_img_modified)

    print('ii: exiting...')

if __name__ == '__main__':
    entry_point()