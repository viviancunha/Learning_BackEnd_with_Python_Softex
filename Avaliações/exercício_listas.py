# Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.

livros = ['Harry Potter e a Pedra Filosofal', 'Crepúsculo', 'A Mulher que Mudou Minha Vida']
print(livros)

# Usando a lista livros, exiba apenas o primeiro e o último elemento.

print(livros[0])
print(livros[-1])   

# Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.

livros.append('Jogos Vorazes')
livros.append('Esse Nosso Jeito Bélico de Viver')
print(livros) 

# Insira o livro "Duna" na segunda posição da lista livros usando insert().

livros.insert(1, 'Duna')
print(livros)

# Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".

if 'Silêncio dos Inocentes' in livros:
    livros.remove('Silêncio dos Inocentes')
    print('Livro removido')
else:
    print('Livro não encontrado.')

# Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.

num = [1, 2, 3, 2, 4, 2, 5]
print(num.count(2))

# Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"

for i in livros:
    print(f'O livro {i} é interessante.')

# Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.

idades = [12, 18, 25, 14, 30]
for i in idades:
    if i >= 18:
        print(i)

# Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.

valores = [10, 20, 30, 40]
soma = 0
for i in valores:
    soma += i
print(soma)

# Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
# notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.

nota_av1 = float(input('Nota 1ª Avaliação: '))
nota_av2 = float(input('Nota 2ª Avaliação: '))
nota_av3 = float(input('Nota 3ª Avaliação: '))

notas_aluno1 = [[nota_av1, nota_av2, nota_av3]]

nota_av1 = float(input('Nota 1ª Avaliação: '))
nota_av2 = float(input('Nota 2ª Avaliação: '))
nota_av3 = float(input('Nota 3ª Avaliação: '))

notas_aluno2 = [[nota_av1, nota_av2, nota_av3]]

notas = [notas_aluno1, notas_aluno2]

for i in notas:
    media = sum(notas_aluno1[0]) / len(notas_aluno2[0])
    print(f'Média do aluno: {media}')

# Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:
# [ ] - para posições vazias
# tor - para a torre
# cav - para o cavalo
# bis - para o bispo
# rai - para a rainha
# rei - para o rei
# pea - para o peão
# Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra. (Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)

import numpy as np
tabuleiro = [['tor', 'cav', 'bis', 'rai', 'rei', 'bis', 'cav', 'tor'],
             ['pea', 'pea', 'pea', 'pea', 'pea', 'pea', 'pea', 'pea'],
             ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
             ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
             ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
             ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
             ['pea', 'pea', 'pea', 'pea', 'pea', 'pea', 'pea', 'pea'],
             ['tor', 'cav', 'bis', 'rei', 'rai', 'bis', 'cav', 'tor']]
print(np.array(tabuleiro))
