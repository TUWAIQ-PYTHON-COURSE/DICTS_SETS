
#Create a variable to hold the values of Nestle products (use a dicitionary)

nestleDict = {
    "KitKat" : 34456432  , 
    "Nescafe" : 14106132 ,
    "Maggi" : 9960312  ,
    "Nido" : 44506003 
}

#Create a variable to hold the values of Unilever products (Use a dictionary)

unileverDict ={
    "Lipton" : 23456000  ,
    "Breyers" : 1235891  ,
    "HellManns" : 17241412 , 
    "Marmite" :  11715324 
}

#Print each product sold by Unilever and the sales figures / numbers for that product.

print("the products sold by Unilever and the sales figures: ")
for key , value in unileverDict.items():
    print(key , value )

#Print each product sold by Nestle and the sales figures / numbers for that product.

print("the products sold by Nestle and the sales figures: ")
for key , value in nestleDict.items():
    print(key , value)

#Print which of the companies has more products that the other company.

#Print the top selling product from Nestle with sales figures.

print("The top selling product from Nestle: ")
top_selling_nestle_product = max(nestleDict , key= nestleDict.get)
top_selling_nestle_product_sales_figures = max(nestleDict.values())
print(top_selling_nestle_product , "with sales figures =" , top_selling_nestle_product_sales_figures , "US Dollars")

#Print the top selling product from Unilever with sales figures.

print("The top selling product from Unilever: ")
top_selling_unilever_product = max(unileverDict , key= unileverDict.get)
top_selling_unilever_product_sales_figures = max(unileverDict.values())
print(top_selling_unilever_product ,"with sales figures =",  top_selling_unilever_product_sales_figures , "US Dollars")

#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.

nestleCountries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan" }
unileverCountries = { "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates" }

print("All the cities Nestle sell their products in :")
for i in nestleCountries:
    print(i)

print("All the cities Unilever sell their products in :")
for i in unileverCountries:
    print(i)


#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.

cities_both_NestleANDUnilver_sell_in = nestleCountries & unileverCountries
print("the cities that both Nestle & Unilver sell in common:" ,cities_both_NestleANDUnilver_sell_in)

#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.

cities_nestle_but_not_unilever_sell_in = nestleCountries - unileverCountries
print("the cities Nestle sells in , but Unilver doens't sell in:" ,cities_nestle_but_not_unilever_sell_in)

