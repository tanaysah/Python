# Read names from file
try:
    with open("name.txt", "r") as f:
        names = [line.strip() for line in f.readlines()]

    # a. Count names
    print("Total names:", len(names))

    # b. Names starting with vowel
    vowels = "AEIOUaeiou"
    vowel_names = [name for name in names if name and name[0] in vowels]
    print("Names starting with vowel:", len(vowel_names))

    # c. Longest name
    longest = names[0]
    for name in names:
        if len(name) > len(longest):
            longest = name
    print("Longest name:", longest)

except FileNotFoundError:
    print("File not found!")