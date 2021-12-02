from tkinter import *
import time
from Ball import *

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg="black")
canvas.pack()

white_ball = Ball(canvas, 0, 0, 100, 1, 1, "white")
green_ball = Ball(canvas, 0, 0, 75, 2, 2,"green")
orange_ball = Ball(canvas, 0, 0, 50, 3, 3,"orange")
blue_ball = Ball(canvas, 0, 0, 125, 3, 3,"blue")

while True:
    white_ball.move()
    green_ball.move()
    orange_ball.move()
    blue_ball.move()
    window.update()
    time.sleep(0.01)


window.mainloop()