from tkinter import *

window = Tk()
window.title('Basic Calculator')

entry = Entry(window, width=20, justify='right')
entry.grid(row=0, column=1, columnspan=2, rowspan=1)

def input(number):
    current = entry.get()
    entry.delete(0, len(current))
    entry.insert(0, str(current)+str(number))

def add():
    global first_number
    first_number = entry.get()
    entry.delete(0, len(first_number))
    try:
        first_number = float(first_number)
    except(ValueError):
        first_number = float(0)
    global operation
    operation = 'addition'

def subtract():
    first_number = entry.get()
    entry.delete(0, len(first_number))
    try:
        first_number = float(first_number)
    except(ValueError):
        first_number = float(0)
    global operation
    operation = 'subtraction'

def multiply():
    global first_number
    first_number = entry.get()
    entry.delete(0, len(first_number))
    try:
        first_number = float(first_number)
    except(ValueError):
        first_number = float(0)
    global operation
    operation = 'multiplication'

def divide():
    global first_number
    first_number = entry.get()
    entry.delete(0, len(first_number))
    try:
        first_number = float(first_number)
    except(ValueError):
        first_number = float(0)
    global operation
    operation = 'division'

def equation():
    second_number = entry.get()
    entry.delete(0, len(second_number))
    try:
        second_number = float(second_number)
    except(ValueError):
        second_number = float(0)
    if operation == 'addition':
        sum = first_number + second_number
        entry.insert(0, sum)
    elif operation == 'subtraction':
        difference = first_number - second_number
        entry.insert(0, difference)
    elif operation == 'multiplication':
        product = first_number * second_number
        entry.insert(0, product)
    else:
        try:
            quotient = first_number / second_number
            entry.insert(0, quotient)
        except(ZeroDivisionError):
            entry.insert(0, 'Error')

def clear():
    entry.delete(0, len(entry.get()))

button_1 = Button(window, text='1', width=10, command=lambda: input(1))
button_2 = Button(window, text='2', width=10, command=lambda: input(2))
button_3 = Button(window, text='3', width=10, command=lambda: input(3))
button_4 = Button(window, text='4', width=10, command=lambda: input(4))
button_5 = Button(window, text='5', width=10, command=lambda: input(5))
button_6 = Button(window, text='6', width=10, command=lambda: input(6))
button_7 = Button(window, text='7', width=10, command=lambda: input(7))
button_8 = Button(window, text='8', width=10, command=lambda: input(8))
button_9 = Button(window, text='9', width=10, command=lambda: input(9))
button_0 = Button(window, text='0', width=10, command=lambda: input(0))
decimal_point = Button(window, text='.', width=10, command=lambda: input('.'))
equal = Button(window, text='=', width=10, command=equation)
addition = Button(window, text='+', width=10, command=add)
subtraction = Button(window, text='-', width=10, command=subtract)
multiplication = Button(window, text='*', width=10, command=multiply)
division = Button(window, text='/', width=10, command=divide)
clear = Button(window, text='AC', width=10, command=clear)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_0.grid(row=4, column=0)
decimal_point.grid(row=4, column=1)
addition.grid(row=1, column=3)
subtraction.grid(row=2, column=3)
multiplication.grid(row=3, column=3)
division.grid(row=4, column=3)
equal.grid(row=4, column=2)
clear.grid(row=10, column=1)

window.mainloop()