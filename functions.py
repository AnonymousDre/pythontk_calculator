from tkinter import *


def create_button(window, text):
    return Button(window, text=text, font=("Arial", 24), bg="#22222c", fg="white")
def place_operator(button, y):
    button.place(relx = 0.9, rely = y, anchor=W, width=50, height=50)
