# Gerenciador de Tarefas com Python e MySQL

Projeto simples de CRUD com Python e MySQL.

## Tecnologias

- Python 3.7+
- MySQL Workbench 8.0 CE
- mysql-connector-python

🧠 Como o projeto funciona
Este projeto é um sistema de gerenciamento de tarefas usando Python e MySQL. Ele permite que você adicione, visualize, atualize e delete tarefas diretamente pelo terminal.

⚙️ Funcionamento passo a passo
Banco de Dados (MySQL)
O banco tarefas_db é criado com a tabela tarefas.
A tabela armazena: id, título, descrição, status, data de criação e data de atualização.
Conexão com o MySQL (database.py)

O Python se conecta ao MySQL usando mysql-connector-python.
As credenciais estão no arquivo database.py.

Funções CRUD (models.py)
adicionar_tarefa() → Insere uma nova tarefa.
listar_tarefas() → Mostra todas as tarefas do banco.
atualizar_tarefa() → Altera o status de uma tarefa.
deletar_tarefa() → Remove uma tarefa.
Interface via terminal (main.py)
Um menu interativo no terminal permite escolher as opções (adicionar, listar, atualizar ou deletar).
As funções do CRUD são chamadas conforme a opção do usuário.
