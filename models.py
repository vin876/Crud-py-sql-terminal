from database import conectar

def adicionar_tarefas(titulo, descrição):
  conn= conectar()
  cursor = conn.cursor()
  sql = "INSERT INTO tarefas (titulo, descricao) VALUES (%s, %s)"
  cursor.execute(sql, (titulo, descricao))
  conn.commit()
  conn.close()
