# Importe o módulo sqlite3 e faça a conexão com o banco de dados escola_v2.db

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

# Faça a query para pegar toda a tabela alunos e imprima na tela. 

cursor = conexao.cursor()
cursor.execute("SELECT * FROM Aluno")
alunos = cursor.fetchall()
for aluno in alunos:
    print(aluno)

conexao.close()

# Obtenha a média entre nota1 e nota2 dos alunos, ordene em ordem decrescente e retorne apenas as 10 maiores notas. No fim, imprima na tela a lista desses alunos e suas médias. 

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT nome, (nota1 + nota2) / 2 AS media FROM Aluno ORDER BY media DESC LIMIT 10")
alunos = cursor.fetchall()
for aluno in alunos:
    print(aluno)

conexao.close()

# Use Left Join com as tabelas Aluno e Turma e imprima todos os dados da tabela. 

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT Aluno.nome, Aluno.nota1, Aluno.nota2, Turma.nome AS turma FROM Aluno LEFT JOIN Turma ON Aluno.id_turma = Turma.id")
alunos = cursor.fetchall()
for aluno in alunos:
    print(aluno)

conexao.close()

# Usando a query da questão 4, adicione um filtro para pegar apenas os alunos da turma 2 e imprima na tela. 

import sqlite3
conexao = sqlite3.connect("Banco de dados/escola_v2.db")

cursor = conexao.cursor()
cursor.execute("SELECT Aluno.nome, Aluno.nota1, Aluno.nota2, Turma.nome AS turma FROM Aluno LEFT JOIN Turma ON Aluno.id_turma = Turma.id WHERE Turma.id = 2")
alunos = cursor.fetchall()
for aluno in alunos:
    print(aluno)

conexao.close()

# --------------------------------FIM!---------------------------------