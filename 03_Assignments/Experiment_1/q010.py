# Write a program to swap two numbers without taking additional variable.

x=int(input('Enter first Number: '))
y=int(input('Enter second Number: '))
print("Before Swapping:")
print("X: ",x)
print("Y: ",y)
x=y-x
y=y-x
x=x+y
print("After Swapping:")
print("X: ",x)
print("Y: ",y)
