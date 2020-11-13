
from random import random

N = 10
lista = []
for x in range(N):
    lista.append(int(random()*100))
    
lista.sort()

print("\n>>>>>>>>>>>>>>>>>>>>>>>>>> B U S Q U E D A    B I N A R I A <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
print("LISTA GENERADA")
print(lista)

num = int(input("\nEscriba el numero que desea saber su posición mediante busqueda binaria: "))

mini = 0
maxi = N-1

while mini <= maxi:
    med = (mini + maxi) //2
    if num < lista[med]:
        maxi = med-1
    elif num > lista[med]:
        mini = med+1
    else:
        print("\nEl numero está localizado en la posicion: ",med)
        break
else:
    print("\nEste numero no esta en la lista\n")
