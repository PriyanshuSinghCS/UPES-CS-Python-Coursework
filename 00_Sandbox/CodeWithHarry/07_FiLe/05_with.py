# f = open("file02.txt")
# print(f.read())
# f.close()


# The same can be written using with statement like this:
with open("file02.txt") as f:
    print(f.read())

# You don't have to explicitily close the file