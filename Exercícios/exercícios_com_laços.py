# 01. Use for para imprimir os números de 1 a 10

for i in range(1, 11): # range(1, 11) gera números de 1 a 10, porque o último número é excluído. Só considera o primeiro número até o 10-1.
    print(i)

# 02. Tabuada. Pedir um número ao usuário e imprimir a tabuada desse número (de 1 a 10).

num = int(input('Digite um número e descubra a tabuada dele: ' )) # Não usei float dessa vez, porque a tabuada é feita com números inteiros.

for i in range(1, 11):
    print(str(num) + ' x ' + str(i) + ' = ' + str(num * i))

# 03. Somatória com while. Ler números até o usuário digitar 0. Mostrar a soma dos números digitados.

soma = 0
num = int(input('Digite um número para somar (0 para sair): ')) 

while num != 0:  # O comando que eu estou dando é "enquanto o número for diferente de 0, continue somando".
    soma += num  # Soma o número digitado ao total.
    print('Soma até agora: ' + str(soma))  # Mostra a soma atual.
    num = int(input('Digite um número para somar (0 para sair): '))  # Pede outro número.  

          