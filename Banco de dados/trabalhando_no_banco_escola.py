# Mostre todos os registros da tabela Aluno. 
# (Use SELECT e FROM)

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT * FROM Aluno;")

registros_alunos = cursor.fetchall()

for aluno in registros_alunos:
    print(aluno)

conexao.close()

# Exiba apenas o nome e a nota1 de todos os alunos.
# (Use SELECT com colunas específicas)

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT nome, nota1 FROM Aluno;")

registros_notas = cursor.fetchall()

for registro in registros_notas:
    print(registro)

conexao.close()

# Liste todos os alunos cuja nota2 seja maior que 8.
# (Use WHERE)

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT * FROM Aluno WHERE nota2 > 8;")

registros_nota2 = cursor.fetchall()

for aluno in registros_nota2:
    print(aluno)

conexao.close()

# Mostre os alunos que nasceram após o ano de 2000.
# (Use WHERE com data)

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT * FROM Aluno WHERE data_nascimento > '2000-12-31';")

registros_nascimento = cursor.fetchall()

for aluno in registros_nascimento:
    print(aluno)

conexao.close()

# Exiba o nome e a mensalidade de todos os cursos que custam mais de 600 reais.
# (Use WHERE com condição numérica)

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT nome, mensalidade FROM Curso WHERE mensalidade > 600;")

registros_cursos = cursor.fetchall()

for curso in registros_cursos:
    print(curso)

conexao.close()

# Mostre o nome das turmas e o ano correspondente, ordenados pelo ano em ordem crescente.
# (Use ORDER BY)

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT nome, ano FROM Turma ORDER BY ano ASC;")

registros_turmas = cursor.fetchall()

for turma in registros_turmas:
    print(turma)

conexao.close()

# Liste o ano das turmas e a quantidade de turmas por ano.
# (Use GROUP BY)

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT ano, COUNT(*) FROM Turma GROUP BY ano;")

registros_agrupados = cursor.fetchall()

for registro in registros_agrupados:
    print(registro)

conexao.close()

# Calcule a média da nota1 dos alunos por turma_id.
# (Use GROUP BY com função de agregação)

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT id_turma, AVG(nota1) FROM Aluno GROUP BY id_turma;")

registros_media = cursor.fetchall()
for registro in registros_media:
    print(registro)

conexao.close()

# Mostre o ano e a quantidade de turmas apenas para os anos que têm mais de 2 turmas.
# (Use GROUP BY e HAVING)

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT ano, COUNT(*) FROM Turma GROUP BY ano HAVING COUNT(*) > 2;")

registros_having = cursor.fetchall()

for registro in registros_having:
    print(registro)

conexao.close()

# Exiba o nome dos cursos e suas mensalidades, ordenando primeiro pela mensalidade (decrescente).
# (Use ORDER BY)

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT nome, mensalidade FROM Curso ORDER BY mensalidade DESC;")

registros_cursos_ordenados = cursor.fetchall()

for curso in registros_cursos_ordenados:
    print(curso)

conexao.close()

# -------------------------------- FIM! ---------------------------------