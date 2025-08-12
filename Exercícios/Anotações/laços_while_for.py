"""
Laço while

Laços são estruturas de repetição que permitem executar um bloco de código várias vezes, enquanto uma condição for verdadeira (while) ou para cada item em uma coleção (for).

"""
# Ex.:

x = 0

while x <= 5: 
    print('O valor de x é:', x)
    x += 1  # Vai incrementar x em 1 a cada iteração

# Ex2.:

while x < 5:
    x += 1
    if x == 3:
        continue # Pula o restante do loop quando x é 3
    print('O valor de x é:', x)

# Na prática:

while int(input('Digite um número: ')) != 0:
    print('Você digitou um número diferente de zero!')

"""
Laço for

O laço for é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string) ou um objeto iterável. Ele executa um bloco de código para cada item na sequência.

"""
# Ex.:

for i in range(5):  # range(5) gera uma sequência de números de 0 a 4. Range é um intervalo. Conta de 0 até o número especificado, mas não inclui o número final. Conta 5 itens. 
    print('O valor de i é:', i)

# Ex2.:

for i in range(1, 11):  # Começa em 1 e vai até 10. O número final não é incluído. Tem que especificar o número inicial e o final. O primeiro número é o inicial e o segundo é o final.
    if i % 2 == 0:  # Verifica se i é par
        print('O número', i, 'é par')
    else:
        print('O número', i, 'é ímpar')             

# in len 

w = 'Python'
len(w)  # len(w) retorna o tamanho da string w, que é 6
print('O tamanho da string w é:', len(w))  # Imprime o tamanho da string w  

# For com in range e len:

for i in range(len(w)):  # Itera sobre os índices da string w
    print('O caractere na posição', i, 'é:', w[i])  # Imprime o caractere na posição i da string w  

