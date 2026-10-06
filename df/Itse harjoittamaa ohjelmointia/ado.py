class Ado:
    def __init__(self, nimi, tyyppi, laulu="Nandemo, nandemo, niiuah!"):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.laulu = laulu

ado = Ado("Ado","singer","Nandemo, nandemo, niiuah!")
print(f"Here's your guys beloved {ado.tyyppi} {ado.nimi}! - {ado.laulu}")

        