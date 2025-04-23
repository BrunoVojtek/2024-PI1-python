subor = open("subor.txt", "r") # toto je relatívna cesta k súboru (musí byť v tom istom priečinku ako samotný kód)
# otvorí súbor subor.txt na čítanie, pre zápis sa používa "w", "r" - read, "w" - write
# subor = open("c:/dokumenty/subor.txt", "r") toto je absolútna cesta
# subor = open("../16-list/subor.txt", "r") .. je o priečinok vyššie 
# for i in range(4):
#     riadok = subor.readline() #readline() prečíta celý riadok (od mieste kde sa aktuálne nachádza) zo súboru a uloží do premennej
#     print(riadok)

# riadok = subor.readline()
# while riadok != "":
#     print(riadok)
#     riadok = subor.readline()

while True:
    riadok = subor.readline()
    if riadok == "":
        break
    print (riadok.strip()) # .strip() odrstani nečítateľné znaky napr. \n, \t

subor.close() # zatvorí súbor