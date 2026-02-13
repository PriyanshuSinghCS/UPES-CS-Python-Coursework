from random import randint as randi
x=[0]
k=0

while abs(x[k])<=10:
    
    r=randi(1,2)
    if r==1:
        new_x = x[k]+1
    else:
        new_x=x[k]-1
    k=k+1
    x.append(new_x)
    print(r)

print(x)
n=len(x)
print(n)
