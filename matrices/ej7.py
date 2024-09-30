def crear_matriz_identidad(n):
    
    matriz_identidad = [[0 for _ in range(n)] for _ in range(n)]
    
    
    for i in range(n):
        matriz_identidad[i][i] = 2
        
    return matriz_identidad


n = 3
resultado = crear_matriz_identidad(n)

print("La matriz identidad de tamaño", n, "x", n, "es:")
for fila in resultado:
    print(fila)
