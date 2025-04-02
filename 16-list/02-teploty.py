import random as rd

teploty = []
pocet_dni = 30

# naplni list teploty nahodnymi teplotami v rozsahu od 10 do 30
for i in range(30):
    # teploty[i] = rd.randint(10,30) # vrati chybu, lebo prvky este neexistuju
    teploty.append(rd.randint(10,30))

# vzpise list tepploty
for i in range(pocet_dni):
    print(f'{i+1}.den - {teploty[i]}°C')

# vypocita a vypise priemernu teplotu
# priemerna_teplota = sum(teploty)/pocet_dni
# print (priemerna_teplota)
suma = 0
for i in range(pocet_dni):
    suma += teploty[i]
priemerna_teplota = suma/pocet_dni
print(f'Priemerna teplota v mesiaci je: {priemerna_teplota}°C')

for i in range(pocet_dni):
    if teploty[i] < priemerna_teplota:
        print(f'Dni s podpriemernou teplotou: {teploty[i]}°C')




