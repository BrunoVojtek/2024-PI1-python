
cislo = int (input ("zadaj číslo: "))

print (f"Párne čísla do {cislo}:")
for i in range (2, cislo + 1, 2):
    print (i)

print (f"Nepárne čísla do {cislo}")
for i in range (1, cislo + 1, 2):
    print (i)

if cislo % 2 == 0:
    print ("Tvoje číslo je párne")

else:
    print ("Tvoje číslo je nepárne")


