# Ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
nimet = set()
nimi = input("Anna nimesi: ")

# While silmukka, missä myös nimejä lisätään joukkoon. 
while nimi != "":
    print(nimi)
    nimet.add(nimi)
    nimi = input("Uusi nimi: ")

# Ohjelma tulostaa lopuksi kaikki nimet yksi tellen allekkaisessa järjestyksessä.

for n in nimet:
    print(n)
