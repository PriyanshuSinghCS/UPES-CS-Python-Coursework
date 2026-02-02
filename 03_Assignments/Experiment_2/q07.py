# Write a program which takes any date as input and display next date of the calendar 
# e.g. 
# I/P: day=20 month=9 year=2005  
# O/P: day=21 month=9 year 2005 

day=int(input("Enter the day: "))
month=int(input("Enter the month: "))
year=int(input("Enter the year: "))
print("\n")
print("Day =",day," Month =",month," Year =",year)
leapyear=0
if year%400==0 or (year%4==0 and year%100!=0):
    leapyear=1

if month==2:
    if leapyear==1:
        max_days=29
    else:
        max_days=28

elif month in (1,3,5,7,8,10,12):
    max_days=31
else:
    max_days=30

if day<max_days:
    day=day+1
else:
    if month<12:
        day=1
        month=month+1
    else:
        day=1
        month=1
        year=year+1
print("Next Date:")
print("Day =",day," Month =",month," Year =",year)


