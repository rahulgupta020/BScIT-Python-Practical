"""
Youtube Video Link :- https://youtu.be/PedX5TQZuPQ

Design a simple database application that stores the records and retrieve the
same

Save File as 10a.py
Run :- python 10a.py

"""
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="",
	database ="bscit"
	)
# print(mydb)
mycursor = mydb.cursor()

mycursor.execute("drop table if exists students")
print("student table drop")

mycursor.execute("""create table students(id int auto_increment primary key, 
				name varchar(25), email varchar(25), age varchar(5), mobile varchar(10))""")
print("table created")
	
sql="insert into students(name, email, age, mobile) values(%s, %s, %s, %s)"
val=[
	('Rahul', 'rahul@gmail.com', '21', '8796135214'),
	('rajan', 'rajan@gmail.com', '22', '8796135211'),
	('roshan', 'roshan@gmail.com', '23', '879613522'),
	('deepak', 'deepak@gmail.com', '24', '8796135214')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Record was inserted.")

print()

mycursor.execute("select * from students")
myresult = mycursor.fetchall()
# print(myresult)
for x in myresult:
	print(x)
