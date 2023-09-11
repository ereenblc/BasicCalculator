from tkinter import *

window = Tk()
window.title("Python Calculator")
window.geometry("450x600")
window.resizable(width=False, height=False)
FONT_button = ("Verdena", 13, "bold")
user_inputs = ""


def get_number(digit):
    global user_inputs
    user_inputs = user_inputs + str(digit)
    result_label.config(text=user_inputs)


def clear_all():
    global user_inputs
    result_label.config(text="")
    user_inputs = ""


def equal_to():
    global user_inputs
    try:
        answer = str(eval(user_inputs))
        result_label.config(text=answer)
        user_inputs = answer
    except:
        result_label.config(text="ERROR!", fg="red")



title = Label(window, text="BASIC CALCULATOR", font=("Verdena", 18, "bold"),
              pady=10)
title.pack()

result_label = Label(window, width=30, height=2,
                     bg="white",
                     font=("Verdena", 18, "bold"))
result_label.pack()

frame = Frame(window)
frame.pack()

#buttons
button_clear = Button(frame, text="CLEAR", width=9, height=4, font=FONT_button, bg="dark gray", fg="white",
                  command=clear_all)
button_clear.grid(row=0, column=0)

button_left = Button(frame, text="(", width=9, height=4, font=FONT_button, bg="dark gray", fg="white",
                  command=lambda: get_number("("))
button_left.grid(row=0, column=1)

button_right = Button(frame, text=")", width=9, height=4, font=FONT_button, bg="dark gray", fg="white",
                  command=lambda: get_number(")"))
button_right.grid(row=0, column=2)

button_addition = Button(frame, text="+", width=9, height=4, font=FONT_button, bg="orange", fg="white",
                  command=lambda: get_number("+"))
button_addition.grid(row=0, column=3)



button_7 = Button(frame, text="7", width=9, height=4, font=FONT_button, bg="gray", fg="white",
                  command=lambda: get_number(7))
button_7.grid(row=1, column=0)

button_8 = Button(frame, text="8", width=9, height=4, font=FONT_button, bg="gray", fg="white",
                  command=lambda: get_number(8))
button_8.grid(row=1, column=1)

button_9 = Button(frame, text="9", width=9, height=4, font=FONT_button, bg="gray", fg="white",
                  command=lambda: get_number(9))
button_9.grid(row=1, column=2)

button_division = Button(frame, text="÷", width=9, height=4, font=FONT_button, bg="orange", fg="white",
                  command=lambda: get_number("/"))
button_division.grid(row=1, column=3)



button_4 = Button(frame, text="4", width=9, height=4, font=FONT_button, bg="gray", fg="white",
                  command=lambda: get_number(4))
button_4.grid(row=2, column=0)

button_5 = Button(frame, text="5", width=9, height=4, font=FONT_button, bg="gray", fg="white",
                  command=lambda: get_number(5))
button_5.grid(row=2, column=1)

button_6 = Button(frame, text="6", width=9, height=4, font=FONT_button, bg="gray", fg="white",
                  command=lambda: get_number(6))
button_6.grid(row=2, column=2)

button_multiplication = Button(frame, text="X", width=9, height=4, font=FONT_button, bg="orange", fg="white",
                  command=lambda: get_number("*"))
button_multiplication.grid(row=2, column=3)



button_1 = Button(frame, text="1", width=9, height=4, font=FONT_button, bg="gray", fg="white",
                  command=lambda: get_number(1))
button_1.grid(row=3, column=0)

button_2 = Button(frame, text="2", width=9, height=4, font=FONT_button, bg="gray", fg="white",
                  command=lambda: get_number(2))
button_2.grid(row=3, column=1)

button_3 = Button(frame, text="3", width=9, height=4, font=FONT_button, bg="gray", fg="white",
                  command=lambda: get_number(3))
button_3.grid(row=3, column=2)

button_substraction = Button(frame, text="−", width=9, height=4, font=FONT_button, bg="orange", fg="white",
                  command=lambda:get_number("-"))
button_substraction.grid(row=3, column=3)

button_0 = Button(frame, text="0", width=9, height=4, font=FONT_button, bg="gray", fg="white",
                  command=lambda: get_number(0))
button_0.grid(row=4, column=1)

button_dot = Button(frame, text=".", width=9, height=4, font=FONT_button, bg="gray", fg="white",
                  command=lambda: get_number("."))
button_dot.grid(row=4, column=2)

button_equal = Button(frame, text="=", width=9, height=4, font=FONT_button, bg="orange", fg="white",
                  command=equal_to)
button_equal.grid(row=4, column=3)

button_mod = Button(frame, text="%", width=9, height=4, font=FONT_button, bg="gray", fg="white",
                    command=lambda: get_number("%"))
button_mod.grid(row=4, column=0)

window.mainloop()