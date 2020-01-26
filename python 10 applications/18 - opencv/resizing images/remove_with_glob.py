import cv2
from glob import glob
from os import remove
resized_pictures = glob("*_resized.jpg")

for picture in resized_pictures:
    remove(picture)