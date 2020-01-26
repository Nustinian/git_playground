import cv2
from glob import glob
pictures = glob("*.jpg")

for picture in pictures:
    img = cv2.imread(picture, 1)
    cv2.imwrite(picture[:-4] + "_resized.jpg",cv2.resize(img, (100, 100)))