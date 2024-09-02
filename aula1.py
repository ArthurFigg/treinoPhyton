tarefas = ["tomar banho", "passear com cachorro", "Leitura diaria"]

def menu():
    """Exibe o menu de opções para o usuário e processa a escolha."""
    while True:
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            listar_tarefas()
        elif escolha == "3":
            concluir_tarefa()
        elif escolha == "4":
            remover_tarefa()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

def adicionar_tarefa():
    """Adiciona uma nova tarefa à lista."""
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    """Lista todas as tarefas."""
    if len(tarefas) == 0:
        print("Não há tarefas na lista.")
    else:
        print("Tarefas na lista:")
        for tarefa in tarefas:
            print("- " + tarefa)

def concluir_tarefa():
    """Marca uma tarefa como concluída."""
    tarefa = input("Digite a tarefa a ser concluída: ")
    if tarefa in tarefas:
        indice = tarefas.index(tarefa)
        tarefas[indice] = "[feito] " + tarefa
        print(f"Tarefa '{tarefa}' marcada como concluída.")
    else:
        print("Tarefa não encontrada.")
        
def remover_tarefa():
            """Remove uma tarefa da lista"""
            tarefa = input("Digite a tarefa a ser removida: ")
            if tarefa in tarefas:
                tarefas.remove(tarefa)
                print("Tarefa removida com sucesso!")
            elif "[feito] " + tarefa in tarefas:
                tarefas.remove("[feito] " + tarefa)
                print("Tarefa concluída removida com sucesso!")
            else:
                print("Tarefa não encontrada.")

# Inicia o programa
listar_tarefas()
menu()
