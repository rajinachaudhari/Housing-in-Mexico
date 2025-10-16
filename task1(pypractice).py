#tabular data structure in python
#creating table employee using pandas 
import pandas as pd 
employee=pd.DataFrame({
        "name":["rajina","sajina","aajina"],   #here employee is table name(observation)and name,id,salary are columns(feature) 
        "id":[1,2,3],
        "salary":[29,30,31]

})
print(employee)

#creating table employee using numpy
import numpy as np
employee=np.array([
        [1,2,3],
        [29,30,31]

])
print(employee)


#list in python
#creating list 
#first LHS of declaration is called variables and 1 variable can contain various datatypes.
#all this line is called list. now let's declare variable"house_0_list1"

house_0_list1=[18,4,"$122"]  
print(house_0_list1)

#accessing each item of list
#[0]/[-3]=first item and [2]/[-1]=last item
print(house_0_list1[-2])

#playing with function in list
print("house_0_list1 type:", type(house_0_list1))  #type function tells datatype of variable


print("house_0_list1 length:", len(house_0_list1))  #len function tells length of variable


print(house_0_list1.append("its addition of new item using append")) #append function adds new item at last of  existing list

#sum, avg can't be used in list as it does sum to all indexvalues from left to right inside list. dfiiferent datatypes can't be added.

#calculating price per metre sq for houses
#method 1:
#price_per_metre_sq=122/18
#print("price_per_metre_sq of house_0_list1 is:", price_per_metre_sq)
#method 2:
house_1_list2=[19,2,123]
price_per_meter = house_1_list2[-1]/house_1_list2[0]
print(price_per_meter)

#method 3: #WQU task1.1.1
# Declare variable `house_0_price_m2`
house_0_list = [115910.26, 128, 4]
house_0_price_m2 =house_0_list[0]/house_0_list[1]

# Print object type of `house_0_price_m2`
print("house_0_price_m2 type:", type(house_0_price_m2))

# Get output of `house_0_price_m2`
print(house_0_price_m2)

 #appending price_per_metre_sq to house_0_list
#print(house_0_list.append(house_0_price_m2))  #this will result to "None" as it modify list but print outdated list

house_0_list.append(house_0_price_m2) #this will modify list
print(house_0_list)  #this will print updated list

#list inside list is called nested list
#creating nested list
house = [
        [115910.26, 128, 4],
        [123456.78, 150, 3],
        [134567.89, 100, 2],
        [145678.90, 200, 5]
]
print(house)
#to calculate price_per_metre_sq of each house we use loop rather than going through 1 by 1

#loop in python 
house_area = [18,24,34]
for x in house_area:   #x is variable which takes each value of house_area one by one
    print(x)        #prints each value of house_area one by one
                        #print of for loop is indented i.e it is inside loop or from margin it must have tab space or 4 spaces
                        
#calculating price_per_metre_sq of each house using loop
for x in house:
        price_per_metre_sq = x[0]/x[1]  #x[0] is price and x[1] is area of each house
        x.append(price_per_metre_sq)    #appending price_per_metre_sq to each house
        print(x)                        #printing each house with price_per_metre_sq                        
    
#method 2: using indexind and unpacking
for i in house:
        price=i[0]
        area=i[1]
        price_per_metre_sq=price/area
        i.append(price_per_metre_sq) #it will duplicate calculation as next time loop reruns on appended houses x1
        print(i)
 
#method 3:
house = [
        [115910.26, 128, 4],
        [123456.78, 150, 3],
        [134567.89, 100, 2],
        [145678.90, 200, 5]
]   #here house has been redefined because it reades previous nested list and reappends price_per_metre_sq to it again and again
for i in house:
        if len(i) == 3:   #to avoid duplication of price_per_metre_sq calculation i.e if i=[price,area,room] which is only 3 length values then append if it turns to 4 length i.e  i=[price,area,room,price_per_metre_sq] then it will not append again
                price=i[0]
                area=i[1]
                price_per_metre_sq=price/area
                i.append(price_per_metre_sq)
        print(i)  #indentation of print matters, if it is inside loop it will print each house one by one, if outside loop it will print whole list at once
                
                
#day 2 practice 





# Declare variable `houses_nested_list`
houses_nested_list = [
    [115910.26, 128.0, 4.0],
    [48718.17, 210.0, 3.0],
    [28977.56, 58.0, 2.0],
    [36932.27, 79.0, 3.0],
    [83903.51, 111.0, 3.0],
]
# Create for loop to iterate through `houses_nested_list`

    # For each observation, append price / sq. meter
for x in houses_nested_list: 
        houses_price_per_m2= x[0]/x[1]
        x.append(houses_price_per_m2)
    # Get output of `houses_nested_list`
print(houses_nested_list)  #print is not indented to avoid repetation of lists. making it out of loop make print to vist 1 time only
# Print `houses_nested_list` type
print("houses_nested_list type:", type(houses_nested_list))

# Print `houses_nested_list` length
print("houses_nested_list length:", len(houses_nested_list))



#Lists are a good way to organize data, but one drawback is that we can only represent values.
# For example, someone looking at [115910.26, 128.0, 4] wouldn't know which values corresponded to price, area, etc.
# A better option might be a dictionary, where each value is associated with a key.

#dictionary in python
#creating dictionary



#day 3:
#creating a dictionary
house_dictionary={
        'price':115910.26,
        'area':128.0,
        'rooms':4.0
}
print(house_dictionary)

#accessing each item of dictionary
x=house_dictionary["price"]   #retriving value of price using key "price"
print(x)

#mehod 2: using get function
y=house_dictionary.get("area")  #retriving value of area using key "area"
print(y)

#access all key names of dictionary     
print(house_dictionary.keys())  #it will print all keys of dictionary


#access all values of dictionary
print(house_dictionary.values())  #it will print all values of dictionary

#conveting dictionary to list
print(list(house_dictionary.keys())) #it will convert dictionary's key to list of keys

print(list(house_dictionary.values())) #it will convert dictionary's  key's values to list of values

#using loop in dictionary
for x in house_dictionary.keys():      #please don't forget "s" in keys and value's' not value
        print(x)      #it will print all keys of dictionary one by one
        
#retriving all values from dictionary using loop
for x in house_dictionary.values():
        print(x)      #it will print all values of dictionary one by one
        
        
#retriving key-value pair from dictionary using loop
for x in house_dictionary.keys():   #house_dictionary.keys() gives  a view of all the keys in the dictionary
                                #for x in house_dictionary.keys() means x= price in first loop then area in second loop then rooms in third loop
        print(x,"=",house_dictionary[x])  #x= all key names whereas house_dictionary[x]= all values of respective keys
                                        #x,"=",house_dictionary[x] means in first loop it will print price=115910.26 and so on

#adding new key-value pair to dictionary
house_dictionary["pice_per_sq_metre"]=house_dictionary["price"] / house_dictionary["area"]
print(house_dictionary)      # this will print updated dictionary
#as list need append but in dictionary we can directly add new key-value pair

#presenting dictionary as json way
 #declaring variable to put multiple  dictionary in a list a.k.a json way
 
houses_dict_json = [
         {
                 "price":115910.26,
                 "area":128.0,
                "rooms":4.0
         },
         {
                 "price":48718.17,
                 "area":210.0,
                 "rooms":3.0
         },
         {
                 "price":28977.56,
                 "area":58.0,
                 "rooms":2.0
        }
 ]
print("houses_dict_json:",type( houses_dict_json)) 
print("houses_dict_json:",len(houses_dict_json))#it will print list of dictionaries
print(houses_dict_json) #it will print whole list of dictionaries  


#creating loop in list of dictionaries
for x in houses_dict_json:
        print(x) #it will print each dictionary one by one

#adding new key-value pair to each dictionary using loop
for x in houses_dict_json:
        x["price_per_sq_m2"]=x["price"]/x["area"] #it will add new key-value pair to each dictionary
        print(x) #it will print each dictionary one by one with new key-value pair
   
   # day 5
   
        
#adding new key-value pair to each dictionary using loop but calculate through column not row
#method1:
for i in range(len(houses_dict_json)):  #range(len(houses_dict_json)) means range(3) means 0,1,2
        price=houses_dict_json[i]["price"]  #it will take price of each dictionary one by one
        area=houses_dict_json[i]["area"]    #it will take area of each dictionary one by one
        houses_dict_json[i]["price_per_sq_m2"]=price/area  #it will add new key-value pair to each dictionary
        print(houses_dict_json[i])  #it will print each dictionary one by one with new key-value pair 

#method 2:

house_price=[]
for x in houses_dict_json:
       house_price.append(x["price"])
print (house_price)

mean_price=sum(house_price)/len(house_price)
print("mean_price:",mean_price)



#putting all values of a same key a.k.a column in a list
house_dict_json_cloumnwise={
        
                "price":[115910.26,48718.17,28977.56],
                "area":[128.0,210.0,58.0],      
                "rooms":[4.0,3.0,2.0]
                
        
}
print(house_dict_json_cloumnwise)
print("type of house_dict_json_cloumnwise:",type(house_dict_json_cloumnwise))
print("length of house_dict_json_cloumnwise:",len(house_dict_json_cloumnwise))


#do columnwise calculation in above cloumnwise dictionary
#calculating mean price of houses

mean_price=sum(house_dict_json_cloumnwise["price"])/ len(house_dict_json_cloumnwise["price"])
print("mean price of houses:",mean_price)


#calculating rowise calculation in above cloumnwise dictionary

#let's learn about tuple(item1,item2,---) and zippinf of list for this concept
area_m2 =[235,130,137]  #list1
price_cop = [400000000,850000000,457000000]  #list 2
new_list = zip(area_m2,price_cop)  #output: [(235, 400000000), (130, 850000000), (137, 457000000)] is it list of tuples(area,price) which is formed after zipping both list
print(list(new_list))  #it will print list of tuples of area and price

#calculating price_per_sq_m2 of each house
price=house_dict_json_cloumnwise["price"]
area=house_dict_json_cloumnwise["area"]
price_area=list(zip(price,area))
print(price_area)   #it will print list of tuples of price and area
for p, a in price_area:
        print("price:",p)
        print("area:",a)

#calculating price_per_sq_m2 of each house
price_per_sqm=[]
for p,a in price_area:   # p=price and a=area of each house
        price_per_sq_m2=p/a
        print(price_per_sq_m2)
        price_per_sqm.append(price_per_sq_m2) #appending price_per_sq_m2 to list price_per_sqm
print(price_per_sqm)  #it will print list of price_per_sq_m2 of each house
house_dict_json_cloumnwise["price_per_sqm"]=price_per_sqm #adding new key-value pair to dictionary
print(house_dict_json_cloumnwise)

#these all datastructure can be used using pandas dataframe also
#pandas is extension of python to do data analysis and manipulation
#dataframe is 2D data structure representation
#instead of accessinf neated list & dictionary we can use dataframe to represent data in tabular form and access them easily
#but the base knowledge of list and dictionary is must to understand dataframe


#representing house_dict_json_cloumnwise in dataframe
import pandas as pd
houses_df=pd.DataFrame(house_dict_json_cloumnwise) #it will convert dictionary to dataframe
print(houses_df)
#output
 #     price   area  rooms  price_per_sqm
#0  115910.26  128.0    4.0     905.548906
#1   48718.17  210.0    3.0     231.991286
#2   28977.56   58.0    2.0     499.613103
#this tabular data structure is called dataframe

print(type(houses_df))  #it will print datatype of houses_df which is dataframe
print(len(houses_df))   #it will print length of dataframe which is 3 i.e number of rows


#Concusion:
#       we have learnt about list,dictionaries,nested them access rowwise and columnwise values,
#       inserted data into rowise&columnwise form and done calculation and append.
#       This is basics of data updating and structring which is part of data wrangling.
#       Data wrangling can be easily done through pandas library and making simple data into dataframe
#       now in task 2 we will dig deeper into data wrangling using pandas library.
#       task1(tabular and  tidy data is ended here)