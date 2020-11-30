"""
Youtube Video Link :- https://youtu.be/Juq8LIabnHw

Write a program that takes two lists and returns True if they have at least one
common member.

Save File as 4a.py
Run :- python 4a.py

"""
lst1=[1,2,3,4,5]
lst2=[5,6,7,8,9]
for x in lst1:
	for y in lst2:
		if(x==y):
			print("True")
