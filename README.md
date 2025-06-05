# 🚀 GERENCIADOR-DE-TAREFAS

### _📝 Lista de Tarefas via Terminal em Python_

Um projeto simples para gerenciar suas tarefas diretamente pelo terminal. Desenvolvido em **Python**, permite criar, listar, marcar como concluída e excluir tarefas, com os dados salvos localmente em um arquivo JSON.

---

## ✨ Funcionalidades

- 📋 **Adicionar Nova Tarefa**: Permite ao usuário inserir uma nova tarefa na lista.
- ✅ **Marcar Tarefa como Concluída**: O usuário pode marcar tarefas existentes como concluídas.
- 🗑️ **Remover Tarefas**: Funcionalidade para excluir tarefas da lista.
- 💾 **Persistência de Dados**: Salva e carrega tarefas de um arquivo `tarefas.json`, garantindo que os dados não sejam perdidos entre as sessões.
- 🖥️ **Interface de Terminal**: Interação totalmente via linha de comando, tornando-o leve e rápido.

---

## 💻 Tecnologias Utilizadas

- **Python**: Linguagem principal do desenvolvimento do projeto.
- **JSON**: Formato utilizado para o armazenamento local e persistência dos dados das tarefas.

---

## 🛠️ Como Usar

Siga os passos abaixo para configurar e executar o projeto:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/vitoryoshii/lista-de-tarefas.git
    ```

2.  **Navegue até a pasta principal do código do projeto:**
    Após clonar, entre no diretório raiz do repositório e, em seguida, na subpasta que contém o código principal:

    ```bash
    cd /lista-de-tarefas
    ```

3.  **Execute o programa:**
    ```bash
    python main.py
    ```

---

## 📂 Estrutura do Projeto

A estrutura de arquivos e pastas do repositório está organizada da seguinte forma:

GERENCIADOR-DE-TAREFAS/ <-- Raiz do repositório clonado
├── lista-de-tarefas/ <-- Contém o código fonte principal do projeto
│ ├── modulos/ # Módulos Python auxiliares
│ │ ├── pycache/ # Diretório de cache do Python (gerado automaticamente)
│ │ ├── manipulaJSON.py # Funções para lidar com a leitura e escrita no arquivo JSON
│ │ └── tarefas.py # Lógica de negócio para as operações de tarefas
│ ├── main.py # Ponto de entrada principal da aplicação
│ └── tarefas.json # Arquivo para armazenar os dados das tarefas (criado/usado pelo programa)
├── LICENSE # Arquivo contendo a licença do projeto (MIT)
└── README.md # Este arquivo de documentação

---

## 📜 Licença

Este projeto está licenciado sob a **Licença MIT**. Consulte o arquivo `LICENSE` na raiz do repositório para mais detalhes.

---

## ✒️ Autor

Desenvolvido por **Vitor Yoshii**.

---
