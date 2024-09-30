def buscar_numero(matriz, numero):
    for i in range(len(matriz)):  # Recorremos las filas
        for j in range(len(matriz[i])):  # Recorremos las columnas
            if matriz[i][j] == numero:  # Si encontramos el número
                return (i, j)  # Retornamos la posición (fila, columna)
    return None  # Si no encontramos el número, retornamos None

# Inicialización de una matriz de ceros de tamaño 3x3
filas = 3
columnas = 3
matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

# Puedes llenar la matriz con algunos números, aquí un ejemplo:
matriz[0][0] = 1
matriz[0][1] = 2
matriz[0][2] = 3
matriz[1][0] = 4
matriz[1][1] = 5
matriz[1][2] = 6
matriz[2][0] = 7
matriz[2][1] = 8
matriz[2][2] = 9

# Pedimos al usuario que ingrese un número a buscar
numero_a_buscar = int(input("Ingrese el número que desea buscar: "))
resultado = buscar_numero(matriz, numero_a_buscar)

if resultado is not None:
    print(f"El número {numero_a_buscar} se encuentra en la posición: fila {resultado[0]}, columna {resultado[1]}")
else:
    print(f"El número {numero_a_buscar} no se encuentra en la matriz.")

