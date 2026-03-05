# Add few names, one name in each row, in “name.txt file”. 
# a. Count no of names 
# b. Count all names starting with vowel 
# c. Find longest name 

with open("name.txt", "w") as f:
    f.write("Priyanshu\nAman\nIshita\nOm\nUpasna\n")

with open("name.txt", "r") as f:
    names = f.read().splitlines()

print("Total names:", len(names))

vowels = "AEIOUaeiou"
vowel_count = 0
for name in names:
    if name[0] in vowels:
        vowel_count += 1
print("Names starting with a vowel:", vowel_count)

longest = max(names, key=len)
print("Longest name is:", longest)