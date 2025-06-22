from tkinter import *

window = Tk()
window.geometry("500x700")
window.title("GUI Calculator")

icon = PhotoImage(file="calculator_image.png")
window.iconphoto(False, icon)
window.config(bg="#33324b")

plus = Button(window, text="+", font=("Arial", 24), bg="#22222c", fg="white")
plus.place(x=450, y=250)
window.mainloop()