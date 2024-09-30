def suma_matrices(matriz_a, matriz_b):
    filas = len(matriz_a)
    columnas = len(matriz_a[0])
    matriz_suma = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            matriz_suma[i][j] = matriz_a[i][j] + matriz_b[i][j]

    return matriz_suma

matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

resultado = suma_matrices(matriz_a, matriz_b)
print("La suma de las matrices es:")
for fila in resultado:
    print(fila)
