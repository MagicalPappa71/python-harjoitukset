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

    def kulje(self, tuntimäärä):
        self.kuljettu_matka = self.tämänhetkinen_nopeus * tuntimäärä

auto1 = Auto("ABC", 45)
auto1.kiihdytä(30)
auto1.kulje(2)
print(auto1.kuljettu_matka)


        