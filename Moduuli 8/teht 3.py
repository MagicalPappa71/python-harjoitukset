# Lentoasemtietojen hakeminen ja tallentaminen
# Lentoasemien nimet ja ICAO-koodit
lentoaseman_tiedot = {"Helsinki-Vantaa": "EFHK",
                     "Oulu": "EFOU",
                     "Rovaniemi": "EFRO",
                      "Tampere-Pirkkala": "EFTP",
                      "Turku": "EFTU"}
# Voidaan myös lisätä ylimääräisiä tietoja mukaan alkioon.
lentoaseman_tiedot["Kuopio"] = "EFKU"
lentoaseman_tiedot["Joensuu"] = "EFJO"


# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
while True:
    lentoaseman_syöte = input("Syötetäänkö uusi lentoasema, hakea jo syötetyn lentoaseman tiedot vai lopetetaanko?: ")

    # Ohjelma kysyy lentoaseman nimeä, jolloin tämä tulostaa koodin.
    if lentoaseman_syöte == "syötä uusi lentoasema":
        nimi = input("Anna lentoaseman nimi: ")
        print(f"Lentoaseman nimi on {nimi} ja sen ICAO-koodi on {lentoaseman_tiedot[nimi]}")

    elif lentoaseman_syöte == "hae tiedot":
        tiedot = input("Anna lentoaseman koodi: ")
        print(f"Lentoaseman koodi on {tiedot} ja sen nimi on {lentoaseman_tiedot[tiedot]}")

    elif lentoaseman_syöte == "lopeta":
        print("Lopetetaan toiminto.")
        break
print("")
