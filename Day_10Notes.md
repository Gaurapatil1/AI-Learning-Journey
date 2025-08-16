# 📅 Day 10 – Numpy Revision

**Focus:** Revised core Numpy concepts in 1-hour focused session.

## ✅ What I Revised
- Array creation (`np.array`, `np.zeros`, `np.ones`, `np.arange`)
- Array slicing (basic, step, negative indexing)
- 2D array indexing (accessing rows, columns, and specific elements)
- Quick exercises from lab + personal dataset

## 🖥 Example Code
```python
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

print("Basic Slicing:", arr[2:7])     # [3 4 5 6 7]
print("With Step:", arr[1:8:2])       # [2 4 6 8]
print("Negative indexing:", arr[-3])  # 6

arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print("Specific element:", arr_2d[1,2])   # 6