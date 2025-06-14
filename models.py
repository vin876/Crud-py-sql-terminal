from database import conectar

def adicionar_tarefas(titulo, descrição):
    conn= conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO tarefas (titulo, descricao) VALUES (%s, %s)"
    cursor.execute(sql, (titulo, descricao))
    conn.commit()
    conn.close()

def listar_tarefas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas

def atualizar_tarefas(id, novo_status):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPTADE tarefas SET status = %s WHERE id = %s"
    cursor.execute(sql, (novo_status, id))
    conn.commit()
    conn.close()

def deletar_tarefa(id):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM tarefas WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    conn.close()
   
