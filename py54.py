#Implement the point (1-5 whatever is applicable) for tuple.
t = (1, 2, 3)

temp = list(t)
temp.append(4)

t = tuple(temp)

print("Modified tuple:", t)
