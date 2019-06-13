## Simple Calculator
import tkinter as cal
from tkinter import messagebox

calc = cal.Tk()
calc.title("Calculator")

heading_label1 = cal.Label(calc, text="Enter first number",)
heading_label1.pack()

firstNo = cal.Entry(calc)
firstNo.pack()

heading_label2 = cal.Label(calc, text="Enter second number")
heading_label2.pack()

secondNo = cal.Entry(calc)
secondNo.pack()

operations = cal.Label(calc, text="Operations")
operations.pack()

def addition():

    first, second = takeValueInput()
    result = first + second

    # print(first + second)
    result_label.config(text="Operations result is: " + str(result))

def subtract():

    first, second = takeValueInput()

    result = first - second

    # print(first + second)
    result_label.config(text="Operations result is: " + str(result))

def multiply():

    first, second = takeValueInput()

    result = first * second

    # print(first + second)
    result_label.config(text="Operations result is: " + str(result))

def divide():

    first, second = takeValueInput()

    if second == 0:
        messagebox.showerror("Error", "Cannot divide the value by 0.")
    else:
        result = first / second

        # print(first + second)

        result = round(result, 2)

        result_label.config(text="Operations result is: " + str(result))

def takeValueInput():

    first = firstNo.get()
    second = secondNo.get()
    
    try:
        first = int(first)
        second = int(second)
        return first, second
    except ValueError:
        if((len(firstNo.get()) == 0) or (len(secondNo.get()) == 0)):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")
        quit(0)

add_button = cal.Button(calc, text="+", command=lambda : addition())
add_button.pack()

sub_button = cal.Button(calc, text="-", command=lambda : subtract())
sub_button.pack()

mul_button = cal.Button(calc, text="*", command=lambda : multiply())
mul_button.pack()

div_button = cal.Button(calc, text="/", command=lambda : divide())
div_button.pack()

result_label = cal.Label(calc, text="Operations result is:")
result_label.pack()

calc.mainloop()