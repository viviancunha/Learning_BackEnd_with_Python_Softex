matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]] # Matriz 3x3. Cada linha representa uma sublista. Isso é o que chamamos de matriz tridimensional. Para uso prático, é recomendável ir só até a 3a lista.

print(matriz[1][1]) # Acessa o elemento na segunda linha e segunda coluna. Vai imprimir 5.

tridimensional = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  [[1, 2, 3], [4, 5, 9], [7, 8, 9]]] # Matriz 3x3x3. Cada linha representa uma lista, e cada lista contém outras sublistas. Isso é o que chamamos de matriz tridimensional.

print(tridimensional[1][1][2]) # Acessa o elemento na segunda lista, segunda linha e terceira coluna. Vai imprimir 6.
                
 
