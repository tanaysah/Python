# Import required libraries
import numpy as np

# a) Convert numbers to string type
numbers = [1, 2.0, 3]
arr = np.array(numbers, dtype=str)
print("A) Converted to string:", arr)

# b) Create 2D array with int32
arr2 = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
print("\nB) 2D Array:\n", arr2)

# c) Find rows and columns
print("\nC) Shape (rows, columns):", arr2.shape)

# d) Print 10 random numbers
rand_nums = np.random.randint(1, 101, 10)
print("\nD) Random numbers:", rand_nums)

# Q2 (a) Help on add
print("\nQ2 (a) Help on np.add:")
help(np.add)

# Q2 (b) None of elements is zero
arr3 = np.array([1, 2, 3, 4])
print("\nQ2 (b) None are zero:", np.all(arr3 != 0))

# Q2 (c) Any non-zero
print("Q2 (c) Any non-zero:", np.any(arr3 != 0))

# Q2 (d) 15 random numbers (normal distribution)
rand_normal = np.random.randn(15)
print("Q2 (d) Normal distribution:", rand_normal)