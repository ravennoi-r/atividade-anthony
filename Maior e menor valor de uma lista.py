def encontrar_maior_menor(numeros):
    maior = numeros[0]
    menor = numeros[0]

    for numero in numeros:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

    return maior, menor


numeros = [8, 3, 10, 1, 5]
maior, menor = encontrar_maior_menor(numeros)

print(maior)
print(menor)