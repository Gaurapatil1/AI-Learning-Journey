# 📅 Day 11 – Basics of Data Visualization

**Focus:** Introduction to Data Visualization using Matplotlib.

---

## ✅ What I Learned
- Plotting a simple **line graph**
- Creating **bar charts**
- Making **scatter plots**
- Adding **titles, labels, and legends**

---

## 🖥 Example Code
```python
import matplotlib.pyplot as plt

# Line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, label="Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Basic Line Graph")
plt.legend()
plt.show()

# Bar chart
subjects = ["Math", "Science", "English"]
marks = [85, 90, 78]
plt.bar(subjects, marks)
plt.title("Bar Chart Example")
plt.show()

# Scatter plot
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.show()


---

⏳ Duration

1 hour practice


---

💡 Key Takeaways

Visualization makes data easy to understand

Matplotlib is the foundation for advanced libraries (Seaborn, Plotly)

Adding labels, legends, and titles makes plots meaningful


