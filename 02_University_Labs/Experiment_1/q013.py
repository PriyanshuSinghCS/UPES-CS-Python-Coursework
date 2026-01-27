num = int(input("Enter a number: "))
shift = int(input("Enter number of bits to shift: "))
left_shift = num << shift
right_shift = num >> shift
print("Left shift value:", left_shift)
print("Right shift value:", right_shift)
