# grid() = geometry manager that organizes widgets in a table-like structure in a parent

from tkinter import *

window = Tk()

Label(window,text="Enter your info.",font=("Impact",15)).grid(row=0,column=0,columnspan=2)

first_name_label = Label(window, text="First name: ",width=15,bg="light gray").grid(row=1,column=0)
first_name_entry = Entry(window).grid(row=1,column=1)

last_name_label = Label(window, text="Last name: ",width=17,bg="gray").grid(row=2,column=0)
last_name_entry = Entry(window).grid(row=2,column=1)

email_label = Label(window, text="E-mail: ",width=15,bg="pink").grid(row=3,column=0)
email_entry = Entry(window).grid(row=3,column=1)

submitButton = Button(window, text="Submit").grid(row=4,column=0,columnspan=2)

window.mainloop()