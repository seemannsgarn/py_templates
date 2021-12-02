from tkinter import *

# button = you click it, then it does stuff


def click():
    print('You click!')

main_win = Tk()
photo = PhotoImage(file='C:\\Users\\mustafaevsl\\Pictures\\like.png')

button_1 = Button(main_win,text='click',
                  command=click,
                  font=('Comic Sans',30),
                  fg='black',
                  bg='white',
                  activeforeground = 'green',
                  activebackground='grey',
                  state=ACTIVE,
                  image=photo,
                  compound='bottom')

button_1.pack()

main_win.mainloop()