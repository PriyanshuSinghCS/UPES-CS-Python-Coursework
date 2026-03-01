# Create a dictionary of n persons where key is name and value is city.  
# a) Display all names 
# b) Display all city names 
# c) Display student name and city of all students. 
# d) Count number of students in each city. 

n = int(input("Enter number of persons: "))

d = {}

for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    d[name] = city

print("Names:")
for name in d:
    print(name)

print("Cities:")
for name in d:
    print(d[name])

print("Name and City:")
for name in d:
    print(name, "-", d[name])

city_count = {}

for name in d:
    city = d[name]
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print("Number of students in each city:")
for city in city_count:
    print(city, city_count[city])