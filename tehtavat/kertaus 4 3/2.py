tuntipalkka= float(input("Kerro tuntipalkkasi: "))
print(f"Lasketaan päiväpalkkasi")

tunnit= float(input("Kerro työtunnit: "))
print(f"Eli tuntipalkkasi on {tuntipalkka} ja työtunteja on {tunnit}")

viikonpv= input("Minä viikonpäivinä olet tehnyt töitä?: ")
if viikonpv == "Sunnuntai" or viikonpv == "sunnuntai" :
    päiväpalkka= tunnit*tuntipalkka*2
    print(f"Päiväpalkkasi on {päiväpalkka} €")

else:
    print(f"Päiväpalkkasi on: {tunnit*tuntipalkka}€")