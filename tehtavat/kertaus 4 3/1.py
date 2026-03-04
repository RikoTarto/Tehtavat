nimi= input("Kerro nimesi: ")

if nimi == ("Matti"):
    print("Hyvä Matti, mutta ei tällä kertaa")

else:

    määrä= int(input("Kerro keittoannosten määrä ja tulostan kokonaishinnan: "))

    kokonaishinta= 5.90*määrä

    print(f"Keittoannosten kokonaishinta on {kokonaishinta}€")