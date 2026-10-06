class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, kiihdytys):
        self.tämänhetkinen_nopeus = self.tämänhetkinen_nopeus + kiihdytys
        if self.tämänhetkinen_nopeus < 0:
            print("Tämän hetkinen nopeus on 0.")
            self.tämänhetkinen_nopeus = 0

        elif self.tämänhetkinen_nopeus > 100:
            print("Tämän hetkinen nopeus ylittyy tietyn nopeuden.")

# Annetaan auton kiihtyvyyden arvot.
auto1 = Auto("ABC", 45)
auto1.kiihdytä(30)
print(auto1.tämänhetkinen_nopeus)
auto1.kiihdytä(70)
print(auto1.tämänhetkinen_nopeus)
auto1.kiihdytä(50)
print(auto1.tämänhetkinen_nopeus)

# Tehdään hätäjarrutus.
auto1.kiihdytä(-200)
print(auto1.tämänhetkinen_nopeus)

            

        


