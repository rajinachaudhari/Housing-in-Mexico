# Task 4: What Influences House Prices in Mexico? – Beginner-Friendly Documentation

This documentation explains every step and concept from your `task4.py` file, with comments and simple explanations for beginners.

---

## 1. Project Goals
- Research what factors influence house prices in Mexico using real data and visualizations.
- Answer two main research questions:
    1. Which state has the most expensive real estate market?
    2. Is there a relationship between home size and price?

---

## 2. Loading and Inspecting Data
- Use pandas to load the cleaned CSV file:
```python
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/mexico-real-estate-clean.csv")
print(type(df))      # Shows DataFrame type
print(df.shape)      # Shows (rows, columns)
print(df.head())     # Shows first 5 rows
```

---

## 3. Research Question 1: Most Expensive State
- Calculate the mean price of properties in each state:
```python
mean_price_by_state = df.groupby("state")["price_usd"].mean().sort_values(ascending=False)
print(mean_price_by_state)
```
- **groupby()** groups data by state, then calculates the average price for each state.
- **sort_values(ascending=False)** sorts states from most to least expensive.
- **Result:** Nayarit has the highest average price, Tlaxcala the lowest.

- Visualize the result with a bar chart:
```python
mean_price_by_state.plot(kind="bar", xlabel="State", ylabel="Mean Price (USD)", title="Mean house Price by State")
plt.show()
```
- Bar chart makes it easy to compare prices between states.

---

## 4. Price per Square Meter by State
- Calculate price per square meter for each property:
```python
df["price_per_m2"] = df["price_usd"] / df["area_m2"]
```
- Group by state and plot average price per m2:
```python
(
    df.groupby("state")["price_per_m2"].mean().sort_values(ascending=False)
    .plot(kind="bar", xlabel="State", ylabel="Mean price per M2[USD]", title="Mean house price per sq m2")
)
plt.tight_layout()
plt.show()
```
- **Insight:** Price per m2 is highest in Mexico City and tourist areas.

---

## 5. Research Question 2: Relationship Between Home Size and Price
- Use a scatter plot to visualize the relationship:
```python
plt.scatter(x=df["area_m2"], y=df["price_usd"])
plt.xlabel("Area[sq meters]")
plt.ylabel("Price[USD]")
plt.title("Price VS Area")
plt.tight_layout()
plt.show()
```
- **Insight:** Most homes are small to medium-sized, but prices vary widely. Bigger homes are not always more expensive.

- Calculate correlation between area and price:
```python
p_correlation = df["area_m2"].corr(df["price_usd"])
print("Correlation of 'area_m2' and 'price_usd' (all Mexico):", p_correlation)
```
- **Result:** Correlation is close to zero, meaning very weak relationship.

---

## 6. Checking Relationship in Specific States
- Subset data for Morelos and Mexico City:
```python
df_morelos = df[df["state"] == "Morelos"]
df_mexico_city = df[df["state"] == "Distrito Federal"]
```
- Create scatter plots and calculate correlation for each:
```python
plt.scatter(x=df_morelos["area_m2"], y=df_morelos["price_usd"])
plt.title("Morelos: Price vs. Area")
plt.show()
p_correlation = df_morelos["area_m2"].corr(df_morelos["price_usd"])
print("Correlation of 'area_m2' and 'price_usd' (Morelos):", p_correlation)

plt.scatter(x=df_mexico_city["area_m2"], y=df_mexico_city["price_usd"])
plt.title("Mexico City: Price vs. Area")
plt.show()
p_correlation = df_mexico_city["area_m2"].corr(df_mexico_city["price_usd"])
print("Correlation of 'area_m2' and 'price_usd' (Mexico city):", p_correlation)
```
- **Result:** Only weak or very weak correlation in these states too.

---

## 7. Key Concepts Learned
- How to group and summarize data by categories (state).
- How to calculate and visualize averages and price per square meter.
- How to use bar charts and scatter plots for comparison and relationships.
- How to calculate correlation to measure strength of relationships.
- How to subset data for deeper analysis of specific groups.
- How to interpret results: house prices depend on many factors, not just size.

---

## Conclusion
- You learned to answer real research questions using data and visualizations.
- You compared house prices across states and found which are most expensive.
- You investigated the relationship between home size and price, and discovered it is weak overall.
- You practiced using pandas and matplotlib for deeper analysis and visualization.
- These skills help you turn raw data into insights and make informed decisions!
