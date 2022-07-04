

from multiprocessing.sharedctypes import Value
from optparse import Values


city_Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
city_Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

dictNestle =  {"Lipton" :23456000, "Breyers" : 1235891, "HellManns" : 17241412, "Marmite" : 11715324}
dictUnilever = {'KitKat':34456432,'Nescafe':14106132, 'Maggi':9960312, 'Nido':44506003}


#D_both = dictNestle,& dictUnilever
#B_both = dictUnilever,& dictNestle
print(max(dictUnilever))
#print(B_both)



def sum_Nestle(dictNestle):


    list_n = []
    for i in dictNestle:
        list_n.append(dictNestle[i])
    final = sum(list_n)
 
    return final

def sum_Unilever(dictUnilever):
 
    list_u = []
    for i in dictUnilever:
        list_u.append(dictUnilever[i])
    final = sum(list_u)
    return final
print((dictUnilever))

dict_N = 53648627
dict_U = 10302887




NU_diff: set = dictUnilever.difference(dictNestle)
print(dictUnilever&dictNestle)
print(dictUnilever.difference(dictNestle))
print(dictUnilever.intersection(dictNestle))
print(dictUnilever.Union(dictNestle))



NU_intersection = dictUnilever.intersection(dictNestle)
print(NU_diff)

#for key,value in dictUnilever.items():
 #   print(value)

#print(list(dict_Dalia.keys()))


