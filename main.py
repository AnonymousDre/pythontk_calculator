from tkinter import *

window = Tk()
window.geometry("500x700")
window.title("GUI Calculator")

icon = PhotoImage(file="calculator_image.png")
window.iconphoto(False, icon)
window.config(bg="#33324b")

def create_button(window, text):
    return Button(window, text=text, font=("Arial", 24), bg="#22222c", fg="white")
def place_operator(button, y):
    button.place(relx = 0.9, rely = y, anchor=W, width=50, height=50)

plus = create_button(window, "+")
minus = create_button(window, "-")
multi = create_button(window, "x")
equal = create_button(window, "=")

zero = create_button(window, "0")
one = create_button(window, "1") 
two = create_button(window, "2")
three = create_button(window, "3")

place_operator(plus, 0.35)
place_operator(minus, 0.425)
place_operator(multi, 0.50)
place_operator(equal, 0.9)

'''place_button(zero, 0.575)
place_button(one, 0.65)
place_button(two, 0.725)
place_button(three, 0.8)
'''
window.mainloop()