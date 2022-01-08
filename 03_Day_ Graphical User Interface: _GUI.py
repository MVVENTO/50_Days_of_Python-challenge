# Graphical User Interface: GUI
#import tinkter
from tkinter import *
window = Tk()
window.title("Welcome to HELL")
window.mainloop()


# create a label widget
from tkinter import *
window = Tk()
window.title("Welcome to HELL")
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
window.mainloop()


#when button is clicked hello changes
from tkinter import *
window = Tk()
window.title("Welcome to HELL")
window.geometry('350x300')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text="Button was clicked")
btn = Button(window, text="Click Me",command=clicked, 
             bg="orange", fg="blue")
btn.grid(column =1, row= 0)


window.mainloop()



#when button is clicked it changes 
from tkinter import *
window = Tk()
window.title("Welcome to HELL")
window.geometry('350x300')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

def clicked():
    btn.configure(text="Button was clicked")
btn = Button(window, text="Click Me",command=clicked, 
             bg="orange", fg="blue")
btn.grid(column =1, row= 0)

window.mainloop()


