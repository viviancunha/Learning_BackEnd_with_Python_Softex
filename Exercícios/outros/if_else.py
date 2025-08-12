# IF = condição
# ELSE = se não

x = 5
y = 's'

if x == 9:
 print('É verdade esse bilhete!')
else:
 print('É mentira esse bilhete!')

print(False or True)

#################################

# Ex.: 

Idade = int(input('Digite a sua idade: '))
Habilitação = input('Você já possui habilitação? (sim/não): ')
Álcool = input('Você já ingeriu álcool hoje? (sim/não): ')

if Idade >= 18 and Habilitação == 'sim' and Álcool == 'não':
    print('Você pode dirigir.')
else:
    print('Você não pode dirigir.')
    