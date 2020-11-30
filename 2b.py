"""
Youtube Video Link :- https://youtu.be/bKGVA-wbpAg

Define a function that computes the length of a given list or string.

Save File as 2b.py
Run :- python 2b.py

"""

#Length of string
s = input("Enter a string :- ")
count=0 
for i in s:
	count=count+1
print(count)
print()
print(len(s))

#Length of list
lst=["python",2,5,7,2.9]
count=0
for i in lst:
	count = count+1
print(count)
print()
print(len(lst))
