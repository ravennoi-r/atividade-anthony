produtos = []

while True:
    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Valor total em estoque")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))

        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        produtos.append(produto)

    elif opcao == "2":
        for produto in produtos:
            print(produto)

    elif opcao == "3":
        total = 0

        for produto in produtos:
            total += produto["preco"] * produto["quantidade"]

        print(f"Valor total em estoque: R$ {total:.2f}")

    elif opcao == "4":
        break

    else:
        print("Opção inválida")