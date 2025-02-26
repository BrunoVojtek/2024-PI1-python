# # string v pythone je immutable, tzn. nemenitelny

ret = "Ahoj svet"
# ret[0] = "a" # toto je nemozne, lebo je immutable

ret = "a" + ret[1:] # ak chceme zmenit nejaky znak, musime to urobit takto
print(ret)

# retazce vieme porovnavat
print("a" == "a")
print(ord("a")) # ord() je funckia, funckia ktora vrati ordinalnu (ciselnu) hodnotu znaku
print(ord("A"))
print("a"=="A")
print("a">"A")
print(chr(64)) # chr() je funkcia, ktora na zaklade ordinalnej hodnoty vrati znak
