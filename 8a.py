"""
Youtube Video Link :- https://youtu.be/u8nyJ80vn_Y

Open a new file in IDLE (“New Window” in the “File” menu) and save it as
geometry.py in the directory where you keep the files you create for this course.
Then copy the functions you wrote for calculating volumes and areas in the
“Control Flow and Functions” exercise into this file and save it.
Now open a new file and save it in the same directory. You should now be able 
16
to importyour own module like this:
importgeometry
Try and add print dir(geometry) to the file and run it.
Now write a function pointyShapeVolume(x, y, squareBase) that calculates the
volume of a square pyramid if squareBase is True and of a right circular cone if
squareBase is False. x is the length of an edge on a square if squareBase is True
and the radius of a circle when squareBase is False. y is the height of the object.
First use squareBase to distinguish the cases. Use the circleArea and squareArea
from the geometry module to calculate the base areas.


Save File as 8a.py
Run :- python 8a.py

"""

geometry.py

import math
def circleArea(r):
    return math.pi*r*r
def squareArea(a):
    return a**2

8a.py

import geometry
print(dir(geometry))

def pointyShapeVolume(x,y,squareBase):
    if squareBase:
        base=((geometry.squareArea(x))*(y/3))
        return base
    else:
        base=(geometry.circleArea(x)*y)/3
        return base
print(pointyShapeVolume(2,3,True))
print(pointyShapeVolume(2,4,False))
