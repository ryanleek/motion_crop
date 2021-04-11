import cv2
import re
import os
import matplotlib.pyplot as plt
import numpy as np

path = "C:/Datasets/vid15"

count = 0
img_data = []
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('15.avi',fourcc, 10, (270,450))

dir_list = os.listdir(path)
dir_list.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])


for img in dir_list:
    img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_COLOR)
    new_array = cv2.resize(img_array, (270,450))
    #cv2.imwrite('out{}.jpg'.format(count), new_array)
    out.write(new_array)
    count += 1