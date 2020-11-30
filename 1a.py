"""
Youtube Video Link :- https://youtu.be/SW40L6CzOA4

Create a program that asks the user to enter their name and their age. Print out a
message addressed to them that tells them the year that they will turn 100 years
old.

Save File as 1a.py
Run :- python 1a.py

"""

import datetime
name=input("Enter your name :- ")
age=int(input("Enter your age :- "))
currentyear=datetime.datetime.now().year
dob=currentyear - age
print(dob+100)
