# Find a factorial of given number.

num=int(input("Enter the numbr: "))
fact=1
while(num>0):
    fact=fact*num
    num=num-1
print(fact)