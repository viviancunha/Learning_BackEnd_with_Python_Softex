import sqlite3

conexao = sqlite3.connect("escola_v2.db")
cursor = conexao.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

print("Tabelas existentes no banco:")
for tabela in tabelas:
    print(tabela[0])

conexao.close()





