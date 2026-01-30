# Find largest number in 1 million divisible by 17

i=1000000
while(i!=0):
    if(i%17==0):
        break
    i=i-1
print(i)