from tkinter import *

window = Tk()
window.geometry("500x700")
window.title("GUI Calculator")

icon = PhotoImage(file="calculator_image.png")
window.iconphoto(False, icon)
window.mainloop()