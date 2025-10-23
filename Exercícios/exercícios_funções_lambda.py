# Dada a lista [1, 2, 3, 4, 5], use map com lambda para gerar uma nova lista com o dobro de cada número.

num = [1, 2, 3, 4, 5]
dobro = list(map(lambda x: x * 2, num))
print(dobro)  

# Dada a lista [10, 15, 20, 25, 30], use filter com lambda para obter apenas os números pares.

num = [10, 15, 20, 25, 30]
pares = list(filter(lambda x: x % 2 == 0, num))
print(pares)

# Usando reduce, some todos os números da lista [1, 2, 3, 4, 5].

from functools import reduce
num = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, num)
print(soma)

# Dada a lista ["uva", "banana", "maçã", "laranja"], ordene as palavras pelo tamanho usando sorted e lambda.

frutas = ["uva", "banana", "maçã", "laranja"]
ordenadas = sorted(frutas, key=lambda x: len(x))
print(ordenadas)

# Dada a lista ["ana", "pedro", "maria"], use map e lambda para transformar em ["Ana", "Pedro", "Maria"].

nomes = ["ana", "pedro", "maria"]
capitalizados = list(map(lambda x: x.capitalize(), nomes))
print(capitalizados)

# Usando reduce, calcule o produto (multiplicação) de todos os elementos da lista [2, 3, 4, 5].

from functools import reduce
num = [2, 3, 4, 5]
produto = reduce(lambda x, y: x * y, num)
print(produto)

# Dada a lista ["banana", "uva", "maçã", "laranja"], ordene as palavras pelo último caractere.

frutas = ["banana", "uva", "maçã", "laranja"]
ordenadas_ultimo = sorted(frutas, key=lambda x: x[-1])
print(ordenadas_ultimo)