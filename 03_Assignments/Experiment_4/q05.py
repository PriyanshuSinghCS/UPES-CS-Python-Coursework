# Given a string containing both upper and lower case alphabets. Write a Python program 
# to count the number of occurrences of each alphabet (case insensitive) and display the 
# same. 
# Sample Input 
# ABaBCbGc 
# Sample Output 
# 2A 
# 3B 
# 2C 
# 1G

s = input("Enter the string: ")

freq = [0]*26

for ch in s:
    if 'A' <= ch <= 'Z':
        i = ord(ch) - ord('A')
        freq[i] += 1
    elif 'a' <= ch <= 'z':
        i = ord(ch) - ord('a')
        freq[i] += 1

for i in range(26):
    if freq[i] != 0:
        print(freq[i], chr(i + 65), sep="")