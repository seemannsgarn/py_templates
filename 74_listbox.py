# listbox = A listing of selectable text items within it's own container

from tkinter import *

def submit():

    langs = []

    for index in listbox.curselection():
        langs.insert(index, listbox.get(index))

    print('Your language is: ')
    for index in langs:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height = listbox.size())

def delete():

    for index in reversed(listbox.curselection()):
        listbox.delete(index)


    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg = '#E7E7E7',
                  font = ('Fira code',25),
                  width = 12,
                  selectmode = MULTIPLE)
listbox.pack()

listbox.insert(1,'Python')
listbox.insert(2,'C')
listbox.insert(3,'Java')
listbox.insert(4,'C++')
listbox.insert(5,'C#')
listbox.insert(6,'Visual Basic')

listbox.config(height = listbox.size())

entryBox = Entry(window)
entryBox.pack()

submit_button = Button(window, text = 'submit',command = submit)
submit_button.pack()

add_button = Button(window, text = 'add',command = add)
add_button.pack()

delete_button = Button(window, text = 'delete',command = delete)
delete_button.pack()

window.mainloop()