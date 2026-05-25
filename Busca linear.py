def buscar(lista, valor):
    for indice in range(len(lista)):
        if lista[indice] == valor:
            return indice

    return -1


nomes = ["Ana", "Carlos", "Joao", "Maria"]

print(buscar(nomes, "Joao"))
print(buscar(nomes, "Pedro"))