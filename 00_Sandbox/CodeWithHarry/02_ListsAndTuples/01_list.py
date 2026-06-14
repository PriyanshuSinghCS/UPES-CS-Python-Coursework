# index starts from zero
# Multiple datatype can be inside a single list

friends = ["Apple", "Orange",5,345.06,False,"Singh","Faith"]
print(friends)
friends[0]="Grapes" # unlike strings lists are mutable
print(friends)

x=5+friends[2]
print(x)

print(friends[1:4])