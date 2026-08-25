# Ohjelma, joka kysyy kolme kokonaislukua
luku1 = int(input("Anna ensimmäinen kokonaisluku"))
luku2 = int(input("Anna toinen kokonaisluku"))
luku3 = int(input("Anna kolmas kokonaisluku"))
# tulostaa lukujen laskut
summa = luku1 + luku2 + luku3 
tulo = luku1 * luku2 * luku3
keskiarvo= (luku1 + luku2 + luku3) / 3
print("Lukujen summa:" + str(summa))
print("Lukujen tulo:" + str(tulo))
print("Lukujen keskiarvo" + str(keskiarvo))

