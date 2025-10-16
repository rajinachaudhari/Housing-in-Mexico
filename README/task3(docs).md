# Task 3: Exploratory Data Analysis and Visualization – Beginner-Friendly Documentation

This documentation explains every step and concept from your `task3.py` file, with comments and simple explanations for beginners.

---

## 1. Project Goals
- Conduct Exploratory Data Analysis (EDA) on Mexico real estate data
- Visualize property locations and distributions
- Summarize and understand both categorical and numerical data

---

## 2. Loading and Inspecting Data
- Use pandas to load the cleaned CSV file:
```python
import pandas as pd
df = pd.read_csv("data/mexico-real-estate-clean.csv")
print(df.shape)      # Shows (rows, columns)
print(df.info())     # Shows column types and missing values
print(df.head())     # Shows first 5 rows
```
- Drop rows with missing location data:
```python
df.dropna(inplace=True)
```

---

## 3. Understanding Data Types
- **Numerical data**: area_m2, price_usd, price_mxn (numbers)
- **Categorical data**: property_type, state (names, types)
- **Location data**: lat, lon (coordinates)

---

## 4. Visualizing Property Locations on a Map
- Use plotly express to show where properties are located:
```python
import plotly.express as px
fig = px.scatter_map(
    df,
    lat="lat",
    lon="lon",
    center={"lat": 19.43, "lon": -99.13},
    width=600,
    height=600,
    hover_data=["price_usd"],
)
fig.update_layout(mapbox_style="open-street-map")
fig.show()
```
- Each dot is a property. Hover to see price. Map is centered on Mexico City.

---

## 5. Aggregating Categorical Data
- Count properties by state:
```python
print(df["state"].value_counts())  # Shows how many properties in each state
print(df["state"].nunique())      # Number of unique states
print(df["state"].unique())       # List of state names
```
- Find the top 10 states with most properties:
```python
print(df["state"].value_counts().head(10))
```

---

## 6. Summarizing Numerical Data
- Use descriptive statistics to understand area and price:
```python
print(df[["area_m2", "price_usd"]].describe())
```
- Key statistics:
    - **count**: number of properties
    - **mean**: average value
    - **std**: standard deviation (spread)
    - **min/max**: smallest/largest value
    - **percentiles**: 25%, 50% (median), 75%
- Insights:
    - Most homes are medium-sized and moderately priced
    - Some outliers (very large or expensive properties)
    - Negative prices are errors and should be removed

---

## 7. Data Cleaning: Removing Errors
- Remove properties with negative prices:
```python
df = df[df["price_usd"] > 0]
```
- Save cleaned data:
```python
df.to_csv("data/mexico-real-estate-clean.csv", index=False)
```
- Drop any remaining missing values:
```python
df.dropna(inplace=True)
```

---

## 8. Visualizing Numerical Data
- **Histogram**: shows distribution shape
```python
import matplotlib.pyplot as plt
plt.hist(df["area_m2"])
plt.xlabel("Area[sq_meter]")
plt.ylabel("frequency")
plt.title("Distribution of home size")
plt.show()
```
- **Boxplot**: shows median, quartiles, and outliers
```python
plt.boxplot(df["area_m2"], vert=False)
plt.xlabel("Area[sq meter]")
plt.title("Distribution of home sizes")
plt.show()
```
- Repeat for price:
```python
plt.hist(df["price_usd"])
plt.xlabel("Price[USD]")
plt.ylabel("frequency")
plt.title("Distribution of home price")
plt.show()
plt.boxplot(df["price_usd"], vert=False)
plt.xlabel("price[USD]")
plt.title("Distribution of home price")
plt.show()
```
- Insights:
    - Most homes are between 60 and 300 m²
    - Most prices are between 0 and 100,000 USD
    - Data is right-skewed (a few expensive properties raise the average)
    - Outliers are visible in both area and price
    - Histogram shows distribution shape, boxplot shows spread and outliers

---

## 9. Key Concepts Learned
- How to load and inspect real-world data
- How to clean and filter data for analysis
- How to distinguish between categorical and numerical data
- How to visualize property locations on a map
- How to summarize and visualize data distributions
- How to interpret results and spot trends/outliers
- How to use pandas, matplotlib, and plotly for EDA

---

## Conclusion
- You learned to explore, clean, and visualize real estate data for Mexico.
- You practiced EDA: inspecting, summarizing, and visualizing both categorical and numerical data.
- You discovered how to use maps, histograms, and boxplots to understand your data.
- These skills are essential for any data analysis project and help you turn raw data into useful insights!
