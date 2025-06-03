def criar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = { "descricao": descricao, "concluida": False }
    tarefas.append(tarefa)
    print("Tarefa criada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    
    print("=== Lista de Tarefas ===")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['descricao']:30}  [{status}]")



   