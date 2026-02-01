# Check whether the given number is divisible by 3 and 5 both.

num = int(input('Enter the number: '))
if(num % 3==0) and (num % 5==0):
    print('It is divisible by 3 and 5 both.')
else:
    print('It is NOT divisible by 3 and 5 both.')