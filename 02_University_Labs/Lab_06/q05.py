from random import randint as randi
x=[]
N=1000000
for k in range (N):
    r= randi(1,6)
    x.append(r)
    x[k]=r

print(x)