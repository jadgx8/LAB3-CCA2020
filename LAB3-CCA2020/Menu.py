import os
from random import randint
from random import random

def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('cls') # NOTA para windows tienes que cambiar clear por cls
    print ("\n >>>>>>>>>> L A B O R A T O R I O  3   - - - -   D I V I D E    Y   V E N C E R A S <<<<<<<<<<<\n")
    print (">>>>>>>>>>>>>>>>>>>>>>>>>> Elaborado por Jesus De Gracia & Gisela Ojo <<<<<<<<<<<<<<<<<<<<<<<<<<\n")
    print ("Selecciona una opción")
    print ("\t1 - Busqueda Binaria")
    print ("\t2 - Quick Sort")
    print ("\t3 - Maximo y Minimo de un Array")
    print ("\t4 - Merge Sort")
    print ("\t9 - salir")
    
while True:
# Las 4 opciones del menu - Divide y Venceras
    def BusquedaBinaria():
        N = 10
        lista = []
        for x in range(N):
            lista.append(int(random()*100))
    
        lista.sort()

        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>> B U S Q U E D A    B I N A R I A <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
        print("Arreglo generado aleatoriamente: ", lista)
        

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
    def QuickSort():
        def particion(arreglo, inicio, final):
            pivote = arreglo[inicio]
            menor = inicio + 1
            mayor = final
            while True:
                #elementos que son más altos que pivotee
                while menor <= mayor and arreglo[mayor] >= pivote:
                    mayor = mayor - 1
                #elems that are menorer than pivote
                while menor <= mayor and arreglo[menor] <= pivote:
                    menor = menor + 1
                if menor <= mayor:
                    arreglo[menor], arreglo[mayor] = arreglo[mayor], arreglo[menor]
                else:
                    break
            arreglo[inicio], arreglo[mayor] = arreglo[mayor], arreglo[inicio]
            return mayor
        def quick_sort(arreglo, inicio, final):
            if inicio >= final:
                return None
            p = particion(arreglo, inicio, final)
            quick_sort(arreglo, inicio, p-1)
            quick_sort(arreglo, p+1, final)
        def generator():
            l1 = list()
            print("\n>>>>>>>>>>>>>>>>>>>>>>>>>> M E T O D O    Q U I C K S O R T<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
            n = int(input("Ingresa el tamaño del arreglo a ordenar: \n"))
            for i in range(n):
                i += 1
                l1.append(randint(0, 50))
                if i > n:
                    break
            return l1
        arreglo = generator()
        print("\nArreglo generado aleatoriamente:", arreglo)
        quick_sort(arreglo, 0, len(arreglo) - 1)
        print("\nArreglo Ordenado por Quicksort: ", arreglo)
        print("\n")
    def MinMaxArray():
        INF = float('inf')
        # Solución Divide y venceras para encontrar el número mínimo y máximo en una lista
        def MinMax(A, izq, der, min, max):

            # si la lista contiene solo un elemento

            if izq == der:		   # Comparacion Comun

                if min > A[der]:	  # comparacion 1
                    min = A[der]

                if max < A[izq]:	   # comparacion 2
                    max = A[izq]

                return min, max

            # si la lista contiene solo dos elementos

            if der - izq == 1:	   # Comparacion Comun

                if A[izq] < A[der]:  # comparacion 1
                    if min > A[izq]:   # comparacion 2
                        min = A[izq]

                    if max < A[der]:  # comparacion 3
                        max = A[der]

                else:
                    if min > A[der]:  # comparacion 2
                        min = A[der]

                    if max < A[izq]:   # comparacion 3
                        max = A[izq]

                return min, max

            # encontrando el elemento medio
            med = (izq + der) // 2

            # recurrir a la sublista izquierda
            min, max = MinMax(A, izq, med, min, max)

            # recurrir a la sublista derecha
            min, max = MinMax(A, med + 1, der, min, max)

            return min, max


        if __name__ == '__main__':
             # proceso de creación de arreglo
            A = []
            n = 10
            for i in range(n):
                A.append(int(random()*100))
            print("\n>>>>>>>>>>>>>>>>>>>>>>>>>> M I N I M O    Y    M A X I M O    E N    U N    A R R A Y <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
            print("\nArreglo generado aleatoriamente", A)
            # inicializar el elemento mínimo por infinito y el elemento máximo por menos infinito
            (min, max) = (INF, -INF)
            (min, max) = MinMax(A, 0, len(A) - 1, min, max)
            print("\nEl elemento minimo del arreglo es: ", min)
            print("El elemento maximo del arreglo es: ", max)
            A.sort()
            print("\nArreglo finalmente ordenado: ", A)
            print("\n")
    def MergeSort():
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

#Empezamos el menú
    menu()
 
# solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ")
    os.system('cls') 
 
    if opcionMenu=="1":
        os.system('cls') 
        BusquedaBinaria()
        input("\npulsa una tecla para continuar")
        os.system('cls') 
    elif opcionMenu=="2":
        os.system('cls') 
        QuickSort()
        input("\npulsa una tecla para continuar")
        os.system('cls') 
    elif opcionMenu=="3":	
        os.system('cls') 
        MinMaxArray()
        input("\npulsa una tecla para continuar")
        os.system('cls') 
    elif opcionMenu=="4":	
        os.system('cls') 
        MergeSort()
        input("\npulsa una tecla para continuar")
        os.system('cls') 
    elif opcionMenu=="9":
        os.system('cls') 
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")