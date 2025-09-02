# 01. Crie um dicionário simples. 
# Crie um dicionário chamado "aluno" com as chaves: "nome", "idade" e "nota", e preencha com valores fictícios.

aluno = {'nome':'Vívian', 'idade':26, 'nota':10.0}
print(aluno)

# 02. Acessando valores.
# Dado o dicionário: produto = {'nome':'caneta', 'preço':2.5, 'estoque':100}, imprima o nome do produto e a quantidade em estoque.

produto = {'nome':'caneta', 'preço':2.5, 'estoque':100}
print(produto['nome'], produto['estoque'])

# 03. Adicionando novos pares chave-valor.
# Dado o dicionário: pessoa = {'nome':'Carlos', 'idade':30}, adicione uma nova chave "cidade" com o valor "São Paulo".

pessoa = {'nome':'Carlos', 'idade':30}
pessoa['cidade'] = 'São Paulo'
print(pessoa)

# 04. Removendo elementos.
# Dado o dicionário: carro = {'marca': 'Ford', 'modelo': 'Fiesta', 'ano': 2010}, remova a chave "ano" do dicionário.

carro = {'marca': 'Ford', 'modelo': 'Fiesta', 'ano': 2010}
carro.pop('ano')
print(carro)


# 05. Verificando existência de uma chave.
# Verifique se a chave "telefone" existe no dicionário: contato = {'nome':'Ana', 'email':'ana@email.com'}.

contato = {'nome':'Ana', 'email':'ana@email.com'}
print('telefone' in contato) # Assim retorna False

# 06. Contando frequência de palavras.
# Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra. 

palavras = ['maçã', 'banana', 'laranja', 'banana', 'maçã']

def qtdd_palavras(palavras): 
    contagem = {}
    for fruta in palavras:
        if fruta in contagem:
            contagem[fruta] += 1
        else:
            contagem[fruta] = 1
    return contagem 
    
frequencia = qtdd_palavras(palavras)
print(frequencia)

# 07. Invertendo um dicionário.
# Dado o dicionário: d = {'a':1, 'b':2, 'c':3} 
# Crie um novo dicionário invertendo as chaves e os valores: {1:'a', 2:'b', 3:'c'}

d = {'a':1, 'b':2, 'c':3}
d_invertido = {valor: chave for chave, valor in d.items()}
print(d_invertido)

# 08. Dicionário com listas
# Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.

notas = {'Vívian': [10, 10, 10], 'Natalia': [9, 9, 9], 'Aryella': [8, 8, 8]}
for aluna in notas:
    média_aluna = sum(notas[aluna]) / len(notas[aluna])
    print(f'Média de {aluna}: {média_aluna}')

# 09. Mesclando dois dicionários
# Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.

dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}

def mesclar_dicionarios(d1, d2):
    d3 = d1.copy()
    d3.update(d2)
    return d3

resultado = mesclar_dicionarios(dic1, dic2)
print(resultado)

# 10. Ordenando dicionário por valor
# Dado o dicionário: pontuações = {'João':50, 'Maria':80, 'Pedro':70}
# Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.

pontuações = {'João':50, 'Maria':80, 'Pedro':70}

for jogador, pontos in sorted(pontuações.items(), key=lambda item: item[1], reverse=True):
    print(f'{jogador}: {pontos}')