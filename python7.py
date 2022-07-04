





kate ={"KitKat" : 34456  , "Nescafe" : 14106  , "Maggi" : 9960 , "Nido" : 44506 }
dalia ={"Lipton" : 23456,  "Breyers" : 1235 , "HellManns" : 17241, "Marmite" : 11715}
print(kate)
print(dalia)

kay = ''
larger_kate = 0
for k,i in kate.items():
    if i > larger_kate:
        larger_kate = i
        kay=k

print(kay,larger_kate)

kay1 = ''
larger_dalia = 0
for k1, i1 in dalia.items():
    if i1 > larger_dalia:
        larger_dalia= i1
        kay1 = k1
print(kay1,larger_dalia)       



cities_Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
cities_Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
all_cities = cities_Nestle.union(cities_Unilever)
print(all_cities)

cities_both = cities_Unilever.intersection(cities_Nestle)
print(cities_both)
cities_for_Nestle_not_Unilever = cities_Nestle.difference(cities_Unilever)
print(cities_for_Nestle_not_Unilever)
