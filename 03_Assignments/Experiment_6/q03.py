def print_numbers(n, current=1):
    if current > n:
        return
    print(current)
    print_numbers(n, current + 1)

num = int(input("Enter n: "))
print_numbers(num)