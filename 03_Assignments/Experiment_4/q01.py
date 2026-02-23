# Write a program to count and display the number of capital letters in a given string. 

text = input("Enter a string: ")
count = 0
for ch in text:
    if 'A' <= ch <= 'Z':
        count += 1

print("Number of capital letters:", count)