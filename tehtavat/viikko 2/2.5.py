print("Sinulla on vanhat mitat käytössä, muutetaan ne vastaamaan tätä päivää")

leviskat= (float(input("Kuinka monta leiviskaa?")))
naulat= (float(input("Kuinka monta naulata?")))
luodit= (float(input("Kuinka monta luodit?")))

lasku= leviskat *20 *30 + naulat *32 + luodit
grammat= lasku *13.5
kilot= int(grammat // 1000)
loput= grammat % 1000

print("uusissa mitoissa", kilot, "kiloa ja", loput, "grammaa")