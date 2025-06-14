# Exemplo de conexão MySQL com variáveis de ambiente

import mysql.connector

def conectar():
    return mysql.connector.connect(
        host("localhost"),
        username("**********"),
        password("**********"),
        database("tarefas_db")
    )
