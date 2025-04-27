from random import randint as r

def matriz(rows,cols):
    matriX = []
    for i in range(rows):       #Crea el contenedor de filas
        matriX.append([])
        for j in range(cols):
            matriX[i].append(r(0,100))
    return matriX

def impresion(matriX):
    for fila in matriX:
        print(fila)

def escalar(matriX):
    valorEscalar = int(input('Ingrese un valor para escalar la matriz: '))
    for i in range(len(matriX)):
        for j in range(len(matriX[i])):
            matriX[i][j] *= valorEscalar
    return matriX

def main():
    filas = int(input('Ingrese el numero de filas: '))
    columnas = int(input('Ingrese el numero de columnas: '))
    lista = matriz(filas,columnas)
    impresion(lista)            #Imprime la matriz original
    listaFinal = escalar(lista)
    impresion(listaFinal)       #Imprime la matriz escalada


if __name__ == "__main__":
    main()