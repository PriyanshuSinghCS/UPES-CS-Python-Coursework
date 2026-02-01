# Find the greatest among the two numbers. If numbers are equal than print “numbers are equal”.

num1 = int(input('Enter First number: '))
num2 = int(input('Enter Second number: '))
if(num1>num2):
    print('First number is greater than second.')
elif(num1<num2):
    print('Second number is greater than first.')
else:
    print('Both Numbers are equal.')

