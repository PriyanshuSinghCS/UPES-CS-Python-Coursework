# Write a Python function to find the maximum and minimum numbers from a sequence of 
# numbers.  (Note: Do not use built-in functions.) 

def find_max_min(numbers):
    if len(numbers) == 0:
        return None, None

    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum


nums = [12, 45, 7, 23, 89, 34]
max_value, min_value = find_max_min(nums)

print("Maximum:", max_value)
print("Minimum:", min_value)