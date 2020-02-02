import cv2, os
from glob import glob
from tkinter import *

def resize_and_rename(dates):
    if len(dates) != 13 or dates[6] != "-":
        date_error()
        return
    folders = ["PreProd", "PreProd-Magento-Web", "Prod", "Prod-Magento-Web", "Shared"]
    for folder in folders:
        pictures = glob(f"{folder}/*.png")
        for picture in pictures:
            img = cv2.imread(picture, 1)
            cv2.imwrite(folder + "\\" + folder + "_" + picture[len(folder) + 1:-4] + "_" + dates + ".png", cv2.resize(img, (930, 430)))
            os.remove(picture)
    canvas.destroy()

def date_error():
    toplevel = Toplevel()
    error_label = Label(toplevel, text = "example: type '200101-200131' (no apostrophes) in the box for January 2020", height = 0, width = 100)
    error_label.pack()

canvas = Tk()

label1 = Label(canvas, text = "Dates:")
label1.grid(row = 0, column = 0)
label2 = Label(canvas, text = "format: type 200101-200131 for January 2020")
label2.grid(row = 1, column = 0, columnspan = 2)
label3 = Label(canvas, text = "WARNING: original files will be deleted.")
label3.grid(row = 2, column = 0, columnspan = 2)

entry1_value = StringVar()
entry1 = Entry(canvas, textvariable = entry1_value)
entry1.grid(row = 0, column = 1)

button1 = Button(canvas, text = "Go", command = lambda: resize_and_rename(entry1_value.get()))
button1.grid(row = 3, column = 1)

canvas.mainloop()