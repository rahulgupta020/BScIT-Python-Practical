"""
Youtube Video Link :- https://youtu.be/OfpLHDsDgzQ

Design a database application to search the specified record from the database

Save File as 10b.py
Run :- python 10b.py

"""
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="",
	database="bscit"
	)
# print(mydb)
mycursor = mydb.cursor()

mycursor.execute("select * from students where age > '22'")
result = mycursor.fetchall()
#print(result)
for x in result:
	print(x)
