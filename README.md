# Gerenciador de Tarefas com Python e MySQL

Projeto simples de CRUD com Python e MySQL.

## Tecnologias

- Python 3.7+
- MySQL Workbench 8.0 CE
- mysql-connector-python

## Como usar

1. Crie o banco e a tabela no MySQL com o script:
```sql
CREATE DATABASE tarefas_db;
USE tarefas_db;
CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    descricao TEXT,
    status VARCHAR(50) DEFAULT 'pendente'
);
