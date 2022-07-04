Nestle_products = {"KitKat": 34456432, "Nescafe": 14106132, "Maggi": 9960312, "Nido": 44506003}

Unilever_products = {"Lipton" : 23456000, "Breyers" : 1235891, "HellManns" :  17241412, "Marmite": 11715324}

for key, value in Unilever_products.items():
    print(key, value)

for key, value in Nestle_products.items():
    print(key, value)

Nestle_num = 0
Unilever_num = 0

for key in Nestle_products:
    Nestle_num += 1

for key in Unilever_products:
    Unilever_num += 1

if Nestle_num > Unilever_num:
    print("Nestle has more products")
elif Nestle_num < Unilever_num:
    print("Unilever has more products")
else:
    print("They have the same number of products")

top_nestle_key = max(Nestle_products, key = Nestle_products.get)
top_nestle_value = max(Nestle_products.values())
print(f"The top selling product from Nestle is {top_nestle_key} and the sale figure is {top_nestle_value}")

top_unilever_seeling = max(Unilever_products, key = Unilever_products.get)
top_unilever_value = max(Unilever_products.values())
print(f"The top selling product from Nestle is {top_unilever_seeling} and the sale figure is {top_unilever_value}")


Nestle_set = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}

Unilever_set = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print(Nestle_set)
print(Unilever_set)

cities_sell_both = Nestle_set & Unilever_set
print(cities_sell_both)

cities_nestle_sell = Nestle_set - Unilever_set
print(cities_nestle_sell)