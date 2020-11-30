"""
Youtube Video Link :- https://youtu.be/zQ-y_FGFF5k

Design a database application to that allows the user to add, delete and modify
the records.

Save File as 10c.py
Run :- python 10c.py

"""
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="",
	database="bscit"
	)
#print(mydb)
mycursor = mydb.cursor()

#ADD
sql="insert into students(name, email, age, mobile) values(%s,%s,%s,%s)"
val=[
	('sanju','sanju@gmail.com','19','789464215'),
	('prathmesh', 'prathmesh@gmail.com','20','65451545')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Record was inserted")

#Delete
mycursor.execute("delete from students where age > 22")
mydb.commit()
print(mycursor.rowcount, "Records deleted")

#modify
mycursor.execute("update students set email='rahul21@gmail.com' where email='rahul@gmail.com'")
mydb.commit()
print(mycursor.rowcount, "records changed")
