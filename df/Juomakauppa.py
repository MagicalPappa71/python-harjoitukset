# Tulostaa juomat, joita asiakas voi tilata

# Kysytään asiakkaan ikä
ika = int(input("Kuinka vanha olet?"))

# Kysy asiakkaan rotu
laji = input("Minkä lajinen olet?")

# Tulostaa juomat, mitä asiakas voi tilata
# Kaikki voivat tilata kahvia
# Yli 18 vuotiaat ihmiset voivat tilata viiniä
# Yli 100 vuotiaat tontut voivat tilata olutta
# Robotit voivat tilata öljyä
if laji == "ihminen" and ika >= 18:
    print("1. kahvi")
elif laji == "tonttu" and ika >= 100:
    print("2. Olut")
elif laji == "robotti":
    print("2. Öljy")
