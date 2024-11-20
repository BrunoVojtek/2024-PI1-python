import random #kniznica ktora sluzi na generovanie nahodnych hodnot

nahodne_cislo = random.randint(1,10) #vygeneruje nahodne cele cislo rozsahu 1-10
print (nahodne_cislo)

nahodna_farba = random.choice(["red", "green,","blue"]) #vygeneruje nahodnu hodnotu zo zoznamu hodnot, zoznam ohranicime []
print (nahodna_farba)

nahodne_pismeno = random.choice("aeiouy") #vygeneruje nahodnu samohlasku
print(nahodne_pismeno)
