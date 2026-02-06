units=int(input("Enter the total no. of electricity units consumed: "))
customer_type=str(input("Domestic or commercial: "))
if customer_type=="Domestic":
    if units<=100:
        total=units*2
    elif units>=101 and units <=200:
        total = 100*2+(units-100)*3
    elif units>=201 and units <=300:
        total = 100*2+100*3+(units-200)*4
    elif units>300:
        total = 100*2+100*3+(units-300)*5
elif customer_type=="commercial":
    if units<=100:
        total=units*3
    elif units>=101 and units <=200:
        total = 100*3+(units-100)*5
    elif units>200:
        total = 100*2+100*5+(units-200)*7

if total>2000:
    total=total-(5/100)*total
    print("Total Bill: ",total)

else:
    print("Total Bill: ",total)
    