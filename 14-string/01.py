#string je retazec znakov napr. "Ahoj"
#retazec zaciname a koncime "" alebo ''
#\n - novy riadok, \t - tabulator, \" - "
#funkcia len - vrati dlzku retazca (pocet znakov)
#znaky v retazci su indexovane - prvy znak ma index 0
#index piseme do [] = alt gr + f/g


retazec = "Ahoj Svet"
print(retazec)
print(len(retazec))
# print(retazec[1])

# for i in range(len(retazec)):
#     print(retazec[i])


for znak in retazec: #postupne vybera znaky z retazca do premennej znak
    print(znak)


