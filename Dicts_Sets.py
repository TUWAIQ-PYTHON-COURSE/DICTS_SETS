#[1,2]
nestleProducts = {"KitKat": "34,456,432 US Dollars", "Nescafe": "14,106,132 US Dollars", "Maggi":"9,960,312 US Dollars", "Nido": "44,506,003 US Dollars"}
unileverProducts= {"Lipton" :" 23,456,000 US Dollars", "Breyers" : "1,235,891 US Dollars","HellManns" : "17,241,412 US Dollars","Marmite" : "11,715,324 US Dollars"}

'''
unil_product = list(unileverProducts.values())
print(f"- All product sold by Unilever are: {unileverProducts}")

nest_product = list(nestleProducts.values())
print(f"- All product sold by Nestle are: {nestleProducts}")
'''
#[3]
print("* Unilever: ")
for key,value in unileverProducts.items():
    print(f"The prodect {key}, The sales {value} ")
#[4]
print("* Nestle: ")
for key,value in nestleProducts.items():
    print(f"The prodect {key}, The sales {value} ")

#[5]
print()
if len(nestleProducts) > len(unileverProducts):
    print("- Nestle has products more than Unilever")
elif len(unileverProducts) > len(nestleProducts):
    print("- Unilever has products more than Nestle")
else:
    print("- Both companies have an equal number of products.")
#[6]
print()
topSells = max(nestleProducts.values())
topValue = max(nestleProducts, key = nestleProducts.get)
print(f"- The top selling product from Nestle is: {topValue} {topSells}")
#[7]
topSells = max(unileverProducts.values())
topValue = max(unileverProducts, key = unileverProducts.get)
print(f"- The top selling product from Unilever is: {topValue} {topSells}")

#[8]
print()
nestleCountries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unileverCountries = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print("- All the cities Unilever & Nestle sell their products in:")
for i in nestleCountries:
    print(i, end=", ")
for j in unileverCountries:
    print(j, end=", ")

#[9]
print()
print("- The cities that both Nestle & Unilver sell in common is: ")
commen = 0
for n in nestleCountries:
    for u in unileverCountries:
        if(n == u):
            commen = n
            print(commen , end=",")

#[10]
print()
print("- The cities Nestle sells in , but Unilver doens't sell in: ")
for n in nestleCountries: 
    if n in unileverCountries:
        continue
    print(n, end=",")