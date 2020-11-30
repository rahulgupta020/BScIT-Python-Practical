"""
Youtube Video Link :- https://youtu.be/prxf_MoU5ks

Try to configure the widget with various options like: bg=”red”, family=”times”,
size=18

Save File as 9a.py
Run :- python 9a.py

"""
from tkinter import *

window=Tk()
window.title("9a")
window.geometry("300x300")

my_label = Label(window, text="Python", bg="red", fg="White", font=('times',18), width=20)
my_label.pack()

window.mainloop()
