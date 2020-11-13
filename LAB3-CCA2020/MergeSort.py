from random import random

#INPUT:-
print("\n>>>>>>>>>>>>>>>>>>>>>>>>>> M E R G E    S O R T <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
def mergeSort(lista):
    print("dividiendo elementos: ",lista)
    if len(lista)>1:
        med = len(lista)//2
        izqmitad = lista[:med]
        dermitad = lista[med:]

        mergeSort(izqmitad)
        mergeSort(dermitad)

        i=0
        j=0
        k=0
        while i < len(izqmitad) and j < len(dermitad):
            if izqmitad[i] <= dermitad[j]:
                lista[k]=izqmitad[i]
                i=i+1
            else:
                lista[k]=dermitad[j]
                j=j+1
            k=k+1

        while i < len(izqmitad):
            lista[k]=izqmitad[i]
            i=i+1
            k=k+1

        while j < len(dermitad):
            lista[k]=dermitad[j]
            j=j+1
            k=k+1
    print("fusionando elementos: ",lista)
lista = []
n=10
for i in range(n):
    lista.append(int(random()*100))
print("\n Arreglo generado aleatoriamente: ",lista)
mergeSort(lista)
print("\n Arreglo final ordenado por Merge Sort: ",lista)
print("\n")