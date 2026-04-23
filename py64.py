try:
    with open("city.txt", "r") as f:
        lines = f.readlines()

    total_area = 0

    print("\nAll City Details:")
    for line in lines:
        name, pop, area = line.split()
        pop = float(pop)
        area = float(area)

        print(name, pop, area)

        if pop > 10:
            print("Population >10L:", name)

        total_area += area

    print("Total Area:", total_area)

except Exception as e:
    print("Error:", e)