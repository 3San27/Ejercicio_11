import bubble_sort as bs
while True:

    lista = []
    fin = False

    while True:

        while True:
            elemento = input("Introducir elemento de lista a ordenar: ")
            if elemento == "fin":
                fin = True
                break

            try:
                elemento = int(elemento)
                break

            except:
                print("El dato introducido no es un número que sea válido")
        if fin:
            break
        if (elemento == -9999):
            break
        lista.append(elemento)
    if fin:
        break
lo = bs.BubbleSort(lista)
print("Lista ordenada: ", '\n', lo.sorted_lista)