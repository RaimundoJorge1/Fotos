import sqlite3

conn = sqlite3.connect('comunidade.db')
cursor = conn.cursor()

id= 12

# excluindo um registro da tabela
cursor.execute("""
DELETE FROM foto
WHERE id = ?
""", (id,))

conn.commit()

print('Registro excluido com sucesso.')

conn.close()