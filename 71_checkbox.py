from tkinter import *

def display():
    if(x.get()==1):
        print('You are agree!')
    else:
        print('You are disagree!')

main_window = Tk()

x = IntVar()

logo_photo = PhotoImage(file='C:\\Users\\mustafaevsl\\Pictures\\life-mini.png')

check_button = Checkbutton(main_window,
                           text='I agree',
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Fira code',20),
                           fg='gray',
                           bg='pink',
                           activebackground='pink',
                           activeforeground='gray',
                           padx=25,
                           pady=10,
                           image=logo_photo,
                           compound='left')
check_button.pack()

main_window.mainloop()