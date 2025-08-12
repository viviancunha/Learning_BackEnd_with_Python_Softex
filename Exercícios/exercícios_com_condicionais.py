# 01. Par ou Ímpar
# Peça para o aluno digitar um número. O programa deve dizer se é par ou ímpar.

numero = float(input('Digite um número: '))
if numero % 2 == 0:
    print('O número', numero, 'é par.')
else:
    print('O número', numero, 'é ímpar.')

# 02. Aprovação escolar
# Ler a nota de um aluno. Mostrar:
# "Aprovado" se a nota >= 7
# "Recuperação" se a nota estiver entre 5 e 6.9
# "Reprovado" se for < 5

Nota_Aluno = float(input('Digite a nota do aluno: '))

if Nota_Aluno >= 7:
    print('Aprovado')
elif 5 <= Nota_Aluno < 7:
    print('Recuperação')
else:
    print('Reprovado')

# 03. Comparação de números
# Mostrar qual é o maior ou se são iguais.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print('O maior número é', num1)
elif num2 > num1:
    print('O maior número é', num2)
else:
    print('Os números são iguais.')

# 04. Classificação de idade
# Ler a idade e dizer:
# "Criança" até 12 anos
# "Adolescente" de 13 a 17 anos
# "Adulto" de 18 a 64 anos
# "Idoso" 65 ou mais

idade = int(input('Digite a sua idade em anos: '))

if idade <= 12:
    print('Você é criança.')
elif 13 <= idade <= 17:
    print('Você é adolescente.')
elif 18 <= idade <= 64:
    print('Você é adulto.')
else:
    print('Você é idoso.')

