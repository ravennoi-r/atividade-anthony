def calcular_media(nota1: float, nota2: float, nota3: float) -> float:
    return (nota1 + nota2 + nota3) / 3


def verificar_situacao(media: float) -> str:
    if media >= 7:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    return "Reprovado"


n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = calcular_media(n1, n2, n3)
situacao = verificar_situacao(media)

print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")