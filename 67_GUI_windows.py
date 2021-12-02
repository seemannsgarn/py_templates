from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

main_window = Tk()           # instantiate an instance of a window
main_window.geometry("420x420")
main_window.title("gui-hui")

icon = PhotoImage(file='C:\\Users\\mustafaevsl\\Pictures\\size.png')
main_window.iconphoto(True,icon)
main_window.config(background='#404742')

main_window.mainloop()       # place window on computer screen, listen for e vents