# radio button =

from tkinter import *

def choice():
    if(x.get()==0):
        print('You are loverboy!')
    elif(x.get()==1):
        print('You are zombie!')
    elif(x.get()==2):
        print('You are robot!')
    else:
        print('huh?')

arr = ['love','death','robots']

main_window = Tk()

love_image = PhotoImage(file='C:\\Users\\mustafaevsl\\Pictures\\life-mini.png')
death_image = PhotoImage(file='C:\\Users\\mustafaevsl\\Pictures\\death-mini.png')
robot_image = PhotoImage(file='C:\\Users\\mustafaevsl\\Pictures\\robot-mini.png')

arr_images = [love_image,death_image,robot_image]

x = IntVar()



for index in range(len(arr)):
    radiobutton = Radiobutton(main_window,
                              padx = 25, # adds padding on x-axis
                              pady = 10,
                              text = arr[index],          # adds text to radio buttons
                              variable = x,               # groups radiobuttons together if they share the same variable
                              value = index,              # assigns each radiobutton a different value
                              font = ('Impact', 30),
                              image = arr_images[index],  # adds images to radiobutton
                              compound = 'left',          # adds image and text
                              indicatoron = 0,            # eliminate width of radio buttons
                              width = 250,                # sets width of radio buttons
                              command=choice)
    radiobutton.pack(anchor=W)

main_window.mainloop()

