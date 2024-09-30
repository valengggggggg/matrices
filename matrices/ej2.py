def multiplicar_matrices(matriz_a, matriz_b):
    filas_a = len(matriz_a)
    columnas_a = len(matriz_a[0])
    columnas_b = len(matriz_b[0])

    matriz_resultado = [[0 for _ in range(columnas_b)] for _ in range(filas_a)]

    for i in range(filas_a):
        for j in range(columnas_b):
            for k in range(columnas_a):
                matriz_resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return matriz_resultado

matriz_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz_b = [
    [7, 8],
    [9, 10],
    [11, 12]
]

resultado = multiplicar_matrices(matriz_a, matriz_b)
print("La multiplicación de las matrices es:")
for fila in resultado:
    print(fila)
