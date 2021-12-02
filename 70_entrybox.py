from tkinter import *
# entry widget = textbox that accepts a single line of user input

def submit():
    username = entry.get()
    print("Hello " + username)
def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1,END)

main_window = Tk()

entry = Entry(main_window,font=('Consolas',25))
entry.pack(side=LEFT)


submit_button = Button(main_window, text='submit',command=submit)
submit_button.pack(side=RIGHT)
delete_button = Button(main_window, text='delete',command=delete)
delete_button.pack(side=RIGHT)
backspace = Button(main_window, text='backspace',command=backspace)
backspace.pack(side=RIGHT)

main_window.mainloop()