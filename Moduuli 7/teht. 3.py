# Yksi gallona on 3,785 litraa.
def muunna_litroiksi(gallonat):
    litra = 3.785
    summa = gallonat * litra
    return summa

# Ohjelma muuttaa gallojen määrää litroiksi. Jos arvo on negatiivinen, niin ohjelma lopettaa tulostuksen.
gallon_määrä = float(input("Anna gallon määrä: "))
muunna_litroiksi(gallon_määrä)

while gallon_määrä >= 0:
    print(f"{gallon_määrä} galloa on {muunna_litroiksi(gallon_määrä)} litraa")
    gallon_määrä = float(input("Anna gallon määrä: "))

print("Annettu arvo on negatiivinen.")

    


    
    