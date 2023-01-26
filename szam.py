import random


def megoldas1():
    randomSzam: int = random.randint(1, 50)
    print(f"I/A:\n\tA generált szám: {randomSzam}")

    szoveg = ""
    if (randomSzam % 5 == 0) and (randomSzam % 3 == 0):
        szoveg = "öttel és hárommal is"
    elif randomSzam % 5 == 0:
        szoveg = "öttel"
    elif randomSzam % 3 == 0:
        szoveg = "hárommal"

    if szoveg != "":
        print(f"I/B:\n\tA szám {szoveg} osztható!")
