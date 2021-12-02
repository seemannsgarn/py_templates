from tkinter import *
import time

WIDTH = 640
HEIGHT = 360
xVelocity = 3
yVelocity = 2

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background_image = PhotoImage(file='C:\\py\\learn_py\\lessons\\images\\water1-bg.png')
background = canvas.create_image(0,0,image=background_image,anchor=NW)


photo_image = PhotoImage(file='C:\\py\\learn_py\\lessons\\images\\clown-fish-mini.png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity = xVelocity * -1
    if (coordinates[1] >= (HEIGHT-image_height) or coordinates[1] < 0):
        yVelocity =  -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
