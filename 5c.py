"""
Youtube Video Link :- https://youtu.be/AB4S9uMpFKY

Write a Python program to sum all the items in a dictionary.

Save File as 5c.py
Run :- python 5c.py

"""
#Method2
dic2 = {'python':90, 'cpp':100, 'java':80, 'php':50}
print("sum is ")
print(sum(dic2.values()))

print()

#Method1
dic1 = {'python':90, 'cpp':100, 'java':80, 'php':50}
sum=0
for i in dic1.values():
	sum=sum+i
print(sum)
