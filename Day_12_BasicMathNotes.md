# 📅 Day 12 – Basic Math for AI

**Focus:** Learned basic Math concepts required for AI with coding examples.

---

## ✅ What I Learned
- Mean, Median, Mode
- Variance & Standard Deviation
- Why these are important in AI → They describe **data distribution**.

---

## 🖥 Example Code with Explanation
```python
import numpy as np
from statistics import mean, median, mode

data = [2, 4, 4, 4, 5, 7, 9]

# Mean (average)
print("Mean:", mean(data))  
# Sum of elements / count = 35 / 7 = 5

# Median (middle value)
print("Median:", median(data))  
# Sorted data = [2,4,4,4,5,7,9] → middle = 4

# Mode (most frequent value)
print("Mode:", mode(data))  
# 4 appears most frequently

# Variance (spread of data)
print("Variance:", np.var(data))  
# Average of squared differences from the mean

# Standard Deviation (square root of variance)
print("Standard Deviation:", np.std(data))