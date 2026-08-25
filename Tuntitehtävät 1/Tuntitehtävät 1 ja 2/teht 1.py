## kysyy käyttäjältä maalattavan seinän korkeus
korkeus = float(input("Anna korkeus"))
## kysy seinän leveys
leveys = float(input("Anna leveys"))
## kysy maalin kattavuus
kattavuus = float(input("Anna kattavuus"))
## lasketaan seinän pinta-ala
pinta_ala = korkeus * leveys
## lasketaan kuinka paljon maalia tarvitaan
maalin_tarve = pinta_ala / kattavuus
## tulostetaan tulos
print(f"Seinän maalaamiseen tarvitaan {maalin_tarve} litraa maalia")
