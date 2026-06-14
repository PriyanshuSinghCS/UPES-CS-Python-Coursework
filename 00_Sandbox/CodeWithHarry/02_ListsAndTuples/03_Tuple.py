a = (1,2,5,6)
print(type(a))

b=(1) # b will be treated as a integer not tuple
print(type(b))

c=(1,)
print(type(c))

d = (1,45,82.55,False,"Rohit","SHIV")
print(type(d))
# tuple is immutable means its value of any index can't be changed

e = ()
print(type(e))

f = []
print(type(f))

g = {}
print(type(g))

h = ""
print(type(h))

matrix_3d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

for layer in matrix_3d:
    for row in layer:
        print(row)