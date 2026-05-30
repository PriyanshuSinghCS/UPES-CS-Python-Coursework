setOne = {1, 2, 3, 4}
a = setOne & {1, 3}  # Intersection
print(a)

b = setOne | {1,3,7}  # Union
print(b)

c = setOne - {1, 2, 3, 4, 7}
print(c)   # set()  , Empty set denotion

print(type({}))