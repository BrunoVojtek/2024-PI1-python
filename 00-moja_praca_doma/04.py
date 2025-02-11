import random


def hod():
    min_hodnota = 1
    max_hodnota = 6
    hod = random.randint(min_hodnota,max_hodnota)
    return hod


while True:
    palyers = input("Zadaj počet hráčov (1-4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
    else:
        print("zla hodnota")
print(players)