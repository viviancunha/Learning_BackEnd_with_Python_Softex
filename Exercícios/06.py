# 06. Operações básicas
# Crie um script que mostre o resultado das operações abaixo usando duas variáveis. Ex.: a = 10 e b = 3.

a = 10
b = 3

print(a+b)  # Adição
print(a-b)  # Subtração
print(a*b)  # Multiplicação
print(a/b)  # Divisão (resultado em ponto flutuante ou float)
print(a//b) # Divisão inteira (ou por inteiro)
print(a%b)  # Módulo (resto da divisão)
print(a**b) # Exponenciação (potência)

# 07. Calculadora simples
# Crie um programa que receba dois números digitados pelo usuário com input() e mostre o resultado das quatro operações básicas. 
# Nota @viviancunha: Usar scrum para facilitar (fluxo).
# Nota @viviancunha 02: input() SEMPRE retorna uma string, então no caso do exercício é necessário converter para int ou float. **E se eu quiser que a máquina identifique o tipo do número?**
# Nota @viviancunha 03: INT é inflexível, enquanto FLOAT é maleável. Se eu não sei que tipo de número o usuário vai inserir no INPUT, é melhor pedir que o INPUT leia como FLOAT, porque vai aceitar os dois tipos de número. 

# - Receber o número do usuário.

num1 = float(input("Digite o primeiro número: "))  
num2 = float(input("Digite o segundo número: "))

# - Realizar as operações.

Soma = num1 + num2 
Subtracao = num1 - num2
Multiplicacao = num1 * num2
Divisao = num1 / num2 

# - Mostrar os resultados.

print('Resultados:')
print('Adição:', str(Soma), "\n"'Subtração:', str(Subtracao), "\n"'Multiplicação:', str(Multiplicacao), "\n"'Divisão:', str(Divisao))

# Nota @viviancunha 04: **Respondendo a minha dúvida anterior**, se eu quiser que a máquina identifique o tipo do número, posso usar o try/except para tentar converter o input em int ou float. Ex.:

# - Receber o número do usuário.

num1 = input('Digite o primeiro número: ')

try:
    num1 = int(num1)
    print('Este é um número inteiro.')
except ValueError:
    try: 
        num1 = float(num1)
        print('Este é um número flutuante (possui casas decimais).')
    except ValueError:
        print('Não é um número válido.')
    

num2 = input('Digite o segundo número: ')  

try:
    num2 = int(num2)
    print('Este é um número inteiro.')
except ValueError:
    try: 
        num2 = float(num2)
        print('Este é um número flutuante (possui casas decimais).')
    except ValueError:
        print('Não é um número válido.')

# - Realizar as operações.

Soma = num1 + num2 
Subtracao = num1 - num2
Multiplicacao = num1 * num2
Divisao = num1 / num2 

# - Mostrar os resultados.

print('Resultados:')
print('Adição:', str(Soma), "\n"'Subtração:', str(Subtracao), "\n"'Multiplicação:', str(Multiplicacao), "\n"'Divisão:', str(Divisao))



