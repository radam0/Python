#Nikhil Vemula
#cs61002:Alogrithm and Programming 1
#04/13/2016
#Lab09.py

import math  # importing mathematical functions
class VECTOR: # defining VECTOR class
    
    def __init__(self,i,j): #constructor is created
        self.i = i
        self.j = j
        
    def __str__(self): #returning vector values as strings
        return "("+str(self.i)+", "+str(self.j)+")"
    
    def __add__(self,a): #Performing addition of vectors
        a1 = self.i + a.i
        a2 = self.j + a.j
        return VECTOR(a1,a2)
    
    def __sub__(self,s): #Performing subtraction of vectors
        s1 = self.i - s.i
        s2 = self.j - s.j
        return VECTOR(s1,s2)
    
    def __mul__(self,m): #Performing multiplication of vectors
        if type(m) in (int,float):
            return VECTOR(self.i*m,self.j*m)
        return VECTOR(self.i*m.i, self.j*m.j)
    
    def __magnitude__(self): #Performing magnitude of vectors
        m1 = (self.i)*(self.i) 
        m2 = (self.j)*(self.j) 
        return math.sqrt(m1+m2) 
        
Vector1 = VECTOR(22,23)
Vector2 = VECTOR(24,25)
print "Operations performed are \n " #Operations like addition,subtraction,multiplication.magnitude are performed
print "Addition of vector 1 and vector 2 coordinates" #Addition operation is performed
print Vector1 + Vector2
print "Subtraction of vector 1 and vector 2 coordinates" #Subtraction operation is performed
print Vector1 - Vector2
print "Multiplication of vector 1 and vector 2 coordinates" #Multiplication operation is performed
print Vector1 * Vector2
print "Magnitude of vector 1 coordinates" #Calculation of magnitude is performed
print Vector1.__magnitude__()
print "Magnitude of vector 1 coordinates" #Calculation of magnitude is performed
print Vector2.__magnitude__()




        
