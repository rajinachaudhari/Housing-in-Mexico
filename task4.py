#Goals: Research about What Influences House Prices in Mexico?

#Research Question 1 : Which state has the most expensive real estate market?
#for this we import data from dataframe and we find mean price of property in each state

# Import "data/mexico-real-estate-clean.csv"
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/mexico-real-estate-clean.csv")

# Print object type, shape, and head
print("df type:", type(df))
print("df shape:", df.shape)
df.head()

# Declare variable `mean_price_by_state`

#mean_price_by_state = df.groupby("state")["price_usd"].mean() #grouping the df by state column and price_usd column using groupby()[] function
                                                #then finding mean of price_usd column for each state using .mean() function
#this will sort by latter A to Z
#mean_price_by_state = df.groupby("state")["price_usd"].mean().sort_values()
#this will sort by value low to high or ascending order

mean_price_by_state = df.groupby("state")["price_usd"].mean().sort_values(ascending=False)
#this will sort by value high to low or descending order
# Print object type, shape, and head
print("mean_price_by_state type:", type(mean_price_by_state))
print("mean_price_by_state shape:", mean_price_by_state.shape)
print(mean_price_by_state)

#output:
# state
#Nayarit###                            118421.050000
#Jalisco###                             84973.267500
#......                                 .....
# Sinaloa###                              2448.780000
# Tlaxcala###                             2162.920000
#     this result says that Nayarit has the most expensive state in mexico with average price of 118421.05 USD
#     and Tlaxcala is the least expensive state in mexico with average price of 2162.92 USD

#visualizing the result of expensive and cheap property state using bar graph


#commenting rn to avoid 

# Create bar chart from `mean_price_by_state` using pandas
# mean_price_by_state.plot()
# plt.show();     #plt.show() only works if matplotlib is imported as plt 
                #only using pandas also display graph using .plot() function but it only works in jypyter notebook not in pycharm or any other ide
                #so to display graph in pycharm or any other ide we have to use matplotlib library
                
#this will just display line graph which isn't easy to understand
#to display bar graph we have to use kind parameter in .plot() function


#commenting rignt now  the below code to avoid multiple plots

# mean_price_by_state.plot(
#     kind="bar",
#     xlabel="State",
#     ylabel="Mean Price (USD)",
#     title="Mean house Price by State"
# )
# plt.show();

#this will display bar graph with state names on x-axis and mean price on y-axis
 
#in reality Mexico City's GDP is significantly larger than Nayarit's. 
# In 2022, Mexico City's GDP was approximately \(212.5\) billion USD, 
# while the entire GDP of the state of Nayarit was only a fraction of that.
#but why Nayarit has the most expensive property?
#maybe the property in Nayarit is more luxurious and spacious than in Mexico City

#so let's calculate price per square meter for each state

# Create "price_per_m2" column
df["price_per_m2"] = df["price_usd"] / df["area_m2"]  #price per meter square is calculated
# Print object type, shape, and head
print("df type:", type(df))
print("df shape:", df.shape)
print(df.head())

#let's see if our price per m2 is according to state or not 
#above method of plotting and finding mean is long 
#so we use chaining method to do it in one line
#for this we use () to enclose the code

# Group `df` by "state", create bar chart of "price_per_m2"
(
    df
    .groupby("state")
    ["price_per_m2"].mean()
    .sort_values(ascending = False)
    .plot(
    kind = "bar",
    xlabel="State",
    ylabel="Mean price per M2[USD]",
    title = "Mean house price per sq m2"
)
);
plt.tight_layout()  # adjusts spacing of graph automatically according to screen size
plt.show() #plt.show() must be used to display any graph in other ide except jupyter notebook
#its like print() function for graph

#insights from graph:
#since it is dummy dataset so result is not accurate as per real world condition(but in general it has to match the pattern of real world)

#in real  world:
#Mexico City (Ciudad de México / Distrito Federal),Estado de México,Jalisco have higher GDP so it may have higher price per m2
#Veracruz, Guanajuato GDP is mid so it may have midrange price per m2
#Chiapas, Oaxaca, Guerrero have lower GDP so it may have lower price per m2
#Tlaxcala is one of the poorer states in Mexico by GDP per capita.


#in bar graph:
#price per m2 is higher at distrito federal and goes down to tlaxcala as in real world scenario
#but nayarit is tourist place so it may have higher price per m2 than other states
#in this way we compare our visualization with real world scenario to check if it is correct or not



#research question 1 answer: the state with the most expensive property is Nayarit.
#                          but this answer is based on location of property only.


                       
# Research Question 2:
# Is there a relationship between home size and price?(regardless of location)

#for this we use scatter plot between area_m2(in x-axis) and price_usd(in y-axis)
#home price is the function of home size

# Create scatter plot of "price_usd" vs "area_m2"
plt.scatter(x=df["area_m2"],y=df["price_usd"]) #x-axis is area_m2 and y-axis is price_usd, scatter() function is used to create scatter plot
plt.tight_layout()  # adjusts spacing of graph automatically according to screen size
plt.xlabel("Area[sq meters]")   # Add x-axis label
plt.ylabel("Price[USD]")# Add y-axis label
plt.title("Price VS Area");# Add title (y-axis vs x-axis always)
plt.show() 

#result of jyputer notebook:
#we can see lot of plot are concentrated as :
#                  if area increase price also increase
#                  some are in straight line
#                  some are outliers

#result of vs code df:
#we can see lot of plot are concentrated as :
#Most dots are concentrated near the left side (small area below 1000 m²).
# this says(Most listings are for small to medium-sized homes (not large estates or lands)).
#Even though most properties are small in area, their prices range widely.
#    some are cheap, some are very expensive even for small areas.
# insights: Price depends on more than just size —
#              things like location, neighborhood, amenities, or building type heavily influence price.

#now we find correlation between area_m2 and price_usd

# Calculate correlation of "price_usd" and "area_m2"
p_correlation = df["area_m2"].corr(df["price_usd"])

# Print correlation coefficient
print("Correlation of 'area_m2' and 'price_usd' (all Mexico):", p_correlation)


#output:Correlation of 'area_m2' and 'price_usd' (all Mexico): 0.010309224126470446
#this result says that there is very weak relation between area_m2 and price_usd
#because correlation value is ~0 which means no correlation
#Note: Correlation finds only linear relationships between two variables.


#let's see if ths correlation is different in different states
#creating a subset datafram for morelos state and mexico city state respectively

#for morelos state
# Declare variable `df_morelos` by subsetting `df`
df_morelos =df[df["state"]=="Morelos"]

# Print object type, shape, and head
print("df_morelos type:", type(df_morelos))
print("df_morelos shape:", df_morelos.shape)
df_morelos.head()

# Create scatter plot of "price_usd" vs "area_m2" in Morelos
plt.scatter(x=df_morelos["area_m2"] , y=df_morelos["price_usd"])

# Add x-axis label
plt.xlabel("Area[sq meter]")
# Add y-axis label
plt.ylabel("Price[USD]")
# Add title
plt.title("Morelos: Price vs. Area")
plt.show()

# Calculate correlation of "price_usd" and "area_m2" in `df_morelos`
p_correlation = df_morelos["area_m2"].corr(df_morelos["price_usd"])

# Print correlation coefficient
print("Correlation of 'area_m2' and 'price_usd' (Morelos):", p_correlation)


#output:Correlation of 'area_m2' and 'price_usd' (Morelos): 0.190288563279854
#this result says that there is weak relation between area_m2 and price_usd in morelos state

#for mexico city state
# Declare variable `df_mexico_city` by subsetting `df`
df_mexico_city = df[df["state"] =="Distrito Federal"]

# Print object type and shape
print("df_mexico_city type:", type(df_mexico_city))
print("df_mexico_city shape:", df_mexico_city.shape)

# Create scatter plot of "price_usd" vs "area_m2" in Morelos
plt.scatter(x=df_mexico_city["area_m2"] , y=df_mexico_city["price_usd"])

# Add x-axis label
plt.xlabel("Area[sq meter]")
# Add y-axis label
plt.ylabel("Price[USD]")
# Add title
plt.title("Mexico City: Price vs. Area")
plt.show()
# Calculate correlation of "price_usd" and "area_m2" in `df_morelos`
p_correlation = df_mexico_city["area_m2"].corr(df_mexico_city["price_usd"])

# Print correlation coefficient
print("Correlation of 'area_m2' and 'price_usd' (Mexico city):", p_correlation)

#output:Correlation of 'area_m2' and 'price_usd' (Mexico city): 0.046785739567096
#this result says that there is very weak relation between area_m2 and price_usd in mexico city state

# Conclusion:
# In task4, you explored what influences house prices in Mexico using real data and visualizations.
# You learned how to:
#   - Compare average house prices across states and found Nayarit has the highest mean price, while Tlaxcala has the lowest.
#   - Calculate and visualize the average price per square meter for each state, revealing that price per m2 is highest in Mexico City and tourist areas.
#   - Use bar charts to easily compare prices between states.
#   - Investigate the relationship between home size (area) and price using scatter plots and correlation.
#   - Discover that, overall, there is very little correlation between area and price, meaning bigger homes are not always more expensive.
#   - Check if this relationship changes in specific states (Morelos and Mexico City), and found only weak or very weak correlation there too.
#   - Understand that house prices depend on many factors, not just size—location, amenities, and local demand matter a lot.
# These skills help you answer real research questions with data, and show how to use pandas and matplotlib for deeper analysis and visualization.
