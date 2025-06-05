import textwrap
from datetime import datetime
from modulos.tarefas import criar_tarefa, listar_tarefas, editar_tarefa,excluir_tarefa, marcar_concluido
from modulos.manipulaJSON import carregar_tarefas

tarefas = carregar_tarefas()

def getMenu():
    hora_atual = datetime.now().strftime("%d-%m-%Y %H:%M")
    
    menu = f'''
    ===={hora_atual}====
    ==========MENU==========

    [1]\tCRIAR TAREFA
    [2]\tLISTAR TAREFAS
    [3]\tEDITAR TAREFA
    [4]\tEXCLUIR TAFEFA
    [5]\tMARCAR TAREFA COMO CONCLUÍDA
    [0]\tSALVAR E SAIR 

    ========================
    Digite a opção desejada:
    '''
    return int(input(textwrap.dedent(menu)))

def main():
    while True:
        option = getMenu()

        if option == 1:
            print("== Criando uma nova tarefa ==")
            criar_tarefa(tarefas)

        elif option == 2:
            print("== Listando as tarefas ==")
            listar_tarefas(tarefas)

        elif option == 3:
            print("== Editando uma tarefa ==")
            editar_tarefa(tarefas)

        elif option == 4:
            print("== Excluindo uma tarefa ==")
            excluir_tarefa(tarefas)

        elif option == 5:
            print("== Marcando tarefa como concluída ==")
            marcar_concluido(tarefas)

        elif option == 0:
            print("== Salvando e saindo do Sistema ==")
            break

        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()