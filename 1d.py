"""
Youtube Video Link :- https://youtu.be/Jx6pDL8Gg6o

Write a function that reverses the user defined value.

Save File as 1d.py
Run :- python 1d.py

"""

def rev(n):
	reverse=0
	while(n>0):
		reminder=n%10
		reverse=(reverse*10)+reminder
		n=n//10
	return reverse
n=int(input("Enter a number :- "))
reverse1=rev(n)
print("reverse number is :- ", reverse1)
