

# 📌 DETAILED GUIDE: CORRELATION IN PYTHON

---

## 1. WHAT IS CORRELATION?

**Correlation** measures the relationship between two variables.

It answers:

👉 *“If one variable changes, how does the other change?”*

### Types of Correlation

| Correlation Value | Meaning           |
| ----------------- | ----------------- |
| +1                | Perfect Positive  |
| 0.7 to 0.9        | Strong Positive   |
| 0.4 to 0.6        | Moderate          |
| 0                 | No Relation       |
| -0.4 to -0.6      | Moderate Negative |
| -0.7 to -1        | Strong Negative   |

---

# 2. TYPES OF CORRELATION METHODS

### (A) Pearson Correlation

* Measures **linear relationship**
* Default in Pandas
* Best for normally distributed data

### (B) Spearman Correlation

* Based on **ranked values**
* Non-linear but monotonic relationships

### (C) Kendall Correlation

* Used for **ordinal data**
* More robust for small datasets

---

# 3. LIBRARIES USED

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

---

# 4. CREATING A REALISTIC DUMMY DATASET

Let’s simulate student behavior data:

```python
data = {
    "Hours_Studied": [2,3,4,5,6,7,8,9,10,11],
    "Marks": [40,42,50,55,65,70,78,85,88,95],
    "Attendance": [60,62,65,70,75,78,80,85,90,95],
    "Sleep_Hours": [8,7,7,6,6,5,6,7,7,8],
    "Gaming_Hours": [5,4,4,3,3,2,2,1,1,0]
}

df = pd.DataFrame(data)

print("----- DATASET -----")
print(df)
```

---

# 5. BASIC EXPLORATION

### Check Basic Info

```python
print(df.info())
```

### Check for Missing Values

```python
print(df.isnull().sum())
```

---

# 6. CALCULATING CORRELATION

---

## A. FULL CORRELATION MATRIX (PEARSON)

```python
pearson_corr = df.corr()

print("\n--- Pearson Correlation Matrix ---")
print(pearson_corr)
```

This calculates correlation between ALL numerical columns.

---

## B. SPEARMAN CORRELATION

```python
spearman_corr = df.corr(method='spearman')

print("\n--- Spearman Correlation Matrix ---")
print(spearman_corr)
```

---

## C. KENDALL CORRELATION

```python
kendall_corr = df.corr(method='kendall')

print("\n--- Kendall Correlation Matrix ---")
print(kendall_corr)
```

---

# 7. FIND SPECIFIC CORRELATIONS

### Example 1 – Hours Studied vs Marks

```python
corr1 = df["Hours_Studied"].corr(df["Marks"])
print("\nCorrelation between Hours Studied and Marks:", corr1)
```

### Example 2 – Gaming vs Marks

```python
corr2 = df["Gaming_Hours"].corr(df["Marks"])
print("Correlation between Gaming Hours and Marks:", corr2)
```

---

# 8. INTERPRETATION LOGIC

```python
def interpret(corr):
    if corr > 0.7:
        return "Strong Positive Correlation"
    elif corr > 0.3:
        return "Moderate Positive Correlation"
    elif corr > 0:
        return "Weak Positive Correlation"
    elif corr == 0:
        return "No Correlation"
    elif corr > -0.3:
        return "Weak Negative Correlation"
    elif corr > -0.7:
        return "Moderate Negative Correlation"
    else:
        return "Strong Negative Correlation"

print("\nInterpretation:")
print("Hours vs Marks:", interpret(corr1))
print("Gaming vs Marks:", interpret(corr2))
```

---

# 9. VISUALIZATION SECTION

---

## A. Scatter Plot: Hours vs Marks

```python
plt.figure()
plt.scatter(df["Hours_Studied"], df["Marks"])
plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()
```

---

## B. Scatter Plot: Gaming vs Marks

```python
plt.figure()
plt.scatter(df["Gaming_Hours"], df["Marks"])
plt.title("Gaming Hours vs Marks")
plt.xlabel("Gaming Hours")
plt.ylabel("Marks")
plt.show()
```

---

## C. HEATMAP USING MATPLOTLIB

```python
plt.figure(figsize=(7,5))
plt.imshow(pearson_corr, cmap='coolwarm')
plt.colorbar()

plt.xticks(range(len(pearson_corr)), pearson_corr.columns, rotation=45)
plt.yticks(range(len(pearson_corr)), pearson_corr.columns)

plt.title("Correlation Heatmap")
plt.show()
```

---

# 10. HANDLING MISSING VALUES (REAL WORLD)

If dataset has missing values:

```python
df_filled = df.fillna(df.mean())
```

Then calculate correlation:

```python
df_filled.corr()
```

---

# 11. USING CORRELATION FOR AI / ML

### Feature Selection Idea

Remove weakly correlated features:

```python
target_corr = df.corr()["Marks"]
print(target_corr)
```

You may drop:

* Columns with very low correlation with target
* Highly correlated independent features (multicollinearity)

---

# 12. EXPORT RESULTS

Save correlation matrix:

```python
pearson_corr.to_csv("correlation_matrix.csv")
```

---

# 13. COMPLETE PROGRAM (ALL-IN-ONE)

Below is the entire runnable program:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create Dummy Data
data = {
    "Hours_Studied": [2,3,4,5,6,7,8,9,10,11],
    "Marks": [40,42,50,55,65,70,78,85,88,95],
    "Attendance": [60,62,65,70,75,78,80,85,90,95],
    "Sleep_Hours": [8,7,7,6,6,5,6,7,7,8],
    "Gaming_Hours": [5,4,4,3,3,2,2,1,1,0]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)

# Correlation Matrices
pearson = df.corr()
spearman = df.corr(method='spearman')
kendall = df.corr(method='kendall')

print("\nPearson:\n", pearson)
print("\nSpearman:\n", spearman)
print("\nKendall:\n", kendall)

# Individual Correlations
c1 = df["Hours_Studied"].corr(df["Marks"])
c2 = df["Gaming_Hours"].corr(df["Marks"])

print("\nHours vs Marks:", c1)
print("Gaming vs Marks:", c2)

# Visualization
plt.figure()
plt.scatter(df["Hours_Studied"], df["Marks"])
plt.title("Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()

plt.figure(figsize=(6,4))
plt.imshow(pearson, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(pearson)), pearson.columns, rotation=45)
plt.yticks(range(len(pearson)), pearson.columns)
plt.title("Correlation Heatmap")
plt.show()

# Save Result
pearson.to_csv("correlation_output.csv")
print("\nCorrelation matrix saved as CSV")
```

---

# 14. REAL-WORLD APPLICATIONS

Correlation is used in:

* Feature Engineering
* Stock Market Analysis
* RAG Data Cleaning
* Computer Vision Dataset Analysis
* Anomaly Detection
* Recommendation Systems

---

## FINAL THOUGHT (AI ENGINEERING VIEW)

In AI workflows:

👉 **Correlation helps to:**

* Remove redundant features
* Understand relationships
* Improve model performance
* Reduce overfitting

---


