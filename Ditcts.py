# Create a variable to hold the values of Nestle products
Nestle_dict = {"KitKat": 34456432, "Nescafe": 14106132,"Maggi": 9960312 ,"Nido ":44506003 }

# Create a variable to hold the values of Unilever products 
Unilever_dict = {"Lipton":23456000,"Breyers":1235891,"HellManns":17241412,"Marmite":11715324}

# Print each product sold by Unilever and the sales figures / numbers for that product.
for key , value in Unilever_dict .items():  # use for loop and detramin the key and value in dictionary 
    print(key , value ,"US Dollars")                     # print out the result for user 

# Print each product sold by Nestle and the sales figures / numbers for that product.
for key , value in Nestle_dict .items():  # use for loop and detramin the key and value in dictionary 
    print(key , value ,"US Dollars")                     # print out the result for user 

# Print which of the companies has more products that the other company.

product_dict = Unilever_dict .items() ^ Nestle_dict .items()
print (product_dict)

# Print the top selling product from Nestle with sales figures.
top_selling_product = max(Nestle_dict , key= Nestle_dict.get) # helps to get the max and have the vlaue of key from dictonary 
print("The top selling product from Nestle: ")   # print out The top selling product from Nestle
top_selling_sales_figures = max(Nestle_dict.values())
print(top_selling_product ,"with sales figures =",  top_selling_sales_figures , "US Dollars")
# Print the top selling product from Unilever with sales figures.
top_selling_product = max(Unilever_dict , key= Unilever_dict.get) # helps to get the max and have the vlaue of key from dictonary 
print("The top selling product from Nestle: ")   # print out The top selling product from Nestle
top_selling_sales_figures = max(Unilever_dict.values())
print(top_selling_product ,"with sales figures =",  top_selling_sales_figures , "US Dollars")
# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
Nestle_Countries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan" }
print("All the cities Nestle sell their products in :")
for i in Nestle_Countries:
    print(i)
Unilever_Countries = { "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates" }
print("All the cities Unilever sell their products in :")
for j in Unilever_Countries:
    print(j)

# Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
cities_in_both_Nestle_and_Unilver_sell_in = Nestle_Countries & Unilever_Countries
print("the cities that both Nestle & Unilver sell in common:" ,cities_in_both_Nestle_and_Unilver_sell_in)


# Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
