letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>","Singh").replace("<|Date|>","10 March"))  # chaining of .replace function
print(letter) # Original letter string doesn"t changed because strings are immutable which means
# that you cannot change them by running functions on them