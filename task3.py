##goals of task3 is:
##1. conduct EDA
##2. visualize location data
##3. aggregate categorical data
##4. summarize numerical data
##5. libraries we need are pandas,matplotlib,plotly for eda and visualization


#step1:inspecting dataframe
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

df=pd.read_csv("data/mexico-real-estate-clean.csv")
print(df.shape)
print(df.info())
print(df.head())


#found NaN values in lat and lon so dropping it
df.dropna(inplace = True)
print(df.info())

#insights about df:
#lat,lon are location data but there datatype is float
#area_m2,price_usd,price_mxn are numerical data and its datatype is float
#property_type,state are categorical data(can be categorised by name,place,type like house or apartment) and its datatype is object
#sometimes categorical data is also called classes data

#commenting map for right now to visualize other output


#finding exactly where are the properties are located in mexico through lat and lon in real map

# # Use plotly express to create figure
fig = px.scatter_map(       #.px is allies of plotly express,scatter_map is function of plotly express to create scatter map 
    df,            #DataFrame is one of the arguments inside function that says where to get data from(here get data from our df)
    lat="lat",      #Latitude(lat) is in this particular column of our df(here latitude data in our df is in "lat" column)
    lon="lon",      #Longitude(lon) is in this particular column of our df(here longitude data in our df is in "lon" column)
                    #put the column name in form of string
    center={"lat": 19.43, "lon": -99.13},  # Map will be centered on Mexico City, the latitude and longitude of mexico city is near 19.43 degree, -99.13 degree
    width=600,  # Width and height of map which we see is set to number of pixels(600,600) pixels
    height=600,  
    hover_data=["price_usd"],  # Display price when hovering mouse over house/dot
)
# #all these function(argument1,argument2,argument3...) are passed in 1 variable fig to make easy to call

# # Add mapbox_style to figure layout
fig.update_layout(mapbox_style="open-street-map")  #update_layout()is used to set the map style, 
#                                                    #open-street-map is free map style provided by mapbox to look like google map

# # Show figure
fig.show()  # show() function is used to show the map in our default web browser
# #in 600/600 screen latitude is in x-axis and longitude is in y-axis
# #each dot in map is one property

#insights from map:
#most properties are located in and around mexico city,puebla,guadalajara,monterrey
#few properties are located in yucatan peninsula and baja california peninsula


#map only gives numerical data insights but not categorical data insights
#location of property can also be found through state column
#here we can categorize properties based on state column
#like how many properties are in each state,does property1 lies in guerrero?,etc


# Get value counts of "state" column
print(df["state"].head())    #displays first 5 state name only
print(df["state"].nunique())     #displays no. of unique state name (like 30 or 20 etc)
print(df["state"].unique())      #displays all the unique name of state in array form(actual name of state)
print(df["state"].value_counts())   #displays series of prevalent property in respective state in number
                            #Or counts no. of property in that particular state
#output: index                number of property in that index state
#        Distrito Federal                   303
#        Estado de México                   179
#        Yucatán                            171
#        Morelos                            160


#if we need 10 most prevalent state we need to set head(10) 
print(df["state"].value_counts().head(10))              #don't forget "s" in counts

#now we have already known location of property by numerical data(lat,lon) and categorical data(state)
#now we will summarize numerical data(area_m2,price_usd,price_mxn) through some statistical measures like mean,median,mode,std,min,max,25%,50%,75% etc

#for this we use descretive statistics.
#ex: what kind of property is there in mexico?
#    what is the average price of property in mexico?
#    what is the average area of property in mexico?

# Get descriptive statistics of numerical columns


# Describe "area_m2", "price_usd" columns
print(df[["area_m2","price_usd"]])     #double[[]] is used to access 2 column at once
print(df[["area_m2","price_usd"]].describe())    #describe() function is used to get the statistical measures of numerical data


# output:
#          area_m2      price_usd
# count   2768.000000    2768.000000 # count means total no. of property in our df
# mean     259.062861   57663.410430 # mean means average area and average price of property in mexico
# std      952.851443   73697.794163 # std means standard deviation of area and price of property in mexico
# min       60.000000 -237089.170000 # min means minimum area and minimum price of property in mexico
# 25%      102.000000    4986.150000 # 25% means 25 percentile of area and price of property in mexico
# 50%      158.000000   15251.350000 # 50% means 50 percentile of area and price of property in mexico
# 75%      220.000000   94971.080000 # 75% means 75 percentile of area and price of property in mexico
# max    16700.000000  326733.660000 # max means maximum area and maximum price of property in mexico

#insights from above output:
#1. total no. of property in our df is 2768
#2. average area of property in our df is 259.06 m2
#3. average price of property in our df is 57663.41 USD
#4. There’s high variation/difference ( standard deviation 952.85) — some properties are much larger or much smaller than average.
#5. There’s high variation/difference ( standard deviation 73697.79) — some properties are more expensive or much cheaper than average.
#6. minimum area of property is 60 m2
#7. minimum price of property is -237089.17 USD,which is invalid (a negative price). This may be a data error i should fix.
#8. 25% of properties have area less than 102 m2
#9. 50%(median) Half of the properties are below 158 m² and half are above.
#10. 75% of properties have area less than 220 m2
#11. 25% of properties have price less than 4986.15 USD
#12. 50%(median) Half of the properties are below 15251.35 USD and half are above.
#13. 75% of properties have price less than 94971.08 USD
#14. maximum area of property is 16700 m2 which could be a large land plot or outlier.
#15. maximum price of property is 326733.66 USD,which could be a luxury property or outlier.

#things to remember for this datum:
# There’s a negative price — that’s likely a data error or missing value indicator. You should remove or fix it.

# Large standard deviation means your data is highly spread out (some extreme outliers).

# The difference between mean and median also suggests right-skewed data (a few expensive properties raise the average).

##GOING UPWARD TO CLEAN -VE PRICE VALUE

df = df[df["price_usd"] > 0]   #filtering the df to remove -ve price value(in df dataframe inside price_usd column keep price whose value is greater than 0)
print(df["price_usd"].min())   #to check whether -ve price value is removed or not
print(df[["area_m2","price_usd"]].describe())  #to check the statistical measures of numerical data again after removing -ve price value

#saving cleaned data in df itself
df.to_csv("data/mexico-real-estate-clean.csv", index = False)  #index = False to avoid extra index column in our csv file 

df.dropna(inplace = True)  #to remove NaN values if any
print(df.info())


#now we will visualize numerical data(area_m2) through histogram(actual bar graph to see clearly the distribution of area_m2)
#Use Matplotlib to create histogram of "area_m2"

plt.hist(df["area_m2"])   #hist() function is used to create histogram,df["area_m2"] say make histogram of  particular column 
plt.xlabel("Area[sq_meter]")  # Add x-axis label
plt.ylabel("frequency")   # Add y-axis label
plt.title("Distribution of home size")  # Add title above graph
plt.show();   #show() function is used to show the histogram in our default output screen   
#to remove the array of numeric output use ; at end of histogram information


# Use Matplotlib to create boxplot of "area_m2"
plt.boxplot(df["area_m2"],vert= False)
# Add x-axis label
plt.xlabel("Area[sq meter]")
# Add title
plt.title("Distribution of home sizes")
plt.show();


# Use Matplotlib to create histogram of "price_usd"
plt.hist(df["price_usd"])
# Add x-axis label
plt.xlabel("Price[USD]")
# Add y-axis label
plt.ylabel("frequency")
# Add title
plt.title("Distribution of home price")
plt.show();

# Use Matplotlib to create boxplot of "price_usd"
plt.boxplot(df["price_usd"], vert = False)  #vert = False to make box plot horizontal
# Add x-label axis
plt.xlabel("price[USD]")
# Add y-label axis
#Add title 
plt.title("Distribution of home price");
plt.show();

#summary of histogram and boxplot:
#1. most properties have area between 60 m2 and 300 m2
#2. most properties have price between 0 USD and 100,000 USD    
#3. there are some outliers in area and price data
#4. median area is around 150 m2 and median price is around 15,000 USD
#5. both area and price data are right-skewed (a few large/expensive properties raise the average)
#6. boxplot shows more clearly the median,quartiles and outliers than histogram does
#7. histogram shows more clearly the distribution shape than boxplot does       
#8. both histogram and boxplot are useful to visualize numerical data distribution
#9. using both histogram and boxplot together gives a more complete picture of numerical data distribution  

###ALSO LOOK FOR GPT (EXPLAIN DATA FILTERING CHAT FOR DETAIL UNDERSTANDING)


#conclusion of task3:
#   - Loading and inspecting a cleaned dataset using pandas.
#   - Identifying and handling missing values (NaN) and fixing data errors (like negative prices).
#   - Understanding the difference between categorical data (like state, property_type) and numerical data (like area, price).
#   - Exploring location data using latitude and longitude, and visualizing property locations on a real map.
#   - Aggregating and summarizing categorical data (counting properties by state).
#   - Summarizing numerical data with descriptive statistics (mean, median, min, max, standard deviation, percentiles).
#   - Visualizing distributions of area and price using histograms and boxplots to spot trends and outliers.
#   - Interpreting results: most properties are in/around major cities, most homes are medium-sized and moderately priced, but there are some outliers.
#   - Learning that combining different visualizations (histogram + boxplot) gives a clearer picture of your data.




