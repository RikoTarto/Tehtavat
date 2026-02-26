hyttiluokka= input("Valitse hyttiluokka, niin kerron tietoa sinulle hytistä.: LUX, A, B, C: ").upper()

if hyttiluokka=="LUX": print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka=="A": print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka=="B": print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka=="C": print("C on ikkunaton hytti autokannen alapuolella.")
else : print("Hyttiluokka on virheellinen.")