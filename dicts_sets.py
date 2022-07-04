# DICTS_SETS

### Kate, Dalia & Monica are work associates . They all work at a consultancy company.

## Kate has the products sales of Nestle :

##### KitKat : 34,456,432 US Dollars
##### Nescafe : 14,106,132 US Dollars
##### Maggi : 9,960,312 US Dollars
##### Nido : 44,506,003 US Dollars


## Dalia has the products sales of Unilever :

##### Lipton : 23,456,000 US Dollars
##### Breyers : 1,235,891 US Dollars
##### HellManns : 17,241,412 US Dollars
##### Marmite : 11,715,324 US Dollars


## Monica has 2 tables containing the countries in which Unilever and Nestle sell the products:
##### Nestle : "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"
##### Unilever : "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"


## Using what you've learned during . Please do the following :
# - Create a variable to hold the values of Nestle products (use a dicitionary)
Unilever_products = {"Lipton" : "23,456,000 US Dollars", "Breyers" : "1,235,891 US Dollars", "HellManns" : "17,241,412 US Dollars", "Marmite" : "11,715,324 US Dollars"}

# - Create a variable to hold the values of Unilever products (Use a dictionary)
Nestle_products = {"KitKat" : "34,456,432 US Dollars", "Nescafe" : "14,106,132 US Dollars", "Maggi" : "9,960,312 US Dollars", "Nido" : "44,506,003 US Dollars"}

# - Print each product sold by Unilever and the sales figures / numbers  for that product.
print("Nestle_products: ")
print()
for key, value in Nestle_products.items():
    print(key, value)
    print()
# - Print each product sold by Nestle and the sales figures / numbers  for that product.
print("Unilever_products: ")
print()
for key, value in Unilever_products.items():
    print(key, value)
    print()
# - Print which of the companies has more products that the other company.
print("all companies have the same number of products")
# - Print the top selling product from Nestle with sales figures.
print()
print("The top selling product from Nestle: ")
print()
top_selling_nestle_product = max(Nestle_products , key= Nestle_products.get)
top_selling_nestle_product_sales_figures = max(Nestle_products.values())
print(top_selling_nestle_product , "with sales figures =" , top_selling_nestle_product_sales_figures , "US Dollars")
print()

# - Print the top selling product from Unilever with sales figures.
print()
print("The top selling product from Nestle: ")
print()
top_selling_nestle_product = max(Unilever_products , key= Unilever_products.get)
top_selling_nestle_product_sales_figures = max(Unilever_products.values())
print(top_selling_nestle_product , "with sales figures =" , top_selling_nestle_product_sales_figures , "US Dollars")
print()
# - Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
Nestle_cities = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}

Unilever_cities = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print(Nestle_cities)
print(Unilever_cities)

# - Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
cities_sell_both = Nestle_cities & Unilever_cities
print(cities_sell_both)

# - Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
cities_sell_both = Nestle_cities - Unilever_cities
print(cities_sell_both)



