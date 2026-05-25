class Usuario:
    def __init__(self, user_id, nome, email, senha):
        self.id = user_id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = True


usuarios = []


while True:
    print("\n===== SISTEMA DE USUÁRIOS =====")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário por e-mail")
    print("4 - Autenticar usuário")
    print("5 - Desativar usuário")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        user_id = len(usuarios) + 1

        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")

        usuario = Usuario(user_id, nome, email, senha)

        usuarios.append(usuario)

        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
        else:
            for usuario in usuarios:
                print("\n----------------")
                print(f"ID: {usuario.id}")
                print(f"Nome: {usuario.nome}")
                print(f"Email: {usuario.email}")
                print(f"Ativo: {usuario.ativo}")

    elif opcao == "3":
        email = input("Digite o email: ")

        encontrado = False

        for usuario in usuarios:
            if usuario.email == email:
                print("\nUsuário encontrado:")
                print(f"ID: {usuario.id}")
                print(f"Nome: {usuario.nome}")
                print(f"Email: {usuario.email}")
                print(f"Ativo: {usuario.ativo}")
                encontrado = True

        if not encontrado:
            print("Usuário não encontrado.")

    elif opcao == "4":
        email = input("Email: ")
        senha = input("Senha: ")

        autenticado = False

        for usuario in usuarios:
            if (
                usuario.email == email
                and usuario.senha == senha
                and usuario.ativo
            ):
                autenticado = True

        if autenticado:
            print("Login realizado com sucesso!")
        else:
            print("Credenciais inválidas.")

    elif opcao == "5":
        email = input("Digite o email do usuário: ")

        encontrado = False

        for usuario in usuarios:
            if usuario.email == email:
                usuario.ativo = False
                print("Usuário desativado!")
                encontrado = True

        if not encontrado:
            print("Usuário não encontrado.")

    elif opcao == "6":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")