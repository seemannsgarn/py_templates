from tkinter import *

def do_something(event):
    # print(event.keysym)
    label.config(text=event.keysym)

window = Tk()
window.geometry("650x200")

window.bind("<Key>",do_something)
label = Label(window,font=("Impact",100))
label.pack()

window.mainloop()