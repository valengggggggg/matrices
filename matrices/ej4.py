def encontrar_maximo(matriz):

    maximo = float('-inf')
    
    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento
                
    return maximo

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

maximo = encontrar_maximo(matriz)
print("El elemento máximo en la matriz es:", maximo)
