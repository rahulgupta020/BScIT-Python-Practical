"""
Youtube Video Link :- https://youtu.be/bZKs65uK1Eg

Create a class called Numbers, which has a single class attribute called
MULTIPLIER, and a constructor which takes the parameters x and y (these should
all be numbers).
i. Write a method called add which returns the sum of the attributes x and y.
ii. Write a class method called multiply, which takes a single number
parameter a and returns the product of a and MULTIPLIER.
iii. Write a static method called subtract, which takes two number parameters, b
and c, and returns b - c.
iv. Write a method called value which returns a tuple containing the values of x
and y. Make this method into a property, and write a setter and a deleter for
manipulating the values of x and y.

Save File as 7c.py
Run :- python 7c.py

"""
class Numbers:
	MULTIPLIER=5
	def __init__(self,x,y):
		self.x=x
		self.y=y
	#subpart-1
	def add(self):
		return self.x + self.y

	#subpart-2
	@classmethod
	def multiply(cls,a):
		return cls.MULTIPLIER * a

	#subpart-3
	@staticmethod
	def substract(b,c):
		return b-c

	#subpart-4
	@property
	def value(self):
		return(self.x, self.y)
	@value.setter
	def value(self, t):
		self.x = t[0]
		self.y = t[1]
	@value.deleter
	def value(self):
		self.x=None
		self.y=None

ob=Numbers(10,20)
print("Add :- ",ob.add())
print("Multiply :- ", Numbers.multiply(10))
print("Substract :- ", Numbers.substract(20,10))

ob.value=(100,200)
print("Add :- ", ob.add())

del ob.value
print("Values :- ",ob.value)
