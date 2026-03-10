# Assume a file city.txt with details of 5 cities in given format (cityname population(in 
# lakhs) area(in sq KM) ): 
# Example: 
# Dehradun 5.78 308.20 
# Delhi 190 1484 
# …………… 
# Open file city.txt and read to: 
# a. Display details of all cities 
# b. Display city names with population more than 10Lakhs 
# c. Display sum of areas of all cities

with open("city.txt", "w") as f:
    f.write("Dehradun 5.78 308.20\n")
    f.write("Delhi 190 1484\n")
    f.write("Mumbai 124 603\n")

total_area = 0.0

print("--- City Details ---")
with open("city.txt", "r") as f:
    for line in f:
        parts = line.split()
        name = parts[0]
        pop = float(parts[1])
        area = float(parts[2])

        print(f"City: {name}, Population: {pop}L, Area: {area} sq KM")

        if pop > 10:
            print(f"-> {name} has a large population.")

        total_area += area

print("\nTotal area of all cities:", total_area)