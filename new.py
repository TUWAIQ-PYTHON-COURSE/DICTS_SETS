## Kate has the products sales of Nestle :

# KitKat : 34,456,432 US Dollars
# Nescafe : 14,106,132 US Dollars
# Maggi : 9,960,312 US Dollars
# Nido : 44,506,003 US Dollars

      
## Dalia has the products sales of Unilever :

# Lipton : 23,456,000 US Dollars
# Breyers : 1,235,891 US Dollars
# HellManns : 17,241,412 US Dollars
# Marmite : 11,715,324 US Dollars
      

# Monica has 2 tables containing the countries in which Unilever and Nestle sell the products:

# Nestle : "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"
# Unilever : "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"


'''
- Create a variable to hold the values of Nestle products (use a dicitionary)
- Create a variable to hold the values of Unilever products (Use a dictionary)
- Print each product sold by Unilever and the sales figures / numbers  for that product.
- Print each product sold by Nestle and the sales figures / numbers  for that product.
- Print which of the companies has more products that the other company.
- Print the top selling product from Nestle with sales figures.
- Print the top selling product from Unilever with sales figures.
- Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
- Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.

'''


#1- Create a variable to hold the values of Nestle products (use a dicitionary)

nestle_products = {"kitkat" : 34456432, "nescafe" : 14106132, "maggi" : 9960312, "nido" : 44506003}

#2- Create a variable to hold the values of Unilever products (Use a dictionary)

unilever_products = {"lipton" : 23456000, "bregers" : 1235891, "hellmanns" : 17241412, "marmite" : 11715324}

#3- Print each product sold by Unilever and the sales figures / numbers  for that product.

print("~"*30)

print("products sold by Unilever and sales figures are:")
for i , y in unilever_products.items():
    print(i,y)

#4- Print each product sold by Nestle and the sales figures / numbers  for that product.

print("~"*30)

print("products sold by nestle and sales figures are:")
for i , y in nestle_products.items():
    print(i,y)

#5- Print which of the companies has more products that the other company.

print("~"*30)

nestle_storehouse = 7532
unilever_storehouse = 1596

if nestle_storehouse > unilever_storehouse:
    print("nestles company has more products")
elif unilever_storehouse > nestle_storehouse:
    print("unilevers company has more products")

else:
    print("they are equal")

#6- Print the top selling product from Nestle with sales figures.

print("~"*30)

maximum = max(nestle_products, key=nestle_products.get)
print(f"top sold product for nestle: {maximum} for {nestle_products[maximum]}")

#7- Print the top selling product from Unilever with sales figures.

print("~"*30)

maximum = max(unilever_products, key=unilever_products.get)
print(f"top sold product for unilever: {maximum} for {unilever_products[maximum]}")

#8- Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.

print("~"*30)

cities_nestle_sell_in = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
cities_unilever_sell_in = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

for i in cities_nestle_sell_in, cities_unilever_sell_in:
    print(i)

#9- Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.

print("~"*30)

print(cities_nestle_sell_in.intersection(cities_unilever_sell_in))

#10- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.

print("~"*30)

print(cities_nestle_sell_in - cities_unilever_sell_in)
