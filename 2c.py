"""
Youtube Video Link :- https://youtu.be/wZgO-78H-WE

Define a procedurehistogram() that takes a list of integers and prints a
histogram to the screen. For example, histogram([4, 9, 7]) should print the
following:
****
*********
*******


Save File as 2c.py
Run :- python 2c.py

"""

def histogram(lst):
	for i in lst:
		print(i * '*')

lst=[]
ln=int(input("Enter the list length :- "))
print("Enter interger = ",ln)
for i in ln:
	data = int(input())
	lst.append(data)

histogram(lst)
