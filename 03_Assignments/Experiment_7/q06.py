# Write a program to create a counter to show that how many times the program is executed. 

import os

if not os.path.exists("counter.txt"):
    with open("counter.txt", "w") as f:
        f.write("0")

with open("counter.txt", "r") as f:
    count = int(f.read())

count += 1

with open("counter.txt", "w") as f:
    f.write(str(count))

print(f"This program has been executed {count} times.")