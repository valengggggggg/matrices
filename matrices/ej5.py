def suma_filas(matriz):
    sumas = []
    
    for fila in matriz:
        suma = sum(fila)
        sumas.append(suma) 
    
    return sumas

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = suma_filas(matriz)
print("La suma de cada fila es:", resultado)
