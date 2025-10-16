#this project1 and assessment1 is about descriptive data science 


import pandas as pd
# Load CSV files into DataFrames
df1 = pd.read_csv("data/mexico_real_estate_messy_v1.csv") #pd.read_csv("filepath") loads a csv file into a dataframe
df2 = pd.read_csv("data/mexico_real_estate_messy_v2.csv")
df3 = pd.read_csv("data/mexico_real_estate_messy_v3.csv")
#if error don't occur then the files are loaded correctly

# Print object type and shape for DataFrames
print("df1 type:", type(df1))     #type() function returns the type of the object passed to it
print("df1 shape:", df1.shape)     #shape attribute returns/displays a tuple representing the dimensionality of the DataFrame i.e (number of rows, number of columns)
print()  # Print a blank line for better readability i.e. spacing between outputs
print("df2 type:", type(df2))
print("df2 shape:", df2.shape)
print()
print("df3 type:", type(df3))
print("df3 shape:", df3.shape)

#inspecting the dataframes
print(df1.shape) #prints no.s of rows and columns
print(df1.head()) #prints first 5 rows
print(df1.info()) #prints summary info about the dataframe like notnull,datatypes,memory usage
print(df1.describe()) #prints statistical summary of numerical columns

#dropping all null(NaN) values 
df1.dropna(inplace=True) #dropna() removes rows with any null values, inplace=True modifies the original dataframe
df1.info() #checking if null values are removed



# before dropping nan vlues (RangeIndex: 1910 entries, 0 to 1909) and below table says:
#out of 1910 entries,1819 non-null values in property_type column,1818 non-null values in state column and so on
#i.e 91 rows had at least one null value 
#   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   property_type  1819 non-null   object 
#  1   state          1818 non-null   object 
#  2   lat            1818 non-null   float64
#  3   lon            1813 non-null   float64
#  4   area_m2        1817 non-null   object 
#  5   price_usd      1816 non-null   object 

# after dropping nan values (RangeIndex: 1819 entries, 0 to 1818) and below table says:
#out of 1819 entries,1819 non-null values in property_type column,1819 non-null values in state column and so on
#i.e all rows with at least one null value are removed!!!!!


#changing datatype of price_usd and area_m2 columns from object to float
print(df1["price_usd"].head()) #checking first 5 values of price_usd column

#if the price contains $ and , we need to remove them before converting to float
#for this we write code as :
#df1["price_usd"].str.replace("$","",regex=False).str.replace(",","",regex=False).head()
#str.replace("$","",regex=False) replaces $ with empty string and regex=False treats $ as a literal character
#.head() displays first 5 values of the modified series


#this will remove $ and , from all values in price_usd column but it still is object not float
# to convert it to float we use astype(float) function


     #these didn't work
# df1["price_usd"]=df1["price_usd"].str.replace("$","",regex=False).str.replace(",","",regex=False).astype(float)
# print(df1["price_usd"].head()) #checking first 5 values of price_usd column after conversion to float
# print(df1.info()) #checking if datatype of price_usd column is changed to float


#    #trying this 
# df1["price_usd"] = df1["price_usd"].astype(float)

# print(df1["price_usd"].head())
# print(df1.info())

#still not working:

invalid_prices = df1[~df1["price_usd"].str.replace(".", "", 1).str.isnumeric()]
print(invalid_prices)
#this code identifies and prints rows where the price_usd column contains invalid values that cannot be converted to numeric format.
#~ negates the condition, so it selects rows where the modified price_usd is not numeric.
#looks like we have ??? sign instead of numbers in price_usd column
# 903          House                     San Luis Potos�  ...       250.0         ???
# 908          House                             Morelos  ...       261.0         ???

#first we convert ??? to NaN values
df1["price_usd"]=df1["price_usd"].replace("???", pd.NA).str.replace("$","",regex=False).str.replace(",","",regex=False)
print(df1["price_usd"].isna().any())
#this code checks if there are any NaN values in the price_usd column after the replacement
#isna() returns a boolean Series indicating where values are NaN, and any() checks if any of those values are True (i.e., if there is at least one NaN value in the column).
#it returned True meaning there are NaN values in price_usd column
df1["price_usd"].info()   #out of total(1411) 1398 is not null values in price_usd column


#again dropping all null(NaN) values

df1.dropna(inplace=True) #dropna() removes rows with any null values, inplace=True modifies the original dataframe
df1.info() #checking if null values are removed 

#now converting price_usd column to float
df1["price_usd"] = df1["price_usd"].astype(float)
print(df1["price_usd"].head()) #checking first 5 values of price_usd column after conversion to float
print(df1.info()) #checking if datatype of price_usd column is changed to float
#it worked!!!!!!! price_usd column is now float64 datatype


#similarly converting area_m2 column to float
print(df1["area_m2"].head()) #checking first 5 values of area_m2 column

invalid_areas = df1[~df1["area_m2"].str.replace(",", "", 1).str.isnumeric()]
print(invalid_areas)
# #looks like area_m2 column has commas(,) in between the numbers 
# #so first we remove commas(,) and then convert it to float

df1["area_m2"]=df1["area_m2"].replace("2024-12-01", pd.NA)
print(df1["price_usd"].isna().any())
df1.dropna(inplace=True)
# df1["area_m2"]=df1["area_m2"].str.replace(",","",regex=False)
df1["area_m2"] = df1["area_m2"].astype(float)
df1.info()

#cleaning df2

print(df2.shape)
print(df2.head())
print(df2.info())

#dropping NaN values
df2.dropna(inplace=True)
df2.info()

#identifying invalid prices
invalid_prices = df2[~df2["price_mxn"].str.replace(".", "", 1).str.isnumeric()]
print(invalid_prices)
#looks like we have ??? signs in 42 rows and - before price



     #this code commented below didn't work
# #replacing invalid symbols to NaN values
# df2["price_mxn"]=(df2["price_mxn"].replace("???", pd.NA)
#                   .str.replace("-","",regex=False)
#                   .str.replace(",","",regex=False)
#                   .str.replace("$","",regex=False)
#                   )

# #checking if NaN values are present in price_mxn column 
# print(df1["price_usd"].isna().any())
# #output: False there in no NaN values so again check invalid symbols


#new mwethod:
df2["price_mxn"] = (
    df2["price_mxn"]
    .astype(str)                        # Ensure the column is treated as strings
    .str.replace("-", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.replace("$", "", regex=False)
)

# Now replace ??? AFTER string operations
df2["price_mxn"].replace("???", pd.NA, inplace=True)   # Replace "???" with NaN but we still don't know whether NaN exists or it's treated as string or actuallu null values

# Finally converting invalid values into NaN (not string/text NaN)
df2["price_mxn"] = pd.to_numeric(df2["price_mxn"], errors="coerce")
#pd.to_numeric safely converts strings to numbers
# errors="coerce" replaces anything that isn’t a valid number with NaN (null values).
#benefit: we don't have to use astype(float) which gives error if invalid values are present
#        it automatically converts valid values to float and invalid to NaN
#        we don't have to check invalid values manually
#       it simplifies the code and makes it more robust and ensures correctness if any error values are missed while checking manually

#checking if NaN values are present in price_mxn column
print(df2["price_mxn"].isna().any())  
#output: True there are NaN values so we drop them

#dropping NaN values
df2.dropna(inplace=True)
df2.info() 
#it worked!!!!!!! price_mxn column is now float64 datatype with no NaN values

#transforming 
#now converting mexican peso to usd(exchange rate 1 USD = 19 Pesos)
df2["price_usd"] = (df2["price_mxn"] / 19).round(2)  #rounding off to 2 decimal places
# 19 peso=1 usd
#1peso=1/19 usd
#x peso=(1/19)*x usd

print(df2.head()) 

df2.drop(columns=["price_mxn"], inplace=True)
print(df2.head())

#converting area_m2 column into float
print(df2["area_m2"].head())

#checking invalid areas
invalid_areas = df2[~df2["area_m2"].str.replace(",", "", 1).str.isnumeric()]
print(invalid_areas)
#it don't have any invalid values but upon using astype (float) it gives error saying there is date value
#so we replace that date value with NaN and then drop NaN values

df2["area_m2"]=df2["area_m2"].replace("2024-12-01", pd.NA)

#check if there are any NaN values
print(df2["area_m2"].isna().any())


#dropping null values
df2.dropna(inplace = True)
print(df2.info())

 #changing datatype of area_m2 column to float
df2["area_m2"] = df2["area_m2"].astype(float)
print(df2["area_m2"].head())

#cleaning df3
print(df3.shape)
print(df3.head())
print(df3.info())


#dropping lat , lon to make dataset like of worldquant
df3.drop(columns=["lat","lon"],inplace =True)
print(df3.head())

# Drop null values from df3
df3.dropna(inplace = True)
df3.info()

# # Create "lat" and "lon" columns for df3 in seperate columns
df3["lat-lon"].str.split(",",expand = True).head() 
#.split: seperates comma seperated values (which is treated as string) into list
#ex: (1939493,-99274923) becomes [1939493 , -99274923]
# and expand make different column of splited values

df3[["lat", "lon"]] = df3["lat-lon"].str.split(",",expand = True).head() # double[[]] is used to make 2 variable

# #  Print object type, shape, and head
print("df3 type:", type(df3))
print("df3 shape:", df3.shape)
print(df3.head())


#splitting place_with_parent_names based on | vertical slash


print(df3["place_with_parent_names"].str.split("|",expand = True))
# we need only column 2 as it is the name of the state

print(df3["place_with_parent_names"].str.split("|",expand = True)[2].head())


#Creating "state" column for df3 using the 2nd column of the split operation
df3["state"] = df3["place_with_parent_names"].str.split("|",expand = True)[2]
print(df3["state"].head())

#Droping "place_with_parent_names" and "lat-lon" from df3
df3.drop(columns=["place_with_parent_names","lat-lon"],inplace= True) 


#Print object type, shape, and head
print("df3 type:", type(df3))
print("df3 shape:", df3.shape)
print(df3.head())
print(df3.shape)

#result:
#   property_type  area_m2  price_usd          lat           lon             state
# 0         house    150.0   67965.56    19.560181    -99.233528  Estado de México
# 1         house    186.0   63223.78   25.6884355  -100.1988071        Nuevo León
# 2     apartment     82.0   84298.37    16.767704    -99.764383          Guerrero
# 3     apartment    150.0   94308.80    16.829782    -99.911012          Guerrero
# 4         house    205.0  105191.37  21.05258302  -89.53863859           Yucatán

# Concatenate df1, df2, and df3 into single DataFrame df
df =pd.concat([df1,df2,df3])    
#by default axis=0 i.e concatenate vertically
# if horizontal concatenation is needed then axis=1
#i.e df=pd.concat([df1,df2,df3],axis=1)
#horizontal concatenation means [df1][df2][df3] side by side which will increase no. of columns
#and also duplicate column names will be there which is not good
#vertical concatenation means stacking one below the other which will increase no. of rows but no. of columns will remain same
#also no duplicate column names will be there which is good

# Print object type, shape, and head
print("df type:", type(df))
print("df shape:", df.shape)
df.head()

# Save df to CSV file 
df.to_csv("data/mexico-real-estate-clean.csv",index=False)
#to_csv("filepath",index=False) saves the dataframe to a csv file without the index column
# if index=True then it will save the index column also which is not needed here
#it will create a new file mexico-real-estate-clean.csv((clean dataset) in data folder which we will use to perform analysis



# Conclusion:
# In this task, we practiced advanced data wrangling using the pandas library.
# We learned how to:
#   - Load messy CSV files into DataFrames.
#   - Inspect, clean, and transform data by handling missing values, fixing invalid entries, and converting data types.
#   - Use string operations to clean columns and safely convert them to numeric types.
#   - Extract and create new columns from complex string fields.
#   - Concatenate multiple cleaned DataFrames into a single tidy dataset.
#   - Save the final cleaned data for further analysis.
# These steps are essential for preparing real-world data for analysis and modeling.
# Mastering these techniques makes you confident in handling messy datasets and turning them into useful, structured information.