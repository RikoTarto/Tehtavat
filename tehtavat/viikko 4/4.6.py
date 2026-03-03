import random

N = int(input("Kuinka monta pistettä arvotaan (N)? "))

ympyra = 0

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y < 1:
        ympyra += 1

pi_likiarvo = 4 * ympyra / N
print("Piin likiarvo on", pi_likiarvo)