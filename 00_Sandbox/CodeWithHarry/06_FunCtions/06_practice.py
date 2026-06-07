# # Write a function is_even(n) that returns True if n is even, else False.

# def is_even(n):
#     return n%2==0
    
# # Write a function circle_area(r, pi=3.14159) that returns the area of a circle.

# import math
# def circle_area(r, pi=math.pi):
#     return pi*(r**2)

# # 3. Write a function average(*nums) that returns the average of any number of arguments (return 0 if none are passed).

# def average(*nums):
#     if len(nums)==0:
#         return 0
#     return nums/len(nums)

# # 4. Write a function describe(**info) that prints each key–value pair as key: value.

# def describe(**info):
#     for key, value in info.items():
#         return f"{key}, {value}"

# # 5. Write a function that returns both the sum and product of a list of numbers.

# def product_n_sum(lst):
#     total = sum(lst)
#     product = 1
#     for i in lst:
#         product = product*i
#     return total,product


# # 6. Demonstrate the mutable default argument bug with a function, then rewrite it correctly.

# def add_nuumbers(num, lst = []):
#     lst.append(num)
#     return lst

# def add_numbers(num,lst=None):
#     lst = []
#     lst.append(num)
#     return lst

# # 7. Write a higher-order function apply(func, values) that applies any single-argument function to every item in 
# #    a list and returns the new list (re-implement map's behaviour using a loop).

# # Write a function make_multiplier(n) that returns a new function. The returned function should multiply whatever it receives by n.
# # Expected behaviour:

def make_multiplier(n):
    def multiplier(n,x=5):
        return n*x
    return multiplier(n)

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))   # 10
print(triple(5))   # 15

