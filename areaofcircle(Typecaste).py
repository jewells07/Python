pi=3.14
print("enter the area of circle")
circle=input()
print(type(circle))
area=int(circle)*pi
print("The area is:",area)

print("ANOTHER WAY TO FIND")
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " ,r, " is: " + str(pi * r**2))

