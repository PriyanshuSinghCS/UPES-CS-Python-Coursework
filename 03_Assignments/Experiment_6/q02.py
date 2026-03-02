def sum_of_cubes(n):
    total = 0
    i = 1
    while i < n:
        total += i * i * i
        i += 1
    return total

num = int(input("Enter a positive integer: "))
print("Sum of cubes:", sum_of_cubes(num))