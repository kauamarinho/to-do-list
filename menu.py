tarefas = []


def adicionar_tarefa():
    nome = input("Digite a nova tarefa: ")

    if nome:
        tarefas.append(nome)
        print(f"Tarefa '{nome}' adicionada com sucesso!")
    else:
        print("O nome da tarefa não pode estar vazio.")


def listar_tarefas():
    '''
    Mostra todas as tarefas cadastradas na lista.
    As tarefas são exibidas com uma numeração.
    '''

    if not tarefas:
        print("Sua lista de tarefas está vazia.")
    else:
        print("Lista de Tarefas")

        for indice, tarefa in enumerate(tarefas, 1):
            print(f"{indice}. {tarefa}")


def tarefa_concluida():
    '''
    Marca uma tarefa como concluída.
    O usuário escolhe a tarefa através do seu número.
    '''

    listar_tarefas()

    numero = int(input("Digite o número da tarefa concluída: "))

    tarefas[numero - 1] = "[Concluída] " + tarefas[numero - 1]

    print("Tarefa marcada como concluída!")


def remover_tarefa():
    listar_tarefas()

    numero = int(input("Digite o número da tarefa que deseja remover: "))

    if numero >= 1 and numero <= len(tarefas):
        tarefa_removida = tarefas.pop(numero - 1)
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
    else:
        print("Número de tarefa inválido.")


def menu():
    '''
    Menu de Opções
    '''

    while True:
        print("\n1 - Adicionar tarefa")
        print("2 - Lista de tarefas atual")
        print("3 - Marcar tarefa como concluída")
        print("4 - Remover tarefa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            tarefa_concluida()

        elif opcao == "4":
            remover_tarefa()

        elif opcao == "5":
            print("Lista Finalizada!")
            break

        else:
            print("Opção inválida, escolha de 1 a 5.")


menu()