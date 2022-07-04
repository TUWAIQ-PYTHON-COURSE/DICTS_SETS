


#q1&2

Kate_Nestle = { "KitKat" : "34,456,432 US Dollars" , "Nescafe " : "14,106,132 US Dollars" ,
"Maggi" : "9,960,312 US Dollars" , "Nido" : "44,506,003 US Dollars" } 

Dalia_Unilever = {"Lipton" : "23,456,000 US Dollars" , "Breyers" : "1,235,891 US Dollars"
, "HellManns" : "17,241,412 US Dollars" , "Marmite" : "11,715,324 US Dollars"}

Monica_Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Monica_Unilever  = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
#q3&4
Nestvalues =list(Kate_Nestle.values())
print(f" All Nestle values are : {Nestvalues} ")

UniValues = list(Dalia_Unilever.values())
print(f" All Unilever values are : {UniValues} ")

print(" Unilever : ")
for key , value in Dalia_Unilever.items() :
     print( f" The Proudct {key} The Sales {value} ") 

print("Nestle  : ")
for key , value in Kate_Nestle.items() :
   print( f" The Proudct {key} The Sales {value} ") 

#5
def Maxproudect(Dalia_Unilever,Kate_Nestle ) :
 i = 0
for i in Dalia_Unilever.keys():
    i+=str(1)
 
j=0
for j in Kate_Nestle.keys():
    j+=str(1)
   

if i> j :
    print("Unileve is max ")
elif i < j : 
    print(" Nestle is max ")
else : 
    print(" they are quall ")


Maxproudect(Dalia_Unilever,Kate_Nestle) 

#q6&7
maxSells = max(Kate_Nestle.values())
max_value = max(Kate_Nestle, key=Kate_Nestle.get)
print(f" Top selling product from Nestle : { max_value } {maxSells}")


maxSells = max(Dalia_Unilever .values())
max_value = max(Dalia_Unilever , key=Dalia_Unilever.get)
print(f" Top selling product from Nestle : { max_value } {maxSells}")

#q8
for i in Monica_Nestle :
    print("all the cities Unilever & Nestle sell their products in : "+i)
for j in Monica_Unilever :
 print("all the cities Unilever & Nestle sell their products in : "+j)

#q9
commen = 0
for mN in Monica_Nestle :
    for mU in Monica_Unilever :
        if (mN == mU) :
            commen= mU
            print("the cities that both Nestle & Unilver sell in common "+ str(commen))



#q10
for mN in Monica_Nestle :
    if mN in Monica_Unilever :
        continue 
    print("the cities Nestle sells in , but Unilver doens't sell in."+str(mN))