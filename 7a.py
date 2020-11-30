"""
Youtube Video Link :- https://youtu.be/VOVWfJfqSj4

Design a class that store the information of student and display the same

Save File as 7a.py
Run :- python 7a.py

"""
class Student:
	def __init__(self, rollno, name, age, phone):
		self.rollno = rollno
		self.name = name
		self.age = age
		self.phone = phone

	def display(self):
		print("Student Roll No = ", self.rollno)
		print("Student Name = ", self.name)
		print("Student age = ", self.age)
		print("Student phone number :- ", self.phone)

print("----- Enter Student Details -----")
rollno = int(input("Enter student roll number :- ")) 
name = input("Enter student name :- ")
age = int(input("Enter student age :- "))
phone = int(input("Enter student phone number :- "))

ob = Student(rollno, name, age, phone)
print("----- Display Student Details -----")
ob.display()
