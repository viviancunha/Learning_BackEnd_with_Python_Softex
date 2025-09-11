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
    

