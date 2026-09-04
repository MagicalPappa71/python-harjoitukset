tuuma = float(input("Anna tuuman määrä: "))
# Yksi tuuma vastaa 2,54 cm.
tuuma_sentteinä = tuuma * 2.54
while tuuma_sentteinä > -1:
    print("Tuuma on " + str(tuuma_sentteinä) + " senttimetriä.")
    tuuma = float(input("Anna tuuman määrä: "))
    tuuma_sentteinä = tuuma * 2.54
print("Luku on negatiivinen, ei voi tulostaa")
# Jos ohjelmalle annetaan negatiivinen luku, niin ohjelma lopettaa. 