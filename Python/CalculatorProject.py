from tkinter import *
from math import *

#Main window for calculator
main_window = Tk()
main_window.title("Calculator")

# Create the input display
display = Entry(main_window, borderwidth=5, justify="right")
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, padx=10, pady=10)

# Function to update display on button click
def button_click(value):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + value)

#function to evaluate
def evaluate():
    try:
        result = eval(display.get())
        display.delete(0, END)
        display.insert(0, str(result))
    except Exception:
        display.delete(0, END)
        display.insert(0, "Error")

# Function to clear the display
def clear_display():
    display.delete(0, END)

#Function to delete the recent text
def delete_last():
    current = display.get()
    display.delete(0, END)
    display.insert(0, current[:-1])

#Button from 0-9 and +,-,*,/
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('<-', 4, 0), ('0', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        Button(main_window, text=text, command=evaluate, height=2, width=5).grid(row=row, column=col)
    elif text == 'C':
        Button(main_window, text=text, command=clear_display, height=2, width=25).grid(row=row, column=col, columnspan=4)
    elif text == '<-':
        Button(main_window, text=text, command=delete_last, height=2, width=5).grid(row=row, column=col)
    else:
        Button(main_window, text=text, command=lambda t=text: button_click(t), height=2, width=5).grid(row=row, column=col)


main_window.mainloop()
