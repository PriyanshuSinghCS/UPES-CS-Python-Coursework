# Write a program to find area of triangle when length of sides are given. 
import math
a=float(input("Enter side a: "))
b=float(input("Enter side b: "))
c=float(input("Enter side c: "))

s=(a+b+c)/2

Area=math.sqrt(s*(s-a)*(s-b)*(s-c))

print("Area of given triangle is: ",Area)