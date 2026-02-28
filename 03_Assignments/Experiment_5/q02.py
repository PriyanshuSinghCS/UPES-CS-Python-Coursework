# Create a tuple to store n numeric values and find average of all values. 

n = int(input("Enter n: "))

values = []

for i in range(n):
    num = int(input())
    values.append(num)

t = tuple(values)
total = 0
for x in t:
    total += x

avg = total / n

print("Average:", avg)