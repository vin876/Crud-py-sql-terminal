from models import adicionar_tarefa, listar_tarefas, atualizar_tarefa, deletar_tarefa

def menu():
    while True:
        print("\n===== GERENCIADOR DE TAREFAS =====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Atualizar status")
        print("4 - Deletar tarefa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            adicionar_tarefa(titulo, descricao)
        elif opcao == "2":
            tarefas = listar_tarefas()
            for t in tarefas:
                print(f"{t[0]} - {t[1]} | {t[2]} | Status: {t[3]}")
        elif opcao == "3":
            id = int(input("ID da tarefa: "))
            status = input("Novo status (pendente, em andamento, concluída): ")
            atualizar_tarefa(id, status)
        elif opcao == "4":
            id = int(input("ID da tarefa a deletar: "))
            deletar_tarefa(id)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

menu()
