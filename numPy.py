import numpy as np

# ===========================
# NumPy Array Creation
# ===========================
# Creating a one-dimensional array
array = np.array([1, 2, 3, 4, 5])
print("One-dimensional array:", array)

# Creating a multi-dimensional array
multi_array = np.array([[['A', 'B', 'C'], ['Cc', 'D', 'E'], ['F', 'G', 'H']],
                         [['I', 'J', 'K'], ['L', 'M', 'N'], ['O', 'P', 'Q']],
                         [['R', 'S', 'T'], ['U', 'V', 'W'], ['X', 'Y', 'Z']]])
print("Element at [2][2][1]:", multi_array[2][2][1])
print("Shape of multi-dimensional array:", multi_array.shape)
print("Number of dimensions:", multi_array.ndim)

# ===========================
# Slicing in NumPy
# ===========================
array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]])
print("Sliced array (2:, 2:4):", array_2d[2:, 2:4])

# ===========================
# Array Arithmetic with Scalars
# ===========================
array = np.array([1, 2, 3])
print("Array + 1:", array + 1)
print("Array - 2:", array - 2)
print("Array * 3:", array * 3)
print("Array / 4:", array / 4)
print("Array ** 5:", array ** 5)
print("Square root of array:", np.sqrt(array))

# ===========================
# Vectorized Math Functions
# ===========================
array2 = np.array([1.34, 2.645, 3.99])
print("Rounded array:", np.round(array2))
print("Floor of array:", np.floor(array2))
print("Ceiling of array:", np.ceil(array2))
print("Value of pi:", np.pi)

# ===========================
# Exercises
# ===========================
print("Pi * array ** array:", np.pi * array ** array)

# Exercise 2
array3 = np.array([4, 5, 6])
print("Array + array3:", array + array3)
print("Array - array3:", array - array3)
print("Array * array3:", array * array3)
print("Array / array3:", array / array3)
print("Array ** array3:", array ** array3)

# Exercise 3
score = np.array([55, 78, 67, 99, 100, 86])
print("Scores <= 88:", score <= 88)
print("Scores == 100:", score == 100)
score[score < 66] = 0
print("Updated scores:", score)

# ===========================
# Broadcasting
# ===========================
array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
array2 = np.array([[1], [2], [3], [4]])
print("Broadcasting result:", array1 * array2)

# ===========================
# Aggregate Functions
# ===========================
array_agg = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Minimum value:", np.min(array_agg))
print("Maximum value:", np.max(array_agg))
print("Mean value:", np.mean(array_agg))
print("Standard deviation:", np.std(array_agg))
print("Sum of array:", np.sum(array_agg))

# ===========================
# Filtering
# ===========================
ages = np.array([[22, 44, 66, 34, 17, 87, 99, 13, 83, 32],
                 [34, 85, 74, 35, 16, 35, 46, 76, 65, 92]])
teenagers = ages[(ages >= 18) & (ages <= 65)]
print("Teenagers:", teenagers)

# ===========================
# Random Numbers in NumPy
# ===========================
rng = np.random.default_rng()
array_random = np.array(['🍎', '🍌', '🍍', '🥑'])
rng.shuffle(array_random)
print("Shuffled array:", array_random)
