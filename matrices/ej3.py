def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    matriz_transpuesta = [[0 for _ in range(filas)] for _ in range(columnas)]
    
    for i in range(filas):
        for j in range(columnas):
            matriz_transpuesta[j][i] = matriz[i][j]
    
    return matriz_transpuesta

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = transponer_matriz(matriz)
print("La matriz transpuesta es:")
for fila in resultado:
    print(fila)
