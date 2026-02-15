# Write a program to print sum of digits. 

num =int(input("Enter a number: "))

original = num
n =len(str(num))
sum = 0
while num>0:
    digit = num%10
    sum += digit
    num //= 10
print(sum)