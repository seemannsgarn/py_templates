from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(initialdir='C:\\',
                                    defaultextension='.txt',
                                    filetypes = [
                                        ('Text file','.txt'),
                                        ('HTML files', '.html'),
                                        ('All files','*.*')
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()


window = Tk()
button = Button(text='Save',command=save_file)
button.pack()
text = Text(window)
text.pack()
window.mainloop()