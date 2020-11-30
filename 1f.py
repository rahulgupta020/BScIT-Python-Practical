"""
Youtube Video Link :- https://youtu.be/CDrjzWfS9nU

Write a recursive function to print the factorial for a given number.

Save File as 1f.py
Run :- python 1f.py

"""
def fact(n):
	if(n==1):
		return 1
	else:
		return n*fact(n-1)

n=int(input("Enter a number :- "))
result=fact(n)
print(result)
