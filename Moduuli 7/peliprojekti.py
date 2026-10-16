# Tehtävän antona on luoda kolme funktiota. Lisäksi ohjelmasta pitäisi muodostaa pelin.
# Pelitarina alkaa
print("Vaellat metsässä iltapäivällä, tuot repun eteesi.")
print("Kaivat repusta jotain esinettä.")

# Lista esineistä
reppu = []

# Ensimmäinen funktio, kysyy käyttäjältä esineen ja lisää listaan.
def inventaario(esineet):
    esine = input("Anna esine: ") 
    esineet.append(esine)
    print(f"Kaivoit repusta: {esine}")

# Toinen funkito tulostaa listan sisällön.

def omistamat_esineet(esineet):
    print("Sinulla on: ")
    for esine in esineet:
        print(esine)

# Näin ohjelma tulostaa repusta kaivetun esineen. 
inventaario(reppu)
omistamat_esineet(reppu)

# Kolmas funktio voi itse päättää mitä voit luoda.
def sieni(kerrat):
    for i in range(kerrat):
        print("YUAAH!" + str(i+1))
    return

print("Oh boy, tuolla on sieni!")
kysymys = input("Tökitäänkö tuota sieniä meidän esineellä, kyllä vai ei?: ")
if kysymys == "kyllä":
    print("Alright, tökitään")
    sieni(4)
    print("Ohoh, sehän on elävä sieni smurffi!")
    print('Älä töki toista!' " - sieni smurffi")
else:
    print("Hpft, nah!")

