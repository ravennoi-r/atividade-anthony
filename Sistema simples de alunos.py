def calcular_media(notas):
    return sum(notas) / len(notas)


alunos = []


while True:
    print("\n" + "="*30)
    print("         MENU ESCOLAR         ")
    print("="*30)
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Exibir aprovados")
    print("5 - Exibir recuperação")
    print("6 - Exibir reprovados")
    print("7 - Sair")
    print("="*30)

    opcao = input("Escolha: ")

    if opcao == "1":
        print("\n--- CADASTRO DE ALUNO ---")
        nome = input("Nome: ")
        matricula = input("Matrícula: ")

        notas = []

        for i in range(3):
            nota = float(input(f"Nota {i + 1}: "))
            notas.append(nota)

        media = calcular_media(notas)

        if media >= 7:
            situacao = "Aprovado"
        elif media >= 4:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        aluno = {
            "nome": nome,
            "matricula": matricula,
            "notas": notas,
            "media": media,
            "situacao": situacao
        }

        alunos.append(aluno)
        print(f"\nAluno {nome} cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--- LISTA DE ALUNOS ---")
        if not alunos:
            print("Nenhum aluno cadastrado no sistema ainda.")
        else:
            for aluno in alunos:
                print(f"Nome: {aluno['nome']} | Matrícula: {aluno['matricula']} | Média: {aluno['media']:.2f} | Situação: {aluno['situacao']}")

    elif opcao == "3":
        print("\n--- BUSCAR ALUNO ---")
        if not alunos:
            print("Nenhum aluno cadastrado no sistema ainda.")
        else:
            matricula_busca = input("Digite a matrícula: ")
            encontrado = False

            for aluno in alunos:
                if aluno["matricula"] == matricula_busca:
                    print(f"\n[Aluno Encontrado]")
                    print(f"Nome: {aluno['nome']}")
                    print(f"Notas: {aluno['notas']}")
                    print(f"Média: {aluno['media']:.2f}")
                    print(f"Situação: {aluno['situacao']}")
                    encontrado = True
                    break
            
            if not encontrado:
                print("Aluno não encontrado com essa matrícula.")

    elif opcao == "4":
        print("\n--- ALUNOS APROVADOS ---")
        aprovados = [a for a in alunos if a["situacao"] == "Aprovado"]
        if not aprovados:
            print("Nenhum aluno aprovado até o momento.")
        else:
            for aluno in aprovados:
                print(f"Nome: {aluno['nome']} - Média: {aluno['media']:.2f}")

    elif opcao == "5":
        print("\n--- ALUNOS EM RECUPERAÇÃO ---")
        recuperacao = [a for a in alunos if a["situacao"] == "Recuperação"]
        if not recuperacao:
            print("Nenhum aluno em recuperação até o momento.")
        else:
            for aluno in recuperacao:
                print(f"Nome: {aluno['nome']} - Média: {aluno['media']:.2f}")

    elif opcao == "6":
        print("\n--- ALUNOS REPROVADOS ---")
        reprovados = [a for a in alunos if a["situacao"] == "Reprovado"]
        if not reprovados:
            print("Nenhum aluno reprovado até o momento.")
        else:
            for aluno in reprovados:
                print(f"Nome: {aluno['nome']} - Média: {aluno['media']:.2f}")

    elif opcao == "7":
        print("\nSaindo do sistema... Até logo!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")