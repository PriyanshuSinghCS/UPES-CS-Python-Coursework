#  Input a sentence and print words in separate lines.

text = input("Enter a sentence: ")

word = ""

for ch in text:
    if ch != " ":
        word += ch
    else:
        print(word)
        word = ""

if word != "":
    print(word)