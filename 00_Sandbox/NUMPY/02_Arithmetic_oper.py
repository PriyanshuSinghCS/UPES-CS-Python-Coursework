import numpy as np

x = np.array([[1, 2],[3,4]])
y = np.array([[11, 12],[13,14]])

z = x+y
print(z)
print()

w = y-x
print(w)
print()

v = y*x  # Not matrix Multiplication
print(v)
print()

u = y@x   # Matrix Multiplication
print(u)
print()

t = y/x
print(t)
print()

s = y//x  # floor division (remove values after decimal)
print(s)
print()

r = y**x
print(r)
print()

q = y%x
print(q)
print()

# Transpose
print(x.transpose())