# WAP to enter a string and a substring. You have to print the number of times that the 
# substring occurs in the given string. String traversal will take place from left to right, not 
# from right to left. 
# Sample Input 
# ABCDCDC 
 
# CDC 
# Sample Output 
# 2 

s = input("Enter the string: ")
sub = input("Enter the substring: ")
count = 0
n = len(s)
m = len(sub)

for i in range(n - m + 1):
    if s[i:i+m] == sub:
        count += 1

print(count)