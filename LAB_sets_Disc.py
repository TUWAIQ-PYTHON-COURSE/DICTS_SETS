nestle_productsc = {"KitKat" : " 34,456,432 US Dollars" ,"Nescafe" : "14,106,132 US Dollars" , "Maggi" : "9,960,312 US Dollars" ,"Nido ": "44,506,003 US Dollars"}
unilever_products = {"Lipton" : "23,456,000 US Dollars" , "Breyers" : "1,235,891 US Dollars" , "HellManns" : "17,241,412 US Dollars" , "Marmite" : "11,715,324 US Dollars"}

Nestle_cities= {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_cities = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
print("nestle_productsc :")
print()
for key, value in nestle_productsc.items():
    print(key, value)
    print()
print("#####################################")
print()
print("unilever_products :")
print()
for key, value in unilever_products.items():
    print(key, value)
print()
print("Both companies have the same number of products")
print()
print(" the top selling product from Nestle with sales figures :")
print(nestle_productsc["Nido "
] , "------> Nido")
print()

print("the top selling product from unilever with sales figures :")
print(unilever_products["Lipton"], "----> Lipton")
print()

print("This nestle cities :")
for x in Nestle_cities:
    print(x)

print("This Unilever cities :")
for v in Unilever_cities:
    print(v)


cities_that_both = Nestle_cities | Unilever_cities
print(cities_that_both)

cities_Nestle_sells_but_Unilver_doenst = Nestle_cities - Unilever_cities
print(cities_Nestle_sells_but_Unilver_doenst)