# Write a program to find simple interest.

p=float(input('Enter the Principle Amount: '))
r=float(input('Enter the Rate of Interest: '))
t=float(input('Enter the Time: '))

si=(p*r*t)/100
print("Simple Interest: ",si)