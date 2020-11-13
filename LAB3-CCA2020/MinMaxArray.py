from random import random


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
    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>> M A X I M O    Y    M I N I M O    E N    U N    A R R A Y <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
    print("\nArreglo generado aleatoriamente", A)
    # inicializar el elemento mínimo por infinito y el elemento máximo por menos infinito
    (min, max) = (INF, -INF)
    (min, max) = MinMax(A, 0, len(A) - 1, min, max)
    print("\nEl elemento minimo del arreglo es: ", min)
    print("El elemento maximo del arreglo es: ", max)
    A.sort()
    print("\nArreglo finalmente ordenado: ", A)
    print("\n")
  
    
