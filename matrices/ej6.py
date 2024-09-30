def suma_columnas(matriz):

    columnas = len(matriz[0])
    sumas = [0] * columnas 

    for fila in matriz:
        for j in range(columnas):
            sumas[j] += fila[j] 

    return sumas

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = suma_columnas(matriz)
print("La suma de cada columna es:", resultado)
