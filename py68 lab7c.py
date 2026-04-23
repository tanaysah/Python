#LAB 7 C

def find_max_min(lst):
    max_val = lst[0]
    min_val = lst[0]

    for n in lst:
        if n > max_val:
            max_val = n
        if n < min_val:
            min_val = n

    return max_val, min_val

print(find_max_min([10, 5, 20, 2]))