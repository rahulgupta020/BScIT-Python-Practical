"""
Youtube Video Link :- https://youtu.be/zpkP7AhzO08

Write a Python program to read last n lines of a file.

Save File as 6c.py
Run :- python 6c.py

"""
n=int(input("Enter n lines :- "))
f = open("myfile.txt","r")
for line in (f.readlines() [-n:]):
	print(line,end="")
f.close()
