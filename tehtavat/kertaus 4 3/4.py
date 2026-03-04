tarina= ""
while True:
    sana= input("Anna sana ja teen sinulle tarinan: ")
    if sana == "Loppu" or sana == "loppu":
        break
    tarina= tarina + " " + sana

print(tarina)