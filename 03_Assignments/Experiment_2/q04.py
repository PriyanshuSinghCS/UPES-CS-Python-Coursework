# Find the greatest among three numbers assuming no two values are same.

num1 = int(input('Enter First number: '))
num2 = int(input('Enter Second number: '))
num3 = int(input('Enter Third number: '))
if(num1>num2) and (num1>num3):
    print('First number is greatest.')
elif(num2>num1) and (num2>num3):
    print('Second number is greatest.')
elif(num3>num1) and (num3>num2):
    print('Third number is greatest.')
