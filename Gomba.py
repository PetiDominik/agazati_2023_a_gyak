
class Gomba():
    def __init__(self, adatsor: str):
        adatok = adatsor.split("@")
        self.nev = adatok[0].strip()
        self.nemzet = adatok[1].strip()
        self.evszak = adatok[2].strip()

    def __str__(self):
        return f"{self.nev} - {self.nemzet} - {self.evszak}"

