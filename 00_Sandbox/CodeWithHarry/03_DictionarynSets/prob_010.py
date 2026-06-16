chai_types = {'Masala': 'Spicy', 'Ginger':'Zesty', 'Green': 'Fresh'}
for chai in chai_types:
    print(chai)

for chai in chai_types:
    print(chai, chai_types[chai])

for key, values in chai_types.items():
    print(key,values)

if "Masala" in chai_types:
    print("I have Masala chai")

print(len(chai_types))

# add items
chai_types["Earl Grey"] = "Citrus"
print(chai_types)

# pop
chai_types.pop("Ginger")
print(chai_types)

chai_types.popitem()
print(chai_types)

del chai_types['Green']
print(chai_types)