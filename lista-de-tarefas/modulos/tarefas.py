from modulos.manipulaJSON import salvar_tarefas, carregar_tarefas

def criar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ").strip()

    if descricao:
        tarefa = { "descricao": descricao, "concluida": False }
        tarefas.append(tarefa)
        salvar_tarefas(tarefas)
        print("Tarefa criada com sucesso!")
    else:
        print("Descrição da tarefa não pode ser vazia.")    

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    
    print("=== Lista de Tarefas ===")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['descricao']:30}  [{status}]")

def editar_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return 
    
    if len(tarefas) > 0:
        indice = int(input("Digite o número da tarefa que deseja editar: "))
        if 0 < indice <= len(tarefas):
            nova_descricao = input("Digite a nova descrição da tarefa: ").strip()
            if nova_descricao:
                tarefas[indice - 1]["descricao"] = nova_descricao
                salvar_tarefas(tarefas) 
                print("Tarefa editada com sucesso!")
            else:
                print("Descrição da tarefa não pode ser vazia.")
        else:
            print("Número de tarefa inválido.")
    
def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    if len(tarefas) > 0:
        indice = int(input("Digite o número da tarefa que deseja excluir: "))
        if 0 < indice <= len(tarefas):
            tarefas.pop(indice - 1)
            salvar_tarefas(tarefas)
            print("Tarefa excluída com sucesso")
        else:
            print("Número de tarefa inválido.")

def marcar_concluido(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    if len(tarefas) > 0:
        indice = int(input("Digite o número da tarefa que deseja concluir: "))
        if 0 < indice <= len(tarefas):
            tarefas[indice-1]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa marcada como concluída!")
        else:
            print("Número de tarefa inválido.")


    
