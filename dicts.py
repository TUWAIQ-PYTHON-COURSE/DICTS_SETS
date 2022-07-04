
nestle_products : dict = {'KitKat' : 34456432, 'Nescafe' : 14106132 , 'Maggi' : 9960312, 'Nido' : 44506003}
unilever_products : dict = {'Lipton' : 23456000, 'Breyers' : 1235891, 'HellManns' : 17241412, 'Marmite' : 11715324}

#---- def ---#

def nestle(nestle_products):
    print('\n//-- product sold by Nestle and the sales figures :')
    for key, value in nestle_products.items():  # all nestle_products 
        print(key, value, '{US Dollars}')

    nestle_top_sales_figure = 0
    for key, value in nestle_products.items():  # top selling nestle_products 
        if value > nestle_top_sales_figure:
            nestle_top_sales_figure = value

    
    key_list = list(nestle_products.keys())
    val_list = list(nestle_products.values())

    position = val_list.index(nestle_top_sales_figure)
    Top_nestle_product = key_list[position]

    print(f'\nTop selling product from Nestle is {Top_nestle_product} and sales figure is {nestle_top_sales_figure} US Dollar')
#--- def unilever --#
def unilever(unilever_products):
    print('\nHere is each product sold by Unilever and the sales figures :')
    for key, value in unilever_products.items():  # to print all unilever_products keys and values
        print(key, value, '{US Dollars}')

    unilever_top_sales_figure = 0
    for key, value in unilever_products.items():  #top selling unilever_products key and value
        if value > unilever_top_sales_figure:
            unilever_top_sales_figure = value










            

    # print key with top_selling_unilever_product value
    key_list = list(unilever_products.keys())
    val_list = list(unilever_products.values())

    position = val_list.index(unilever_top_sales_figure)
    top_unilever_product = key_list[position]
    print(f'\nTop selling Unilever is {top_unilever_product} && and sales figure is {unilever_top_sales_figure} US Dollar ..')


nestle(nestle_products)
unilever(unilever_products)

#the companies has more products that the other company.
number_of_nestle_products = len(list(nestle_products.keys()))
number_of_unilever_products = len(list(unilever_products.keys()))
if number_of_nestle_products > number_of_unilever_products:
    print(f'\nNestle has more products {number_of_nestle_products}')
    print('\n-------------')
if number_of_unilever_products > number_of_nestle_products:
    print(f'\nUnilever has more products {number_of_unilever_products}')
    print('\n-------------')
else:
    print('\nBoth companies = products.')


nestle_city = {"SaudiArabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_city = {"SaudiArabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}


print('\n//city Unilever & Nestle sell their products in')
print('\n-------------')
for i in nestle_city | unilever_city:
    print(i , end =' ')

#Using Sets 
print('\n-------------')
print('\n\nThe city that both Nestle & Unilver sell ')
for i in nestle_city & unilever_city:
    print(i , end =' ')
print('\n-------------')

print('\n\nThe city Nestle sells in , but Unilver doens not sell in')
print('')
for i in nestle_city - unilever_city:
    print(i, end= ' ') 
    print('\n-------------')
