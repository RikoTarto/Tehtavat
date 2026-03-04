import math
while True:
    lasku= input("Mitä lasketaan? Osaan peruslaskuja (+) (-) (/) (*). 'lopeta' lopettaa laskimen: ")
    print(f"Eli tehdään {lasku} laskuja.")
    luku1= float(input("Anna minulle 1 luku: "))
    luku2= float(input("Anna minulle 2 luku: "))

    if lasku == "+":
        print("Tulos: ", luku1 + luku2)

    elif lasku == "-":
        print("Tulos:", luku1 - luku2)

    elif lasku == "/":
        print("Tulos: ", luku1 / luku2)

    elif lasku == "*":
        print("Tulos: ", luku1 * luku2)
    else:
        print("Tuntematon toiminto")

    if lasku == "lopettaa":
        print("Lopetetaan...")
        break