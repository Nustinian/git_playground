from tkinter import *
from datetime import datetime

window = Tk()

steps = [["jump"], ["jump twice", "do a push up"], ["break a leg"]]
current_step = 0
nested_step = 0
paths = {"1": "one", "2": "two", "2.1": "two point one", "2.2": "two point two", "3": "three"}

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
label2 = Label(window, text=steps[0][0])
label2.grid(row=1, column=0)

entry1_value = StringVar()
entry1 = Entry(window, textvariable=entry1_value)
entry1.grid(row=0, column=1)

button1 = Button(window, text="Go", command=update)
button1.grid(row=3, column=1)

button2 = Button(window, text="Skip one", command=skip)
button2.grid(row=3, column=0)

window.mainloop()


