# Program to count number of unique words in a given sentence using sets. 

s = input("Enter a sentence: ")

words = []
word = ""

for ch in s:
    if ch != " ":
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""

if word != "":
    words.append(word)

unique = []

for w in words:
    found = False
    for u in unique:
        if w == u:
            found = True
            break
    if not found:
        unique.append(w)

print("Number of unique words:", len(unique))