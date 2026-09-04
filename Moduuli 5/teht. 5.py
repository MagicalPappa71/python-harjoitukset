# Ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
tunnus = input("Anna käyttjätunnus: ")

salasana = input("Anna salasana: ")

toisto = 0
# Jos ohjelma ilmoittaa viisi kertaa väärää kirjautumista, niin ohjelma sammuu.
while tunnus != "python" or salasana != "rules":
    if toisto == 5:
        print("Pääsy evätty") 
        break
    
    print("Väärä käyttäjätunnus tai salasana, yritä uudelleen")
    toisto += 1
    tunnus = input("Anna käyttjätunnus: ")
    salasana = input("Anna salasana: ")

else:
    print("Tervetuloa")

  
    
    
    