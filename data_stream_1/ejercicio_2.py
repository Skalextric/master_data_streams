import random

aciertos = 0
Num_Valores = 200;
UpperQuarter = (Num_Valores*3)/4
Intentos = 10000
K = 8

lista = range(1, Num_Valores + 1)

for x in range(Intentos):
    random.shuffle(lista)
    for x in lista[:K]  :
        if x > UpperQuarter:
            aciertos += 1
            break


print 1 - aciertos/float(Intentos)