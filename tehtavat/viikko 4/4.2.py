while True:
    tuuma = float(input("Anna minulle tuuma, niin muutan sen senttimetreiksi:"))

    if tuuma < 0:
        print("Anna positiivinen luku")
        break
    senttimetrit= tuuma * 2.54
    print(f"{tuuma} tuuma = {senttimetrit} cm")