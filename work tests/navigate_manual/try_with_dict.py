from tkinter import *
from datetime import datetime

window = Tk()

paths = {"1": {"steps": 2, 1: "2", 2: "yes"}, "2": {"steps": 0, 1: "two"}}

sheet = "1"
steps = 0
current_step = 0

def do_next(sheet, steps, current_step):
    if steps == 0:
        current_step = 1
        try:
            steps = paths[sheet]["steps"]
        except IndexError:
            label2.config(text="all done!")
        try:
            nested_sheet = int(paths[sheet][current_step])
            do_next(nested_sheet, 0, 1)
        except:
            label2.config(text=paths[sheet][current_step])
            if current_step == steps:
                steps = 0
            current_step += 1
    label2.config(text=paths[sheet][current_step])
    current_step += 1

def update():
    global current_step
    global nested_step
    nested_step += 1
    try:
        label2.config(text=steps[current_step][nested_step])
    except IndexError:
        nested_step = 0
        current_step += 1
        try:
            label2.config(text=steps[current_step][nested_step])
        except IndexError:
            label2.config(text="all done!")

def skip():
    global current_step
    global nested_step
    nested_step = 0
    current_step += 1
    try:
        label2.config(text=steps[current_step][nested_step])
    except IndexError:
        label2.config(text="all done!")


label1 = Label(window, text="Information:")
label1.grid(row=0, column=0)
label2 = Label(window, text="blank")
label2.grid(row=1, column=0)

entry1_value = StringVar()
entry1 = Entry(window, textvariable=entry1_value)
entry1.grid(row=0, column=1)

button1 = Button(window, text="Go", command=do_next(sheet, steps, current_step))
button1.grid(row=3, column=1)

button2 = Button(window, text="Skip one", command=skip)
button2.grid(row=3, column=0)

window.mainloop()


