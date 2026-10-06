# Ohjelma, joka kysyy leivisköjä, nauloja ja luoteja.
lieviskä = int(input("Anna lieviskä."))
naula = int(input("Anna naula."))
luoti = float(input("Anna luoti."))

# Yksi lieviskä vastaa 20 naulaa 
laskettu_lieviskä = lieviskä * 20

# Yksi naula vastaa 32 luotia
laskettu_naula = naula * 32

# Yksi luoti vastaa 13,3 grammaa
laskettu_luoti = luoti * 13.3

# Tulostetaan massa nykymitan kilo- ja gramma.

kilo = (laskettu_lieviskä + laskettu_naula + laskettu_luoti) // 1000
gramma = (laskettu_lieviskä + laskettu_naula + laskettu_luoti) 
print("Massa nykymittojen mukaan: " + str(kilo) + " kilogrammaa ja " + str(gramma) + " grammaa.")

