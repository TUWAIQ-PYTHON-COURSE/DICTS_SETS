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
# Create a variable to hold the values of Nestle products (use a dicitionary)
# Print each product sold by Unilever and the sales figures / numbers  for that product.

nestle_product = {"KitKat": "34,456,432", "Nescafe": "14,106,132", "Maggi": "9,960,312", "Nido": "44,506,003"}
for key, value in nestle_product.items():
    print(key, value)

# Create a variable to hold the values of Unilever products (Use a dictionary)
# Print each product sold by Nestle and the sales figures / numbers  for that product.

unilever_product = {"Lipton": "23,456,000", "Breyers": "1,235,891", "HellManns": "17,241,412", "Marmite": "11,715,324"}  
for key, value in unilever_product.items():
    print(key, value)

# Print which of the companies has more products that the other company.
number_of_nestle_products : int = len(list(nestle_product.keys()))
number_of_unilever_products : int = len(list(nestle_product.keys()))
if number_of_nestle_products > number_of_unilever_products:
    print(f'\nNestle has more products {number_of_nestle_products}')
if number_of_unilever_products > number_of_nestle_products:
    print(f'\nUnilever has more products {number_of_unilever_products}')
else:
    print('Both companies have an equal number of products.')

# Print the top selling product from Nestle with sales figures.
print("The top selling product from Nestle: ")
top_nestle_product = max(nestle_product , key= nestle_product.get)
top_nestle_product_sales_figures = max(nestle_product.values())
print(top_nestle_product , "with sales figures =" , top_nestle_product_sales_figures , "US Dollars")
# Print the top selling product from Unilever with sales figures.
print("The top selling product from Unilever: ")
top_unilever_product = max(unilever_product , key= unilever_product.get)
top_unilever_product_sales_figures = max(unilever_product.values())
print(top_unilever_product , "with sales figures =" , top_nestle_product_sales_figures , "US Dollars")

# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.

nestle_set = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_set = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

for x in nestle_set, unilever_set:
  print(x)

# Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.

sell_products = nestle_set | unilever_set
print(sell_products)

# Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.

sell_diff = nestle_set - unilever_set
print("In cities where Nestle sells", sell_diff, "but Unilver does'n sell there.")


