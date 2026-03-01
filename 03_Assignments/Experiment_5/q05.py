#  Store details of n movies in a dictionary by taking input from the user. Each movie must 
# store details like name,  year, director name, production cost, collection made (earning) 
# & perform the following :- 
# a) print all movie details 
# b) display name of movies released before 2015 
# c) print movies that made a profit. 
 
# d) print movies directed by a particular director.

n = int(input("Enter number of movies: "))

movies = {}

for i in range(n):
    name = input("Enter movie name: ")
    year = int(input("Enter year: "))
    director = input("Enter director name: ")
    cost = int(input("Enter production cost: "))
    collection = int(input("Enter collection made: "))

    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

print("All movie details:")
for m in movies:
    print(m, movies[m])

print("Movies released before 2015:")
for m in movies:
    if movies[m]["year"] < 2015:
        print(m)

print("Movies that made a profit:")
for m in movies:
    if movies[m]["collection"] > movies[m]["cost"]:
        print(m)

d = input("Enter director name to search: ")
print("Movies directed by", d)
for m in movies:
    if movies[m]["director"] == d:
        print(m)