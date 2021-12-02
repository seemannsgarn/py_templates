# canvas = widget that is used to draw graphs, plots, images in a window
from tkinter import *

window =Tk()
canvas = Canvas(window,height=500,width=500)
# canvas.create_line(0,0,500,500,fill='brown',width=5)
# canvas.create_line(0,500,500,0,fill='pink',width=5)
# canvas.create_rectangle(50,50,250,250,fill='gray',width=2)
# points = [250,0,500,500,0,500]
# canvas.create_polygon(points,fill="light gray",outline="black",width=5)
# canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,width=5)

canvas.create_arc(10,10,490,490,fill="red",extent=180,width=10)
canvas.create_arc(10,10,490,490,fill="white",extent=180,start=180,width=10)
canvas.create_oval(200,200,300,300,fill="white",width=10)
canvas.pack(padx=10,pady=10)
window.mainloop()