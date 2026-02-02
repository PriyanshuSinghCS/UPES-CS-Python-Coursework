num=int(input("enter: "))
fact=1
for x in range(num):
    fact=fact*num
    num=num-1
    if num==0:
        break

print(fact)