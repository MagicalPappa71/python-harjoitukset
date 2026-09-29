# Ohjelma kysyy käyttäjältä kuukauden numerot
vuodenajat = ("kevät", "kesä", "syksy", "talvi")
kuukauden_numerot = int(input("Anna kuukauden numero: "))


# Kun kuukauden numeroa annetaan, niin ohjelma tulostaa sitä mukaan kuukauden vuodenaika. 
if kuukauden_numerot < 3 or kuukauden_numerot == 12:
    print(f"Kuukauden {kuukauden_numerot}. vuodenaika on {vuodenajat[3]}")

elif kuukauden_numerot < 6 and kuukauden_numerot > 2:
    print(f"Kuukauden {kuukauden_numerot}. vuodenaika on {vuodenajat[0]}")

elif kuukauden_numerot < 9 and kuukauden_numerot > 5:
    print(f"Kuukauden {kuukauden_numerot}. vuodenaika on {vuodenajat[1]}")

elif kuukauden_numerot < 12 and kuukauden_numerot > 8:
    print(f"Kuukauden {kuukauden_numerot}. vuodenaika on {vuodenajat[2]}")





    

