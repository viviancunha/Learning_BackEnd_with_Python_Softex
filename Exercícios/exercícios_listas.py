# Crie uma lista que contenha diferentes tipos de dados (string, inteiro, outra lista…)

lista_mista = ['qq valor', 42, 3.14, True, [1, 2, 3], {'chave': 'outro valor'}] # O valor entre colchetes é uma lista, o valor entre chaves é um dicionário. Nesse caso, o dicionário está dentro da lista.
print(lista_mista)

# Usando a lista criada na questão anterior, use o método insert ou append para adicionar mais dois elementos a lista e use remove, pop ou del para remover um elemento da lista.

lista_mista.append('novo valor')  # Adiciona um novo valor ao final da lista
lista_mista.insert(2, 'valor no meio')  # Adiciona um valor na posição 2
print(lista_mista)  

lista_mista.remove(42)  # Remove o valor 42 da lista
lista_mista.pop()  # Remove o último elemento da lista
del lista_mista[1]  # Remove o elemento na posição 1
print(lista_mista)  

# Faça uma cópia da lista da questão anterior. Use a função id para verificar se realmente criou uma lista nova (obs: mesmo valor de ID indica que é o mesma lista e não uma nova)

lista_copia = lista_mista.copy()  # Cria uma cópia da lista
print(lista_copia)
print(id(lista_mista))  # ID da lista original
print(id(lista_copia))  # ID da lista copiada

# Crie uma nova lista só com números (inteiro e/ou ponto flutuante) e multiplique os elementos da lista por 5. O resultado deve ser uma nova lista com os elementos multiplicados.

lista_numeros = [1, 2, 3.5, 4, 5]  # Lista de números
lista_multiplicada = [num * 5 for num in lista_numeros]
print(lista_multiplicada)  # Exibe a nova lista com os elementos multiplicados

# Use o slice para criar uma nova lista que inclua apenas os elementos com índice 3 e 4 da lista a seguir: [ 1,2,3,4,5,6]. Resultado esperado: [4,5].

lista_original = [1, 2, 3, 4, 5, 6]  # Lista original
lista_slice = lista_original[3:5]  # Slice para obter os elementos com índice 3 e 4
print(lista_slice)  # Exibe a nova lista com os elementos selecionados
