arr = np.array([[5, 8, 2],
                [7, 3, 9],
                [4, 6, 1]])

# Row sum
print("Row sums:", np.sum(arr, axis=1))

# Column sum
print("Column sums:", np.sum(arr, axis=0))

# Second maximum element
second_max = np.sort(arr.flatten())[-2]
print("Second maximum element:", second_max)