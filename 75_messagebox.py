from tkinter import *
from tkinter import messagebox # import messagabox library

def click():
    # messagebox.showinfo(title='INFO',message='You are a little dick!')
    # messagebox.showwarning(title='WARNING',message='You have a little dick!!!')
    # messagebox.showerror(title='ERROR',message='You have a little dick!!!')

    # if messagebox.askokcancel(title='ask ok cancel',message='DO IT!!!'):
    #     print('You clicked OK, redneck!')
    # else:
    #     print('You clicked cancel, fucking coward')

    # if messagebox.askretrycancel(title='ask try cancel', message='message!'):
    #     print('try')
    # else:
    #     print('cancel')

    # if messagebox.askyesno(title='ask yes or no',message='Do you like pron?'):
    #     print('I like pron too')
    # else:
    #     print('Why do you not like pron?')

    # answer = messagebox.askquestion(title='ask question',message='Do you like Gal Gadot?')
    # if (answer == 'yes'):
    #     print('Yeeee, she is awesome!')
    # else:
    #     print('wat?')

    answer = messagebox.askyesnocancel(title='yes no cancel', message='Do you like watching anime?')
    if (answer == True):
        print('Yes')
    elif (answer == False):
        print('No')
    else:
        print('Cancel')
        
window = Tk()

button = Button(window, text='click',command=click,padx=15,pady=10)
button.pack()

window.mainloop()
