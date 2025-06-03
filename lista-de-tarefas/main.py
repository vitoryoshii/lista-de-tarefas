from modulos.utilidades import getMenu
from modulos.tarefas import criar_tarefa, listar_tarefas
tarefas = []

while True:
    option = getMenu()

    if option == 1:
        print("== Criando uma nova tarefa ==")
        criar_tarefa(tarefas)

    elif option == 2:
        print("== Listando as tarefas ==")
        listar_tarefas(tarefas)

    elif option == 0:
        print("== Salvando e saindo do Sistema ==")
        break

    else:
        pass
