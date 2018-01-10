# CS62001: Algorithms and Programming 1 
# Name: Nikhil Vemula,
# Date: Jan 26 2015
# Lab02.py

##This assignment will give you experience on the use of:
##1. Integers and floats
##2. Mathematical operations
##3. The float(), int(), round(), print(), and input()functions
##4. Importing a Python module

import math
length=float(input ("enter length of side of garden in feet:"))
spacing=float(input("enter spacing between plants in feet:"))
depth=float(input("enter depth of garden soil in feet:"))
fill=float(input("enter depth of fill in feet:"))
radius=length/4
area=(math.pi * (radius**2))/2
semit=math.trunc(area / (spacing**2))
area=math.pi * (radius**2)
circt=math.trunc(area / (spacing**2))
tp=circt + (semit*4)
volume=(math.pi * (radius**2) * depth)/2
cv=volume/27
cvrs=round(cv,1)
volume=(math.pi*(radius**2)*depth)/2
cvrc=round(cv,1)
total=(cvrs * 4) +cvrc
totalr=round(total,1)
tv=(length**2)*fill
tcs=(math.pi*(radius**2)*depth)*3
tf=tv-tcs
ctf=tf/27
ctfr=round(ctf,1)
print("plants for each semicircle garden:",semit)
print("plants for the circle garden:",circt)
print("total plants for garden:",tp)
print("soil for each semicircle garden:",cvrs)
print("total soil for the garden:",totalr)
print("total fill for the garden:",ctfr)




