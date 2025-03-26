# print(bin(255))# vypise cislo v binarnej sustave
# print(hex(255))# vypise cislo v hexadecimalnej sustave
# print(0b11111111)# vypise binarne cislo v desiatkovej sustave
# print(0xff)# vypise hexadecimalne cislo v desiatkovej sustave

def dec_bin(cislo):
    binarne = ""
    while cislo>0:
        zvysok = cislo % 2
        binarne = str(zvysok) + binarne
        cislo = cislo // 2
    return binarne


def dec_hex(cislo):
    hexadecimalne = ""
    while cislo > 0:
        zvysok = cislo % 16
        if zvysok < 10:
            hexadecimalne = str(zvysok) + hexadecimalne
        # elif zvysok == 10:
        #     hexadecimalne = "A"+ hexadecimalne
        # elif zvysok == 11:
        #     hexadecimalne = "B"+ hexadecimalne
        # elif zvysok == 12:
        #     hexadecimalne = "C"+ hexadecimalne
        # elif zvysok == 13:
        #     hexadecimalne = "D"+ hexadecimalne
        # elif zvysok == 14:
        #     hexadecimalne = "E"+ hexadecimalne
        # else:
        #     hexadecimalne = "F"+ hexadecimalne                 
        else:
            hexadecimalne = chr(55+zvysok) + hexadecimalne
        cislo = cislo //16
    return hexadecimalne


cislo = 255

print(dec_hex(cislo))