# Exemplo de conexão MySQL com variáveis de ambiente

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
