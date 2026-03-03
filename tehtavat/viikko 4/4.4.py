import random

salainen_luku = random.randint(1,10)

while True:
    arvaus= int(input("Arvaa luku 0-10:"))

    if arvaus > salainen_luku:
        print("Liian suuri arvaus")
    elif arvaus < salainen_luku:
        print("Liian pieni arvaus")
    else:
        print("Oikea arvaus")
        break