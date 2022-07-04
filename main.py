
nestle_set = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_set = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}


# - Create a variable to hold the values of Nestle products (use a dicitionary)
values_nestle = {"KitKat":34456432, "Nescafe":14106132, "Maggi":9960312, "Nido":44506003}

# - Create a variable to hold the values of Unilever products (Use a dictionary)
values_unilever = {"Lipton":23456000, "Breyers":1235891,"HellManns":17241412, "Marmite":11715324}
print("\n")
# - Print each product sold by Unilever and the sales figures / numbers  for that product.
print("Products sold by unilever:")
for i, j in values_unilever.items():
    print(f"{i} / {j}")
print("\n")
# - Print each product sold by Nestle and the sales figures / numbers  for that product.
print("Products sold by Nestle:")
for i, j in values_nestle.items():
    print(f"{i} / {j}")
print("\n")
# - Print which of the companies has more products that the other company.
if len(values_nestle) == len(values_unilever):
    print("They're equivalent.")
elif len(values_nestle) > len(values_unilever):
    print("Nestle has more products.")
else:
    print("Unilever has more products.")
print("\n")
# - Print the top selling product from Nestle with sales figures.

print(f"Top selling product by Nestle: {max(values_nestle)}")

# - Print the top selling product from Unilever with sales figures.
print(f"Top selling product by Unilever: {max(values_unilever)}")
print("\n")

# - Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print("All cities: ")
for i in (nestle_set | unilever_set):
    print(i)
print("\n")

# - Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print("Cities in common: ")
for i in (nestle_set & unilever_set):
    print(i)
print("\n")

# - Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print("Cities found only in Nestle: ")
for i in (nestle_set - unilever_set):
    print(i)







