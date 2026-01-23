a=float(input('Enter a pos float: '))
b=float(input('Enter a pos float: '))
aTob = a ** b
bToa= b ** a
if aTob > bToa:
 print(aTob)
else:
 print(bToa)