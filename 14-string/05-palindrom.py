# retazec, ktory je rovnaky pri citani od zaciatku alebo od konca

works = True

print("Pre skončenie programu napíš stop")

while works:
    ret = input("Zadaj reťazec: ")
    obrateny = ret[::-1]
    
    if ret == "stop":
         break
    
    if ret == obrateny:
        print("Reťazec", ret, "je palindrom")
    else:
        print("Reťazec", ret, "nie je palindrom")

