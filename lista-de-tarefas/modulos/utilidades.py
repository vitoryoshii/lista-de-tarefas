import textwrap
from datetime import datetime

def getHora():
    return datetime.now().strftime("%d-%m-%Y %H:%M")

def getMenu():
    hora_atual = getHora()
    
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
    '''
    return int(input(textwrap.dedent(menu)))