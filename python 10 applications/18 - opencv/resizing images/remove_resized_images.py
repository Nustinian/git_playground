from os import listdir, remove
from os.path import isfile, join
resized_pictures = [f for f in listdir(".") if isfile(join(".", f)) and f[-12:] == '_resized.jpg']

for picture in resized_pictures:
    remove(picture)