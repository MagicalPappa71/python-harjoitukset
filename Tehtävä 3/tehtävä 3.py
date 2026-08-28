## kysyy suorakulmion kannan
kanta = float(input("Anna kanta"))
## kysyy suorakulmion korkeuden
korkeus = float(input("Anna korkeus"))
## lasketaan suorakulmion piiri ja pinta-ala
pinta-ala = kanta * korkeus
piiri = korkeus * 2 + kanta * 2

print(f"piiri: {piiri: <5.3f}")
print(f"pinta-ala: {pinta-ala:}")