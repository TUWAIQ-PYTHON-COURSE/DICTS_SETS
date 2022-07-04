
#Create a variable to hold the values of Nestle products (use a dicitionary)
nestle = {" KitKat" : "34,456,432 US Dollars" , "Nescafe" : "14.106.132 US Dollars"  ,  "Maggi": "9,960,312 US Dollars" ,  "Nido": "44,506,003 US Dollars"}

# Create a variable to hold the values of Unilever products (Use a dictionary)
unilever =  {" Lipton" : "23,456,000 US Dollars" , "Breyers" : "1,235,891 US Dollars"  ,  "HellManns": "17,241,412 US Dollars" ,  "Marmite": "11,715,324 US Dollars"}

#Print each product sold by Unilever and the sales figures / numbers  for that product.
print(nestle)

for key, value in nestle.items():
    print(key, value)

#Print each product sold by Nestle and the sales figures / numbers  for that product.
print(unilever)

for key, value in unilever.items():
    print(key, value)

#Print the top selling product from Nestle with sales figures.
max_val = nestle.items()
maxNestle = max(max_val)
print(maxNestle)

#Print the top selling product from Unilever with sales figures.
max_valu = unilever.values()
maxUnilever = max(max_valu)
print(maxUnilever)

nestle_city = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_city = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.

nestle_city.update(unilever_city)
for x in nestle_city:
    print(x)

#by union 
all_city = nestle_city | unilever_city 
print(all_city)

#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.

both_city = set()
for x in nestle_city:
    if x in unilever_city:
        both_city.add(x)

print(both_city)

#by Intersection
all_city_inboth = nestle_city & unilever_city
print(all_city_inboth)


#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.

for city in nestle_city:
    if city not in unilever_city:
        print (city)

#by Difference
city_nestle = nestle_city - unilever_city
print(city_nestle)
