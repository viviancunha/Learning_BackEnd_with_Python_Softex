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

palavras = {'maçã', 'banana', 'laranja', 'banana', 'maçã'}

def qtdd_palavras(palavras): 
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem