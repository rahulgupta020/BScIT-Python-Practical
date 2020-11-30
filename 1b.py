"""
Enter the number from the user and depending on whether the number is even or
odd, print out an appropriate message to the user.

Save File as 1b.py
Run :- python 1b.py

"""

n=int(input("Enter a number :- "))
if n%2==0:
	print(n, " is Even")
else:
	print(n, " is Odd")
