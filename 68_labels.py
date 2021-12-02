from tkinter import *

# label = an area widget that holds text and/or an image within a window

main_window = Tk()
photo = PhotoImage(file='C:\\Users\\mustafaevsl\\Pictures\\pixel.png')
label = Label(main_window,
              text='Hi,my name is Shashkin Sasha!',
              font=('Bahnschrift',40),
              fg='black',
              bg='white',
              relief=RAISED,
              bd=3,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
# label.place(x=150,y=150)
label.pack()

main_window.mainloop()