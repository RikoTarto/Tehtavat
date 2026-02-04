import math

# Kysytään säde käyttäjältä
sade_str = input("Anna ympyrän säde: ")

# Jos käyttäjä kirjoittaa desimaalit pilkulla (esim. 2,5), vaihdetaan pisteeksi
sade = float(sade_str.replace(",", "."))

# Lasketaan pinta-ala: A = πr²
pinta_ala = math.pi * sade**2

# Tulostetaan tulos
print(f"Ympyrän pinta-ala on: {pinta_ala:.2f}")