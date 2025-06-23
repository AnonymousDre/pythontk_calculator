from tkinter import *

window = Tk()
window.geometry("500x700")
window.title("GUI Calculator")

icon = PhotoImage(file="calculator_image.png")
window.iconphoto(False, icon)
window.config(bg="#33324b")

def create_button(window, text):
    return Button(window, text=text, font=("Arial", 24), bg="#22222c", fg="white")

plus = create_button(window, "+")
minus = create_button(window, "+")
multi = create_button(window, "x")
equal = create_button(window, "=")

zero = create_button(window, "0")
one = create_button(window, "1")
two = create_button(window, "2")
three = create_button(window, "3")

plus.place(relx = 0.9, rely = 0.35, anchor=W, width=50, height=50)
minus.place(relx = 0.9, rely = 0.425, anchor = W, width = 50, height = 50)
multi.place(relx = 0.9, rely = 0.50, anchor= W, width = 50, height = 50)
equal.place(relx = 0.9, rely = 0.9, anchor= CENTER, width = 100, height = 50)
window.mainloop()