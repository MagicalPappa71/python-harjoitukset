# Ohjelma kysyy käyttäjältä lukuja.
luku = int(input("Anna luku: "))
while luku != "":
    print(str(luku))
    # Jos annetaan "", niin ohjelma lopettaa tulostamisen.
    luku = int(input("Anna luku: "))
print("Annoit tyhjän luvun, ohjelma lopetettu!")

