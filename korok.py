

def megoldas2():
    eletkorok = []
    for i in range(5):
        eletkorok.append(int(input(f"{i+1}.kor: ")))
    elekkorokKiir(eletkorok)
    elsoId = elsoIdos(eletkorok)
    konzolra_ir(elsoId)
    fajl_ir(elsoId)


def elekkorokKiir(lista: list[int]):
    for i in range(len(lista)):
        print(f"{lista[i]}", end=":" if i < len(lista)-1 else "\n")

def elsoIdos(lista: list[int]) -> int:
    i = 0
    while (lista[i] < 70) and (i < len(lista)):
        i += 1

    return i

def konzolra_ir(elsoId: int):
    print(f"II/D, E:\n\tElső idős ember korának helye a listában: {elsoId}")

def fajl_ir(elsoId: int):
    with open("oreg.txt", "w", encoding="utf-8") as kiFajl:
        kiFajl.write(f"II/F:\n\tElső idős ember korának helye a listában: {elsoId}")
