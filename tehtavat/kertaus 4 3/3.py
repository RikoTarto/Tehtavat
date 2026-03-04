import math
while True:

    luku= int(input("Anna minulle kokonaisluku: "))

    if luku <0:
        print("Virheellinen numero!")

    elif luku >0:
        print(f"Tässä sinulle luvun neliöjuuri: {math.sqrt(luku)}")

    else:
        luku== 0
        break