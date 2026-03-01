L = [12, -3, 7, 0, 12, 45, -3, 9, 0, 21]

unique_list = []
for x in L:
    if x not in unique_list:
        unique_list.append(x)

positives = sorted([x for x in unique_list if x > 0])
zeros = [x for x in unique_list if x == 0]
negatives = sorted([x for x in unique_list if x < 0], reverse=True)

reordered_list = positives + zeros + negatives

sorted_unique = sorted(unique_list)
second_smallest = sorted_unique[1]
second_largest = sorted_unique[-2]

rebuilt_list = [x for x in reordered_list]

print("Original List:", L)
print("1. Unique List (no set):", unique_list)
print("2. Reordered List:", reordered_list)
print("3. Second Smallest:", second_smallest)
print("   Second Largest:", second_largest)
print("4. Rebuilt List (Comprehension):", rebuilt_list)