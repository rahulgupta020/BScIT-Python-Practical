"""
Youtube Video Link :- https://youtu.be/xjsrwmzk2pI

Try to change the widget type and configuration options to experiment with
other widget types like Message, Button, Entry, Checkbutton, Radiobutton, Scale
etc.

Save File as 9b.py
Run :- python 9b.py

"""
from tkinter import *
window = Tk()

window.title("9b")
window.geometry("500x500")

my_message = Message(window, text="Registration form", relief = RAISED, width=150)
my_message.pack(pady=10)

L1=Label(window, text="Full name ")
L1.pack()
E1=Entry(window, bd=5)
E1.pack()

L1=Label(window, text="Email ")
L1.pack()
E1=Entry(window, bd=5)
E1.pack()

L1=Label(window, text="Password ")
L1.pack()
E1=Entry(window, bd=5)
E1.pack()

Button1 = Checkbutton(window, text="Remember", onvalue=1, offvalue=0)
Button1.pack()
Button2 = Checkbutton(window, text="Not Remember", onvalue=1, offvalue=0)
Button2.pack()

R1 = Radiobutton(window, text="Male", value=1)
R1.pack()
R2 = Radiobutton(window, text="Female", value=2)
R2.pack()

my_button = Button(window, text="submit")
my_button.pack(pady=20)


def sel():
	selection="Value "+str(var.get())
	label.config(text=selection)

var = DoubleVar()
scale = Scale(window,variable=var)
scale.pack()
Button = Button(window, text="Get Scale Value", command=sel)
Button.pack()
label = Label(window)
label.pack()


window.mainloop()
