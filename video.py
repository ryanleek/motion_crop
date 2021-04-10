import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

path = "C:/Datasets/vid1"

count = 0
img_data = []
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 10, (279,584))

#dir_list = os.listdir(path)
#for item in dir_list:
#    print(item)

for img in os.listdir(path):
    img_array = cv2.imread(os.path.join(path, img))
    cv2.imshow("fffff", img_array)
    cv2.waitKey(0)
    #new_array = cv2.resize(img_array, dsize=(279, 584), interpolation=cv2.INTER_AREA)
    #cv2.imwrite('out{}'.format(count), new_array)
    #out.write(new_array)
    #count += 1