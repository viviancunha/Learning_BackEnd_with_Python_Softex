matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]] # Matriz 3x3. Cada linha representa uma sublista. Isso é o que chamamos de matriz tridimensional. Para uso prático, é recomendável ir só até a 3a lista.

print(matriz[1][1]) # Acessa o elemento na segunda linha e segunda coluna. Vai imprimir 5.

tridimensional = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  [[1, 2, 3], [4, 5, 9], [7, 8, 9]]] # Matriz 3x3x3. Cada linha representa uma lista, e cada lista contém outras sublistas. Isso é o que chamamos de matriz tridimensional.

print(tridimensional[1][1][2]) # Acessa o elemento na segunda lista, segunda linha e terceira coluna. Vai imprimir 6.
                
lista1 = []
for i in range (10):
    lista1.append(i) # Adiciona os números de 0 a 9 na lista1.

print(lista1) # Imprime a lista de 0 a 9.

lista2 = [i for i in range(10) if i % 2 == 0] # Cria uma lista com os números de 0 a 9, mas apenas os pares. A lista2 vai conter [0, 2, 4, 6, 8].
print(lista2) # Imprime a lista de números pares de 0 a 9. Dá pra criar listas de forma mais rápida e eficiente usando compreensão de listas, como mostrado aqui. Também é possível criar listas direto no terminal usando apenas print. O python aceita isso. Por exemplo, print([i for i in range(10)]) imprime a lista de 0 a 9 diretamente no terminal. A única diferença é que, como eu não atribuí a uma variável, não posso usar a lista depois. Mas é uma forma rápida de ver o resultado no terminal sem precisar criar uma variável para armazenar a lista.



