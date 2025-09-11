# 01. Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.

while True:
    num = input("Digite um número inteiro: ")
    try:
        inteiro = int(num)
        print(f"Você digitou o número inteiro: {inteiro}")
        break
    except ValueError:
        try:
            decimal_para_inteiro = int(float(num))
            print('Você digitou um número decimal. Nós convertemos para inteiro:', decimal_para_inteiro)
        except ValueError:
            print('Dado inválido. Por favor, digite um número inteiro.\n Tente novamente.') # Para o caso de o usuário inserir uma letra, por exemplo.

# 02. Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.

while True:
    print('Calculadora de multiplicação')
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    try:
        resultado = float(num1) * float(num2)
        print('O resultado da multiplicação é:', resultado)
        break
    except ValueError:
        print('Dado inválido. Por favor, digite apenas números.\n Tente novamente.')

# 03. Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.

while True:
    num = input('Digite um número inteiro: ')
    try:
        inteiro = int(num)
    except ValueError:
        print('Dado inválido. Por favor, digite um número inteiro.\n Tente novamente.')
    else:
        print(f'Você digitou o número inteiro: {inteiro}')
        break

# 04. Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.

try:
    arquivo = open('dados.txt', 'r')
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print('Arquivo não encontrado.')
finally:
    print('Encerrando programa.')
    try:
        arquivo.close()
    except NameError:
        pass  # Se o arquivo não foi aberto, então não há nada para fechar.    

# 05. Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. Caso contrário, retorne o resultado da divisão.

def divisão(a, b):
    if b == 0:
        raise ZeroDivisionError('Divisão por zero não é permitida.')
    return a / b

while True:
    a = input('Digite o dividendo: ')
    b = input('Digite o divisor: ')
    try:
        resultado = divisão(float(a), float(b))
        print('Resultado:', resultado)
        break
    except ValueError:
        print('Dado inválido. Por favor, digite apenas números.\n Tente novamente.')
    except ZeroDivisionError as resultado:
        print(resultado)

# 06. Crie uma exceção personalizada chamada IdadeInvalidaError. Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.

class IdadeInvalidaError(Exception):
    pass

def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("Não existe idade negativa.")
    
    print(f"Idade cadastrada com sucesso: {idade} anos.")

try:
    cadastrar_idade(-5)
except IdadeInvalidaError as e:
    print(f"Erro: {e}")

print("-" * 30)

try:
    cadastrar_idade(25)
except IdadeInvalidaError as e:
    print(f"Erro: {e}")

# 07. Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro: ValueError se o usuário digitar algo inválido; ZeroDivisionError se tentar dividir por zero

while True:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    try:
        resultado = float(num1) / float(num2)
        print(f"Resultado da divisão: {resultado}")
        break
    except ValueError:
        print("Erro: Por favor, digite apenas números.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    print("Tente novamente.\n")

# 08. Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use: try para a conversão, else para verificar se é par ou ímpar; finally para exibir "Fim do programa"

while True:
    num = input("Digite um número inteiro: ")
    try:
        inteiro = int(num)
    except ValueError:
        print("Erro: Por favor, digite um número inteiro.")
    else:
        if inteiro % 2 == 0:
            print(f"O número {inteiro} é par.")
        else:
            print(f"O número {inteiro} é ímpar.")
        break
    finally:
        print("Fim do programa.\n")

# 09. Crie uma função sacar(saldo, valor) que: Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo. Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.

class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente.")
    return saldo - valor
try:
    saldo_atual = 1000
    valor_saque = float(input("Digite o valor a sacar: "))
    novo_saldo = sacar(saldo_atual, valor_saque)
    print(f"Saque realizado com sucesso. Novo saldo: {novo_saldo}")
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")
except ValueError:
    print("Erro: Por favor, digite um valor numérico válido.")
    