numero= int(input("Anna joku vuosiluku, niin ilmoitan onko se karkausvuosi: "))
if numero > 0:
    if numero % 4 == 0 and numero % 100 !=0 or (numero % 400==0):
        print(numero,"Vuosi on karkausvuosi")
    else:
        print(numero,"Vuosi ei ole karkausvuosi")