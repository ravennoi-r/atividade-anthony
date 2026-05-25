def normalizar_nome(nome: str) -> str:
    nome = nome.strip()
    palavras = nome.split()

    palavras_formatadas = []

    for palavra in palavras:
        palavras_formatadas.append(palavra.capitalize())

    return " ".join(palavras_formatadas)


nome = input("Digite o nome: ")
print(normalizar_nome(nome))