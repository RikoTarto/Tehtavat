Pienin= None
Suurin= None

while True:
    syote= (input("Anna joku luku, enter lopettaa ja tulostaa isoimman ja pienimmän luvun:"))
    if syote == "":
        break

    luku= float(syote)

    if Pienin is None or luku < Pienin:
        Pienin = luku

    if Suurin is None or luku > Suurin:
        Suurin = luku

if Pienin is not None:
    print(f"Pienin luku {Pienin}")
    print(f"Suurin luku {Suurin}")
else:
    print("Et antanut yhtään lukua")