# Write a program to compute the length of the hypotenuse (c) of a right triangle using 
# Pythagoras theorem.

import math
b=float(input("Enter the base of the triangle: "))
h=float(input("Enter the height of the triangle: "))

c=math.sqrt(b**2+h**2)
print("Hypotenuse of the right triangle is: ",c)