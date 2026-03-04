while True:
    lasku= input("Mitä lasketaan? Osaan peruslaskuja (+) (-) (/) (*). 'lopeta' lopettaa laskimen: ")

    if lasku == "lopeta":
        print("Lopetetaan...")
        break

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