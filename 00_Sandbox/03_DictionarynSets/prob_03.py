# Can we have a set with 18 (int) and '18' (str) as a value in it?
# s=()   invalid because s now became a touple
s = set()
s.add(18)
s.add("18")
print(s)