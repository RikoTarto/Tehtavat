pituus = int(input("anna pituutesi: "))
paino = float(input("anna painosi: "))

bmi = paino / (pituus / 100) **2

print("BMI:si on:", bmi)