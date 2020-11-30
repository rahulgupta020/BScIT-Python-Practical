"""
Youtube Video Link :- https://youtu.be/v7gw2fI6vEg

Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

Save File as 5b.py
Run :- python 5b.py

"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

dic4={}
for d in (dic1, dic2, dic3):
	dic4.update(d)
print(dic4)
