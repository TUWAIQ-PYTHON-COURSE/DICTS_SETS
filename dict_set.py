# 1
from itertools import count


nestle_product = {"kitkat": 34456432, "nescafe": 14106132 , "maggi": 9960312, "nido": 44506003 }
# 2
unilever_product = {"lipton" : 23456000 , "breyers" : 1235891 , "hellManns" :  17241412 , "marmite": 11715324 }
# 3
for key, value in unilever_product.items():
    print(key, value)
# 4
print("#"*50)
for key, value in nestle_product.items():
    print(key, value)

# 5
print("#"*50)
nestle_counter = 0
unilever_countr = 0
for key in unilever_product:
    nestle_counter = nestle_counter + 1

for key in nestle_product:
    unilever_countr = unilever_countr + 1

if nestle_counter > unilever_countr:
    print("nestle has more products")
elif unilever_countr > nestle_counter:
    print("unilever has more products")
else:
    print("they are equal")

# 6
print("#"*50)
#max = nestle_product.pop()
# x =0
# max_value = 0
# max_key = ""
# for key, value in nestle_product.items():
#     x = nestle_product.get(key)
#     if x < nestle_product.get(key):
#         max_value = nestle_product.get(key)
#         max_key = key
#     max_value = x
#     max_key = key
# print(f"Top selling product is {max_key} by {max_value} ")

result2 = max(nestle_product, key=nestle_product.get)
print(f"Maximum value: {result2} by {nestle_product[result2]}")

# 7

# y =0
# max_value_2 = 0
# max_key_2 = ""
# for key, value in unilever_product.items():
#     y = unilever_product.get(key)
#     if y <= unilever_product.get(key):
#         print("dcawfqwdv")
#         max_value_2 = unilever_product.get(key)
#         max_key_2 = key
#     max_value_2 = y
#     max_key_2 = key
# print(f"Top selling product is {max_key_2} by {max_value_2} ")

# nest_values_list = list(nestle_product.values())
# nest_keys_list = list(nestle_product.keys())
# print(nest_keys_list, nest_values_list)



result = max(unilever_product, key=unilever_product.get)
print(f"Maximum value: {result} by {unilever_product[result]}")

print("#"*50)

# 8

nestle_set = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}

unilever_set = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

for z in nestle_set, unilever_set:
    print(z)

# 9
print(nestle_set.intersection(unilever_set))
# 10
print(nestle_set - unilever_set)
