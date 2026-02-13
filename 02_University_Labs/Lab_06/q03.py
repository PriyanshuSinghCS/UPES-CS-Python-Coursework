x=[3,5,1,7]
print(x)

x.append(5)
print(x)

t=[100,200]
x.extend(t)
print(x)

i=2
a=100
x.insert(i,a)
print(x)

i=2
m=x.pop(i)
print(m)
print(x)

n=len(x)
s=sum(x)
print(n)
print(s)