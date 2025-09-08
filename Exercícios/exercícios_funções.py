# 01. Crie uma função chamada saudacao que imprime na tela a mensagem "Olá, bem-vindo ao Python!". Em seguida, chame a função no programa.

def saudacao():
    print('Olá, bem-vindo ao Python!')

saudacao()

# 02. Crie uma função chamada dobro que recebe um número como parâmetro e retorna o dobro desse número. Teste chamando a função com diferentes valores.

def dobro(numero):
    return numero*2

print(dobro(2)) 
print(dobro(15))
print(dobro(-1))
print(dobro(0))

# 03. Crie uma função chamada soma que receba dois números e retorne a soma deles. Depois, use a função para somar 10 + 20.

def soma(num1, num2):
    return num1 + num2

print(soma(10, 20))

# 04. Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem: "Olá, [nome]!". Caso o nome não seja informado, mostre "Olá, visitante!".

def mensagem(nome='visitante'):
    nome = input('Digite seu nome: ')
    if nome == '':
        print('Olá, visitante!')
    else:
        print(f'Olá, {nome}!')

mensagem()

# 05. Crie uma função chamada operacoes que receba dois números e retorne a soma, a subtração e a multiplicação deles.

def operacoes(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    return soma, subtracao, multiplicacao

resultado = operacoes(2, 7)
print(resultado)

# 06. Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. Teste com 3, 5 e 7 valores diferentes.

def media(*nums):
    return sum(nums) / len(nums)

média = media(1, 5, 7)
print(média)
média = media(8, 12, 37, 29, 13)
print(média)
média = media(4, 6, 8, 10, 12, 14, 16)
print(média)

# 07. Crie uma função chamada dados_pessoais que receba informações de uma pessoa (nome, idade, cidade, etc.) usando **kwargs e imprima cada dado em uma linha. Exemplo de chamada: dados_pessoais(nome="Ana", idade=25, cidade="Recife").

def dados_cadastrais(**kwdados):
    for chave, valor in kwdados.items():
        print(f'{chave}: {valor}'   )

dados_cadastrais(
    nome=input('Digite o seu nome: '),
    idade=input('Informe a sua idade: '),
    cidade=input('Indique a sua cidade natal: ')
)

# 08. Crie uma função chamada calculadora que tenha dentro dela outras funções (somar, subtrair, multiplicar, dividir). A função principal deve permitir escolher a operação e retornar o resultado.

def calculadora():
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        if b != 0:
            return a / b
        else:
            return 'Erro: A divisão de qualquer número por zero é inexistente.'

    print("Menu Calculadora: escolha a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    escolha = input('Digite o número da operação, sendo 1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão: ')
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    if escolha == '1':
        print(f'Resultado: {somar(num1, num2)}')
    elif escolha == '2':
        print(f'Resultado: {subtrair(num1, num2)}')
    elif escolha == '3':
        print(f'Resultado: {multiplicar(num1, num2)}')
    elif escolha == '4':
        print(f'Resultado: {dividir(num1, num2)}')
    else:
        print("Operação inválida.")

calculadora()

# 09. Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros. A função deve aplicar a operação recebida (ex: soma, multiplicação). Exemplo:
# def soma(a, b): return a + b
# aplicar_operacao(3, 4, soma)

def aplicar_operacao(num1, num2, operacao):
    return operacao(num1, num2)
def soma(a, b):
    return a + b
def multiplicacao(a, b):
    return a * b
def subtracao(a, b):
    return a - b
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return 'Erro: A divisão de qualquer número por zero é inexistente.'

print(aplicar_operacao(3, 4, soma))
print(aplicar_operacao(3, 4, multiplicacao))
print(aplicar_operacao(3, 4, subtracao))
print(aplicar_operacao(9, 3, divisao))