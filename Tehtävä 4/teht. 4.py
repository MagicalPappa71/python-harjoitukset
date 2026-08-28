# Ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
vuosi = int(input("Anna vuosi"))
# Vuosi on karkausvuosi, jos se on jaollinen neljällä
if vuosi % 4 == 0:
    print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")