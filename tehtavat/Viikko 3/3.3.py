sukupuoli= input("Mikä on biologinen sukupuolesi M=mies/W=nainen?: ")

hb= int(input("Mikä on hemoglobiiniarvosi? "))

if sukupuoli == "M":
    if hb < 134:
        print("Hemoglobiiniarvosi on matala!")
    elif 134 <= hb <= 195:
        print("Hemoglobiiniarvosi on normaali!")
    else:
        print("Hemoglobiiniarvosi on korkea!")

elif sukupuoli == "W":
    if hb < 117:
        print("Hemoglobiiniarvosi on matala!")
    elif 117 <= hb <= 175:
        print("Hemoglobiiniarvosi on normaali!")
    else:
        print("Hemoglobiiniarvosi on korkea!")