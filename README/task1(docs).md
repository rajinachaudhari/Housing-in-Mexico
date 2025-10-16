# Python Data Structures – Beginner-Friendly Notes

This guide explains every code and concept from your `task1(pypractice).py` file. It uses comments and simple explanations so you can understand each part at first sight.

---

## 1. Tabular Data Structures

### 1.1 Pandas DataFrame
- **Pandas** is a Python library for working with tables (like Excel).
- **DataFrame** is a table with rows and columns.
```python
import pandas as pd 
employee = pd.DataFrame({
    "name": ["rajina", "sajina", "aajina"],   # 'name', 'id', 'salary' are columns (features)
    "id": [1, 2, 3],
    "salary": [29, 30, 31]
})
print(employee)
```
**Output:**
```
     name  id  salary
0  rajina   1      29
1  sajina   2      30
2  aajina   3      31
```
- Each row is an employee; each column is a feature.

---

### 1.2 NumPy Array
- **NumPy** is a library for working with numbers and arrays.
- **Array** is a grid of values.
```python
import numpy as np
employee = np.array([
    [1, 2, 3],      # First row: IDs
    [29, 30, 31]    # Second row: Salaries
])
print(employee)
```
**Output:**
```
[[ 1  2  3]
 [29 30 31]]
```

---

## 2. Lists

### 2.1 Creating a List
- **List** is a collection of items (numbers, strings, etc.).
```python
house_0_list1 = [18, 4, "$122"]  # Area, rooms, price
print(house_0_list1)
```
**Output:** `[18, 4, '$122']`

---

### 2.2 Accessing List Items
- Use index to get items: `[0]` is first, `[-1]` is last.
```python
print(house_0_list1[-2])  # Second-to-last item
```
**Output:** `4`

---

### 2.3 List Functions
- `type()` tells you the type of variable.
- `len()` tells you how many items are in the list.
- `append()` adds an item to the end.
```python
print("house_0_list1 type:", type(house_0_list1))  # <class 'list'>
print("house_0_list1 length:", len(house_0_list1)) # 3
house_0_list1.append("its addition of new item using append")
print(house_0_list1)  # [18, 4, '$122', 'its addition of new item using append']
```

---

### 2.4 Calculating from List
- You can do math with numbers in a list.
```python
house_1_list2 = [19, 2, 123]  # Area, rooms, price
price_per_meter = house_1_list2[-1] / house_1_list2[0]  # price / area
print(price_per_meter)
```
**Output:** `6.473684210526316`

---

### 2.5 Appending Calculated Value
- Add calculated value to the list.
```python
house_0_list = [115910.26, 128, 4]
house_0_price_m2 = house_0_list[0] / house_0_list[1]
house_0_list.append(house_0_price_m2)
print(house_0_list)
```
**Output:** `[115910.26, 128, 4, 906.33484375]`

---

### 2.6 Nested List (List of Lists)
- A list inside a list is called a nested list.
```python
house = [
    [115910.26, 128, 4],
    [123456.78, 150, 3],
    [134567.89, 100, 2],
    [145678.90, 200, 5]
]
print(house)
```

---

### 2.7 Looping Through a List
- **Loop** lets you do something for each item.
```python
house_area = [18, 24, 34]
for x in house_area:
    print(x)
```
**Output:**  
```
18
24
34
```

---

### 2.8 Calculating for Each Nested List
- Use a loop to calculate for each house.
```python
for x in house:
    price_per_metre_sq = x[0] / x[1]
    x.append(price_per_metre_sq)
    print(x)
```
**Output:**  
Each house now has price per sq meter added.

---

### 2.9 Avoiding Duplicate Calculation
- Only add if not already calculated.
```python
house = [
    [115910.26, 128, 4],
    [123456.78, 150, 3],
    [134567.89, 100, 2],
    [145678.90, 200, 5]
]
for i in house:
    if len(i) == 3:  # Only add if there are 3 items
        price = i[0]
        area = i[1]
        price_per_metre_sq = price / area
        i.append(price_per_metre_sq)
    print(i)
```

---

## 3. Dictionaries

### 3.1 Creating a Dictionary
- **Dictionary** stores data as key-value pairs.
```python
house_dictionary = {
    'price': 115910.26,
    'area': 128.0,
    'rooms': 4.0
}
print(house_dictionary)
```
**Output:** `{'price': 115910.26, 'area': 128.0, 'rooms': 4.0}`

---

### 3.2 Accessing Dictionary Items
- Get value by key.
```python
print(house_dictionary["price"])  # 115910.26
print(house_dictionary.get("area"))  # 128.0
print(house_dictionary.keys())  # dict_keys(['price', 'area', 'rooms'])
print(house_dictionary.values())  # dict_values([115910.26, 128.0, 4.0])
```

---

### 3.3 Looping Through Dictionary
```python
for x in house_dictionary.keys():
    print(x)  # price, area, rooms

for x in house_dictionary.values():
    print(x)  # 115910.26, 128.0, 4.0

for x in house_dictionary.keys():
    print(x, "=", house_dictionary[x])  # price = 115910.26, etc.
```

---

### 3.4 Adding New Key-Value Pair
```python
house_dictionary["pice_per_sq_metre"] = house_dictionary["price"] / house_dictionary["area"]
print(house_dictionary)
```

---

### 3.5 List of Dictionaries (JSON Style)
- A list of dictionaries is like a table with rows.
```python
houses_dict_json = [
    {"price": 115910.26, "area": 128.0, "rooms": 4.0},
    {"price": 48718.17, "area": 210.0, "rooms": 3.0},
    {"price": 28977.56, "area": 58.0, "rooms": 2.0}
]
print(houses_dict_json)
```

---

### 3.6 Looping and Adding to Each Dictionary
```python
for x in houses_dict_json:
    x["price_per_sq_m2"] = x["price"] / x["area"]
    print(x)
```

---

### 3.7 Column-wise Dictionary
- Each key is a column, values are lists.
```python
house_dict_json_cloumnwise = {
    "price": [115910.26, 48718.17, 28977.56],
    "area": [128.0, 210.0, 58.0],
    "rooms": [4.0, 3.0, 2.0]
}
print(house_dict_json_cloumnwise)
```

---

### 3.8 Calculating Mean Price
```python
mean_price = sum(house_dict_json_cloumnwise["price"]) / len(house_dict_json_cloumnwise["price"])
print("mean price of houses:", mean_price)
```

---

### 3.9 Zipping Lists & Calculating Price per Sq Meter
- **zip()** combines two lists into pairs.
```python
area_m2 = [235, 130, 137]
price_cop = [400000000, 850000000, 457000000]
new_list = zip(area_m2, price_cop)
print(list(new_list))  # [(235, 400000000), (130, 850000000), (137, 457000000)]
```

---

### 3.10 Add Calculated Column to Dictionary
```python
price = house_dict_json_cloumnwise["price"]
area = house_dict_json_cloumnwise["area"]
price_area = list(zip(price, area))
price_per_sqm = []
for p, a in price_area:
    price_per_sq_m2 = p / a
    price_per_sqm.append(price_per_sq_m2)
house_dict_json_cloumnwise["price_per_sqm"] = price_per_sqm
print(house_dict_json_cloumnwise)
```

---

## 4. Pandas DataFrame
- **DataFrame** is a table with rows and columns.
```python
import pandas as pd
houses_df = pd.DataFrame(house_dict_json_cloumnwise)
print(houses_df)
print(type(houses_df))  # <class 'pandas.core.frame.DataFrame'>
print(len(houses_df))   # 3 (number of rows)
```
**Output:**
```
       price   area  rooms  price_per_sqm
0  115910.26  128.0    4.0     906.334844
1   48718.17  210.0    3.0     232.467476
2   28977.56   58.0    2.0     499.613103
```

---

## 5. Summary
- **List**: Ordered collection of items.
- **Dictionary**: Key-value pairs.
- **Nested List**: List inside a list.
- **Loop**: Repeat actions for each item.
- **Pandas DataFrame**: Table for easy data analysis.

**You learned how to organize, access, and calculate data in Python. These are the basics of data wrangling!**
