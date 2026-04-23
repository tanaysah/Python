# Store movie details

n = int(input("Enter number of movies: "))
movies = {}

for i in range(n):
    name = input("Movie name: ")
    year = int(input("Year: "))
    director = input("Director: ")
    cost = float(input("Production cost: "))
    collection = float(input("Collection: "))

    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

print("All Movie Details:")
for name, details in movies.items():
    print(name, details)

print("Movies released before 2015:")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

print("Profitable Movies:")
for name, details in movies.items():
    if details["collection"] > details["cost"]:
        print(name)


search_director = input("Enter director name to search: ")
print("Movies directed by", search_director)
for name, details in movies.items():
    if details["director"] == search_director:
        print(name)