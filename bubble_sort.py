class BubbleSort:
    def _init_(self, lista):
        elemento = len(lista)
        for i in range(elemento - 1):
            for j in range(elemento - 1 - i):
                if lista[j] > lista[j + 1]:
                    aux = lista[j + 1]
                    lista[j + 1] = lista[j]
                    lista[j] = aux

        self.sorted_list = lista