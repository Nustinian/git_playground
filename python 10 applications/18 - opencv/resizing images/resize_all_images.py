import cv2
from os import listdir
from os.path import isfile, join
pictures = [f for f in listdir(".") if isfile(join(".", f)) and f[-4:] == '.jpg']

for picture in pictures:
    img = cv2.imread(picture, 1)
    cv2.imwrite(picture[:-4] + "_resized.jpg",cv2.resize(img, (100, 100)))