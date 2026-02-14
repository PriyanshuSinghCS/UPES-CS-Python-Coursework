# Find whether the given number is Armstrong number.

num =int(input("Enter a number: "))

original = num
n =len(str(num))
sum_of_powers = 0
while num>0:
    digit = num%10
    sum_of_powers += digit ** n
    num //= 10
if sum_of_powers==original:
    print("It is an Armstrong number")
else:
    print("It is NOT an Armstrong number")
