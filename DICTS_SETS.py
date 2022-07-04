nestle_products : dict = {'KitKat' : 34456432, 'Nescafe' : 14106132 , 'Maggi' : 9960312, 'Nido' : 44506003}
unilever_products : dict = {'Lipton' : 23456000, 'Breyers' : 1235891, 'HellManns' : 17241412, 'Marmite' : 11715324}

def nestle(nestle_products):
    print('\nHere is each product sold by Nestle and the sales figures :')
    for key, value in nestle_products.items():  # to print all nestle_products keys and values
        print(key, value, 'US Dollars')

    nestle_top_sales_figure = 0
    for key, value in nestle_products.items():  # to print top selling nestle_products key and value
        if value > nestle_top_sales_figure:
            nestle_top_sales_figure = value

    # print key with top_selling_nestle_product value
    key_list = list(nestle_products.keys())
    val_list = list(nestle_products.values())
 
    position = val_list.index(nestle_top_sales_figure)
    Top_nestle_product = key_list[position]

    print(f'\nTop selling product from Nestle is {Top_nestle_product} and sales figure is {nestle_top_sales_figure} US Dollar ..')

def unilever(unilever_products):
    print('\nHere is each product sold by Unilever and the sales figures :')
    for key, value in unilever_products.items():  # to print all unilever_products keys and values
        print(key, value, 'US Dollars')
    
    unilever_top_sales_figure = 0
    for key, value in unilever_products.items():  # to print top selling unilever_products key and value
        if value > unilever_top_sales_figure:
            unilever_top_sales_figure = value

    # print key with top_selling_unilever_product value
    key_list = list(unilever_products.keys())
    val_list = list(unilever_products.values())

    position = val_list.index(unilever_top_sales_figure)
    top_unilever_product = key_list[position]
    print(f'\nTop selling product from Unilever is {top_unilever_product} and sales figure is {unilever_top_sales_figure} US Dollar ..')
        

nestle(nestle_products)
unilever(unilever_products)

# Print which of the companies has more products that the other company.
number_of_nestle_products = len(list(nestle_products.keys()))
number_of_unilever_products = len(list(unilever_products.keys()))
if number_of_nestle_products > number_of_unilever_products:
    print(f'\nNestle has more products {number_of_nestle_products}')
if number_of_unilever_products > number_of_nestle_products:
    print(f'\nUnilever has more products {number_of_unilever_products}')
else:
    print('\n***Both companies have an equal number of products.***')


nestle_cities = {"SaudiArabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_cities = {"SaudiArabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print('\nAll the cities Unilever & Nestle sell their products in')
for i in nestle_cities | unilever_cities:
    print(i , end =' ')
#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print('\n\nThe cities that both Nestle & Unilver sell in common ..')
for i in nestle_cities & unilever_cities:
    print(i , end =' ')
#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print('\n\nThe cities Nestle sells in , but Unilver doens not sell in')
for i in nestle_cities - unilever_cities:
    print(i, end= ' ')