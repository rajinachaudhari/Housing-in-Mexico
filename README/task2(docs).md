# Task 2: Data Wrangling and Cleaning in Python – Beginner-Friendly Documentation

This documentation explains every step and concept from your `task2.py` file, with comments and simple explanations for beginners.

---

## 1. Project Overview
- This project is about descriptive data science: loading, cleaning, and preparing real estate data from Mexico for analysis.

---

## 2. Loading Data
- **pandas** is a Python library for working with tables (DataFrames).
- We load three messy CSV files into DataFrames:
```python
import pandas as pd
# Load CSV files into DataFrames
df1 = pd.read_csv("data/mexico_real_estate_messy_v1.csv")
df2 = pd.read_csv("data/mexico_real_estate_messy_v2.csv")
df3 = pd.read_csv("data/mexico_real_estate_messy_v3.csv")
```
- Each DataFrame is a table with rows and columns.

---

## 3. Inspecting Data
- Check the type and shape (rows, columns) of each DataFrame:
```python
print(type(df1))
print(df1.shape)
print(df1.head())      # Shows first 5 rows
print(df1.info())      # Shows summary info (nulls, datatypes)
print(df1.describe())  # Shows stats for numeric columns
```

---

## 4. Handling Missing Values (NaN)
- Remove rows with any missing (null) values:
```python
df1.dropna(inplace=True)
```
- This keeps only complete rows for analysis.

---

## 5. Cleaning and Converting Data Types
- Some columns (like `price_usd` and `area_m2`) are stored as text (object) instead of numbers.
- Remove symbols like `$`, `,`, and replace invalid entries (like `???`) with NaN:
```python
df1["price_usd"] = df1["price_usd"].replace("???", pd.NA).str.replace("$", "", regex=False).str.replace(",", "", regex=False)
df1.dropna(inplace=True)
df1["price_usd"] = df1["price_usd"].astype(float)
```
- Do the same for `area_m2` and other columns as needed.

---

## 6. Identifying and Fixing Invalid Data
- Find rows with invalid values (like `???` or dates in numeric columns):
```python
invalid_prices = df1[~df1["price_usd"].str.replace(".", "", 1).str.isnumeric()]
invalid_areas = df1[~df1["area_m2"].str.replace(",", "", 1).str.isnumeric()]
```
- Replace these with NaN and drop them.

---

## 7. Cleaning Other DataFrames
- Repeat similar cleaning steps for `df2` and `df3`:
    - Remove symbols and convert to numbers.
    - Replace invalid entries with NaN and drop them.
    - Convert prices from Mexican Pesos to USD for consistency.
    - Split columns (like `lat-lon` and `place_with_parent_names`) to create new columns for latitude, longitude, and state.

---

## 8. Combining Cleaned Data
- Concatenate (stack) all cleaned DataFrames into one big DataFrame:
```python
df = pd.concat([df1, df2, df3])
```
- This gives a single, tidy dataset ready for analysis.

---

## 9. Saving the Clean Data
- Save the final cleaned DataFrame to a new CSV file:
```python
df.to_csv("data/mexico-real-estate-clean.csv", index=False)
```
- This file is now ready for further analysis and visualization.

---

## 10. Key Concepts Learned
- How to load data from CSV files into pandas DataFrames.
- How to inspect, clean, and transform messy real-world data.
- How to handle missing values and invalid entries.
- How to convert text columns to numeric types safely.
- How to extract new columns from complex string fields.
- How to combine multiple datasets into one.
- How to save your cleaned data for future use.

---

## Conclusion
- You practiced advanced data wrangling using pandas.
- You learned to turn messy, real-world data into a clean, structured dataset.
- These skills are essential for any data analysis or machine learning project.
- Mastering these steps makes you confident in handling and preparing data for deeper analysis!
