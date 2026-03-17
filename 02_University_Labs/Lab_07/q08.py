f = open("numbers.txt", "w")
n = int(input("Enter how many numbers you want to store: "))

for i in range(n):
    num = int(input("Enter number: "))
    f.write(str(num) + "\n")

f.close()
f = open("numbers.txt", "r")

numbers = []
for line in f:
    numbers.append(int(line.strip()))

f.close()
maximum = max(numbers)
print("Maximum number:", maximum)

average = sum(numbers) / len(numbers)
print("Average:", average)

count = 0
for num in numbers:
    if num > 100:
        count += 1

print("Numbers greater than 100:", count)