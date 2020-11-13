from random import randint


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
print("\nArrgelo Ordenado por Quicksort: ", arreglo)
print("\n")