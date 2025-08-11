# numpy.py

# ✅ 1. Importing NumPy
import numpy as np  # np is the standard alias for NumPy

# ✅ 2. Creating Arrays
arr1 = np.array([1, 2, 3])  # 1D array
arr2 = np.array([[1, 2], [3, 4]])  # 2D array

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# ✅ 3. Array Attributes
print("Shape:", arr2.shape)      # (2, 2): 2 rows, 2 columns
print("Size:", arr2.size)        # Total elements: 4
print("Data Type:", arr2.dtype)  # Usually int32 or int64
print("Dimensions:", arr2.ndim)  # 2D

# ✅ 4. Indexing & Slicing
print("arr1[1]:", arr1[1])       # Access second element
print("arr2[0][1]:", arr2[0][1]) # First row, second column
print("arr2[:, 1]:", arr2[:, 1]) # All rows, second column

# ✅ 5. Array Operations (element-wise)
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# ✅ 6. Broadcasting
# Allows operations between arrays of different shapes
c = np.array([[1], [2], [3]])
d = np.array([10, 20, 30])
print("Broadcast Result:\n", c + d)  # Adds d to each row of c

# ✅ 7. Useful Array Generators
print("Zeros:\n", np.zeros((2, 3)))         # 2x3 matrix of 0s
print("Ones:\n", np.ones((2, 2)))           # 2x2 matrix of 1s
print("Arange:", np.arange(0, 10, 2))       # [0 2 4 6 8]
print("Linspace:", np.linspace(0, 1, 5))    # 5 evenly spaced values from 0 to 1

# ✅ 8. Reshape & Flatten
e = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Shape:", e.shape)
print("Reshaped to (3,2):\n", e.reshape(3, 2))
print("Flattened:", e.flatten())  # Converts to 1D array

# ✅ 9. Aggregations (with axis)
print("Sum:", e.sum())
print("Mean:", e.mean())
print("Max:", e.max())
print("Row-wise Sum:", e.sum(axis=1))   # Sum across columns
print("Column-wise Sum:", e.sum(axis=0))  # Sum across rows

# ✅ 10. Boolean Masking
f = np.array([5, 10, 15, 20])
mask = f > 10
print("Mask:", mask)             # [False False  True  True]
print("Filtered:", f[mask])      # [15 20]

# ✅ 11. Random Numbers
np.random.seed(42)  # Ensures reproducibility
print("Random floats:", np.random.rand(3))  # 3 random numbers between 0 and 1
print("Random integers:\n", np.random.randint(1, 100, size=(2, 2)))  # 2x2 matrix

# ✅ 12. Copy vs View
g = np.array([1, 2, 3])
view_g = g[1:]     # This is a view, shares memory with g
copy_g = g.copy()  # This is a separate copy

view_g[0] = 100    # Changes original array
copy_g[0] = 200    # Does not affect original

print("Original g after modifying view:", g)   # g becomes [1, 100, 3]
print("Copy_g (unchanged):", copy_g)           # [200, 2, 3]

img = np.random.randint(0, 255, (28, 28))  # Fake 28x28 grayscale image
print("Shape:", img.shape)
flattened = img.flatten()  # Neural nets like 1D input
