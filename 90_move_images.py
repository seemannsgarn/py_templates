from tkinter import *

# --------move image in a label---------------------------

# def move_up(event):
#     label.place(x=label.winfo_x(),y=label.winfo_y()-10)
#
# def move_down(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y() + 10)
# def move_left(event):
#     label.place(x=label.winfo_x() - 10, y=label.winfo_y())
# def move_right(event):
#     label.place(x=label.winfo_x() + 10, y=label.winfo_y())
#
# window = Tk()
# window.geometry("500x500")
#
# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)
# window.bind("<Up>",move_up)
# window.bind("<Down>",move_down)
# window.bind("<Left>",move_left)
# window.bind("<Right>",move_right)
#
# car_image = PhotoImage(file="C:\\Users\\mustafaevsl\\Pictures\\car_red_mini.png")
# label = Label(window,image=car_image)
# label.place(x=0,y=0)
#
# window.mainloop()

#------------------------------------------------------------
def move_up(event):
    canvas.move(myimage,0,-10)
def move_down(event):
    canvas.move(myimage,0,10)
def move_left(event):
    canvas.move(myimage,-10,0)
def move_right(event):
    canvas.move(myimage,10,0)
window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

photoimage = PhotoImage(file="C:\\Users\\mustafaevsl\\Pictures\\car_red_mini.png")
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

window.mainloop()