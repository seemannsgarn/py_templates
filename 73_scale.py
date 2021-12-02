from tkinter import *

def submit():
    print('The temperature is: ' + str(scale.get())+' degrees C')

window = Tk()

hot_image = PhotoImage(file='C:\\Users\\mustafaevsl\\Pictures\\life-mini.png')
hot_label = Label(image=hot_image)
hot_label.pack()

scale = Scale(window,
              from_ = 100,
              to = 0,
              length = 600,
              orient = VERTICAL,    # orientation of scale
              font = ('Courier new', 15),
              tickinterval = 10,
              # showvalue = 0,         # hide current value
              resolution = 5,         # increment of slider
              troughcolor = 'pink',
              bg='black',
              fg='pink'
)

scale.set(((scale['from'] - scale['to'])/2) + scale['to'])  # set current value of slider
scale.pack()

cold_image = PhotoImage(file='C:\\Users\\mustafaevsl\\Pictures\\robot-mini.png')
cold_label = Label(image=cold_image)
cold_label.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()