"""
Youtube Video Link :- https://youtu.be/Q3h39Cc7V1M

A pangram is a sentence that contains all the letters of the English alphabet at
least once, for example: The quick brown fox jumps over the lazy dog. Your task
here is to write a function to check a sentence to see if it is a pangram or not.

Save File as 3a.py
Run :- python 3a.py

"""
def pangram(str,alphabet):
	flag=True
	for char in alphabet:
		if char not in str.lower():
			flag=False

	if(flag==True):
		print("Pangram")
	else:
		print("Not Pangram")
str="The quick brown fox jumps over the lazy dog"
alphabet="abcdefghijklmnopqrstuvwxyz"
pangram(str,alphabet)
