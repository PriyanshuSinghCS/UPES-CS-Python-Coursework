# Sum all even numbers in 1 million

i=1000001
sum=0
while(i!=0):
    i-=1
    if(i%2==1):
        continue
    sum+=i
print(sum)