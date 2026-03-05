check_values = lambda my_dict : len(set(my_dict.values())) == 1

data = {'item1': 50, 'item2': 50, 'item3': 50}

print("Are all values the same?", check_values(data))