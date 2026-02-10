print("Tässä sinulle kaksi random numerolukon koodi:")

import random
code1= ""
for i in range(3):
    code1 += str(random.randint(0,9))
print("Kolmenumeroinen pinkoodi:", code1)

code2= ""
for i in range(4):
    code2 += str(random.randint(1,6))
print("Nelinumeroinen pinkoodi:", code2)