ikä = int(input("Anna ikäsi: ")) 
toisto = 0

if ikä > 12:
    print("Terve käyttäjä!")
    komento = input("Tehdään hupaisia juttuja! Kyllä vai ei?")
    

    while komento == "kyllä":
        toiminto = input("Anna kirjain a-c: ")

        if toiminto == "lopeta" or toisto == 5:
            print("Komento sammuu!")
            break

        elif toiminto == "a":
            toisto += 1
            print("Maailman väestössä on yli 8 miljardia.")
            
           

        elif toiminto == "b":
            toisto += 1
            print("Tässä on vitsi...sinä!")
            
            

        elif toiminto == "c":
            toisto += 1
            print("Katso taaksesi >:)")
            

        else:
            print("Syötä kirjain a-c: ")
            toiminto = input("Anna kirjain a-c: ")

print("Olet alle 12-vuotias, komento sammuu.")