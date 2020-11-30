"""
Youtube Video Link :- https://youtu.be/J1rGejlBs8M

Write a function that takes a character (i.e. a string of length 1) and returns True
if it is a vowel, False otherwise.

Save File as 2a.py
Run :- python 2a.py

"""
def vowel(s):
	if(s=='a' or s=='e' or s=='i' or s=='o' or s=='u' or
		s=='A' or s=='E' or s=='I' or s=='O' or s=='U'):
		return True
	else:
		return False

s=input("Enter a character :- ")
result=vowel(s)
print(result)
