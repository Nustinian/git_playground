from tkinter import *
from datetime import datetime
from typing import List
from steps_dict import steps_dict

window = Tk()

information = "hello"

timestamps: List[datetime] = []

def traverse(page):
    page_dict = steps_dict[page]
    steps = page_dict["steps"]
    for step in range(1, steps + 1):
        if isinstance(page_dict[step], list):
            print(page_dict[step][0])
            options = page_dict[step]
            options_string = concatenate(options)
            while True:
                try:
                    user_entry = input("enter one of the following: " + options_string)
                    if user_entry in options:
                        traverse(user_entry)
                        break
                except ValueError:
                    continue
        else:
            try:
                next_page = float(page_dict[step])
                traverse(str(next_page))
            except:
                print(page_dict[step])
                user_input = input(
                    "press enter when done, or input 'b' to go back a step."
                )
                if user_input == "b" or user_input == "B":
                    pass
                timestamps.append(
                    (page_dict[step], datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                )


def concatenate(options):
    result = " "
    for i in range(1, len(options)):
        result += str(options[i]) + " "
    return result


def update(add_me):
    global information
    information += add_me
    label2.config(text=information)


label1 = Label(window, text="Information:")
label1.grid(row=0, column=0)
label2 = Label(window, text=information)
label2.grid(row=1, column=0)

entry1_value = StringVar()
entry1 = Entry(window, textvariable=entry1_value)
entry1.grid(row=0, column=1)

button1 = Button(window, text="Go", command=lambda: update(entry1_value.get()))
button1.grid(row=3, column=1)
button2 = Button(window)

traverse("4.45")

print(timestamps)
