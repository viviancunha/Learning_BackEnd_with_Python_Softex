"""
IF = condição
ELIF = se não, se (Outra condição. Pode ter vários.)
ELSE = se não
A indentação (o espaço entre as condicionais) é importante para o Python entender o bloco de código. O PEP8 recomenda 4 espaços.

"""

x = 5
y = 's'

if x == 5 and y == 's':
    print('É verdade esse bilhete!') 
else:
    print('É mentira esse bilhete!')

print(False or True)

# Ex.: 

Idade = int(input('Digite a sua idade: '))
Habilitação = input('Você já possui habilitação? (sim/não): ')
Álcool = input('Você já ingeriu álcool hoje? (sim/não): ')

if Idade >= 18 and Habilitação == 'sim' and Álcool == 'não':
    print('Você pode dirigir.')
else:
    print('Você não pode dirigir.')

"""

Condicionais em uma linha

Ação - Condição TRUE - ELSE - Ação

"""

# Ex.:

print('Você pode dirigir.' if Idade >= 18 and Habilitação == 'sim' and Álcool == 'não' else 'Você não pode dirigir.')