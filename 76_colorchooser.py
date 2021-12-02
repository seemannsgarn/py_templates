from tkinter import *
from tkinter import colorchooser #submodule

def click():
    color = colorchooser.askcolor() # assign color to a variable
    colorHex = color[1]             # assigns element at index 1 to a variable
    window.config(bg=colorHex)      # change background color

window = Tk()

window.geometry("500x500")

button = Button(text='click', command=click, padx=25, pady=25)
button.pack()

window.mainloop()