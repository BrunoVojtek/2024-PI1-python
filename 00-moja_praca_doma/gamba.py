import random

moznosti = {
"párne":None,
"nepárne":None,
"vyber":None
}



def hrac():
    moznosti["párne"] = 2
    moznosti["nepárne"] = 1
    odpoved = random.choice([moznosti["párne"], moznosti["nepárne"]])
    print("Stlač [1] pre párne")
    print("Stlač [2] pre nepárne")

    while True:
        try:
            vyber = int(input("Vyber si jednu z možností: "))
            print(vyber)

            if vyber == 1:
                moznosti["vyber"] = moznosti["párne"]
                break
            elif vyber == 2:
                moznosti["vyber"] = moznosti["nepárne"]
                break
            else:
                print("Iba [1] a [2]")
        except ValueError:
            print("Zadaj platné číslo [1] alebo [2].")

    if vyber == odpoved:
        print("Vyhral si")
    else:
        print("Prehral si")
hrac()
