# Mean-Variance-Standard Deviation Calculator

This is a Python project for freeCodeCamp that calculates the mean, variance, standard deviation, max, min, and sum of rows, columns, and all elements in a 3x3 matrix using NumPy.

## 📌 Project Requirements

- Input: A list of 9 numeric values
- Output: A dictionary with statistical values calculated over:
  - Rows (axis 1)
  - Columns (axis 0)
  - Flattened matrix

## ✅ Example

```python
from mean_var_std import calculate

print(calculate([0,1,2,3,4,5,6,7,8]))
