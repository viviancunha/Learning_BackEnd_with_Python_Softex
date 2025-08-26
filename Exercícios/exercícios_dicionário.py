# 01. Crie um dicionário vazio chamado cadastro e adicione os seguintes pares chave-valor:

cadastro = {}
cadastro['nome'] = 'Lucas'
cadastro['idade'] = 25
cadastro['email'] = 'lucas@email.com'
print(cadastro)

# 02. Usando o dicionário abaixo, use o método .get() para obter o valor da chave "telefone", retornando "Não informado" se a chave não existir.

cliente = {"nome": "Amanda", "idade": 31}
telefone = cliente.get("telefone")
if telefone is None:
    telefone = "Não informado"
print(telefone)

# 03. Utilize um laço for para imprimir todas as chaves do dicionário abaixo.
# livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}

livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}
for i in livro:
    print(i) # Vai imprimir só as chaves.

# OU:

livro = {"título": 1984, "autor": "George Orwell", "ano": 1949}
for i, valor in livro.items():
    print(f'{i} = {valor}') # Vai imprimir as chaves e os valores.

# 04. Adicione uma nova chave chamada "disponível" ao dicionário acima com o valor True.
# livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}

livro["disponível"] = True
print(livro)

# 05. Use o método .pop() para remover a chave "ano" do dicionário livro. Imprima o valor removido.

livro = {"título": 1984, "autor": "George Orwell", "ano": 1949}
ano = livro.pop("ano")
print(ano)

# 06. Crie um dicionário compras com pelo menos 3 itens (nome do produto como chave e preço como valor). Em seguida, use .values() para calcular o total da compra.

compras = {"produto1": 10.99, "produto2": 5.49, "produto3": 8.75}
total = sum(compras.values())
print(total)

# 07. Dado o dicionário: frutas = {"maçã": 3, "banana": 5, "laranja": 2}, imprima as frutas que têm mais de 2 unidades usando um laço for. 

frutas = {"maçã": 3, "banana": 5, "laranja": 2}
for fruta, valor in frutas.items():
    if valor > 2:
       print(fruta)

# Verifique se a chave "senha" está presente no dicionário abaixo. Se não estiver, adicione-a com o valor "123456".
# usuario = {"login": "joaosilva"}

usuario = {"login": "joaosilva"}
if "senha" is None:
    usuario["senha"] = "123456"

# 09. Use o método .items() para iterar sobre o dicionário abaixo e imprima frases como "A capital de SP é São Paulo".
# capitais = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Belo Horizonte"}

capitais = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Belo Horizonte"}
for estado, cidade in capitais.items():
    print(f'A capital de {estado} é {cidade}.')

# 10. Dado o dicionário abaixo, atualize o valor da chave "estoque" somando 10 unidades ao valor atual.
# produto = {"nome": "Teclado", "estoque": 15}

produto = {"nome": "Teclado", "estoque": 15}
produto["estoque"] += 10
print(produto)
