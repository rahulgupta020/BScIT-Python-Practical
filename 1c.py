"""
Youtube Video Link :- https://youtu.be/51mPPDleddI

Write a program to generate the Fibonacci series.

Save File as 1c.py
Run :- python 1c.py

"""
n=int(input("Enter a number :- "))
first=0
second=1
for i in range(n):
   print(first)
   temp=first
   first=second
   second = second+temp
