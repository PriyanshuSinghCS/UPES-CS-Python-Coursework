# Store integers in a file. 
# a. Find the max number 
# b. Find average of all numbers 
# c. Count number of numbers greater than 100 

with open("numbers.txt", "w") as f:
    f.write("10\n150\n45\n200\n5\n")

with open("numbers.txt", "r") as f:
    num_list = []
    for line in f:
        num_list.append(int(line.strip()))

print("Maximum number:", max(num_list))

avg = sum(num_list) / len(num_list)
print("Average of numbers:", avg)

count_big = 0
for n in num_list:
    if n > 100:
        count_big += 1
print("Numbers greater than 100:", count_big)