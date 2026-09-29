# Tehtävän antona on luoda kolme funktiota. Lisäksi ohjelmasta pitäisi muodostaa pelin.
# Pelitarina alkaa
print("Vaellat metsässä iltapäivällä, tuot repun eteesi.")
print("Kaivat repusta jotain esinettä.")

#lista esineistä
pakkaus = []

def esineiden_lisäys(esineet):
    esine = input("Anna esine: ")
    esineet.append(esine)

print("Kaivoit repustasi")
esineiden_lisäys(esineet)

# Ensimmäinen funktio, kysyy käyttäjältä esineitä.
def omistamat_esineet(esineet):
    print("Sinulla on: ")
    for jokainen_esine in esineet:
        print(jokainen_esine)

# Tässä koodissa kysytään esineitä, jotka menevät "pakkaus" listaan. 
omistamat_esineet(pakkaus)



def tikku(kerrat):
    for i in range(kerrat):
        print("YUAAH!" + str(i+1))
    return

print("Oh boy, tuolla on tikku!")
kysymys = input("Poimitaanko sitä, vai ei poimita?: ")
if kysymys == "poimitaan":
    print("Alright, poimitaan")
    tikku(4)

else:
    print("Hpft, nah!")

