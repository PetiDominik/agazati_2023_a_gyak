from Gomba import Gomba

def megoldas3():
    osszesGomba: list[Gomba] = beolvasas()
    gombak_szama(osszesGomba)
    papsakpa(osszesGomba)
    tinoru(osszesGomba)

def beolvasas() -> list[Gomba]:
    osszesGomba: list[Gomba] = []
    with open("gombak.txt", "r", encoding="utf-8") as beFajl:
        # beFajl.readline()
        for sor in beFajl:
            osszesGomba.append(Gomba(sor.strip()))
    return osszesGomba

def gombak_szama(oGomba: list[Gomba]):
    print(f"III/A, B:\n\tA gombák száma: {len(oGomba)}.")

def papsakpa(oGomba: list[Gomba]):
    i = 0
    while (i < len(oGomba) and (oGomba[i].nemzet != "papsapkagombák")):
        i += 1
    print(f"III/C:\n\tAz első papsapkagomba neve: {oGomba[i].nev}.")

def tinoru(oGomba: list[Gomba]):
    db = 0
    for gomba in oGomba:
        if gomba.nemzet == "tinóru":
            db += 1

    print(f"III/D:\n\tA tinóru gombák száma: {db}.")
