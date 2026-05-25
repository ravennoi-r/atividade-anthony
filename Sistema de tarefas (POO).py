class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.status = "pendente"

    def marcar_como_concluida(self):
        self.status = "concluída"

    def marcar_como_pendente(self):
        self.status = "pendente"

    def exibir(self):
        print("\n----------------")
        print(f"Título: {self.titulo}")
        print(f"Descrição: {self.descricao}")
        print(f"Status: {self.status}")


tarefas = []


while True:
    print("\n===== SISTEMA DE TAREFAS =====")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Listar tarefas pendentes")
    print("5 - Listar tarefas concluídas")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título da tarefa: ")
        descricao = input("Descrição da tarefa: ")

        tarefa = Tarefa(titulo, descricao)

        tarefas.append(tarefa)

        print("Tarefa cadastrada com sucesso!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for tarefa in tarefas:
                tarefa.exibir()

    elif opcao == "3":
        titulo = input("Digite o título da tarefa: ")

        encontrada = False

        for tarefa in tarefas:
            if tarefa.titulo == titulo:
                tarefa.marcar_como_concluida()
                print("Tarefa concluída!")
                encontrada = True

        if not encontrada:
            print("Tarefa não encontrada.")

    elif opcao == "4":
        print("\n===== TAREFAS PENDENTES =====")

        for tarefa in tarefas:
            if tarefa.status == "pendente":
                tarefa.exibir()

    elif opcao == "5":
        print("\n===== TAREFAS CONCLUÍDAS =====")

        for tarefa in tarefas:
            if tarefa.status == "concluída":
                tarefa.exibir()

    elif opcao == "6":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")