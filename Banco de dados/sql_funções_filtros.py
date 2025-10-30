# Mostre quantos alunos estão cadastrados na tabela Aluno. (Use a função COUNT).

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT COUNT(*) FROM Aluno")
resultado = cursor.fetchone()
print(f"Qtdd alunos cadastrados: {resultado[0]}")

conexao.close()

# Mostre a menor mensalidade entre todos os cursos cadastrados. (Use a função MIN).

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT MIN(mensalidade) FROM Curso")
resultado = cursor.fetchone()
print(f"Menor valor de mensalidade: {resultado[0]}")

conexao.close()

# Mostre a maior nota1 registrada entre todos os alunos. (Use a função MAX).

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT MAX(nota1) FROM Aluno")
resultado = cursor.fetchone()
print(f"Maior nota1 registrada: {resultado[0]}")

conexao.close()

# Calcule o valor total das mensalidades de todos os cursos. (Use a função SUM).

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT SUM(mensalidade) FROM Curso")
resultado = cursor.fetchone()
print(f"Valor total das mensalidades: {resultado[0]}")

conexao.close()

# Mostre a média geral da nota2 dos alunos. (Use a função AVG).

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT AVG(nota2) FROM Aluno")
resultado = cursor.fetchone()
print(f"Média geral nota2: {resultado[0]}")

conexao.close()

# ---------------------------------FIM!---------------------------------