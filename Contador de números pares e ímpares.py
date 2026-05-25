pares = 0
impares = 0

maior = None
menor = None

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < menor:
        menor = numero

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")