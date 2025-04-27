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

def busqueda(matriX):
    minimo=min(matriX[0])
    maximo=max(matriX[0])
    for fila in range (len(matriX)):
        if min(matriX[fila]) < minimo:
            minimo = min(matriX[fila])
            rows1 = fila
            cols1 = matriX[fila].index(minimo)
        if max(matriX[fila])> maximo:
            maximo = max(matriX[fila])
            cols2 = matriX[fila].index(maximo)
            rows2 = fila
    return maximo,minimo,rows1,cols1,rows2,cols2



def main():
    filas = int(input('Ingrese el numero de filas: '))
    columnas = int(input('Ingrese el numero de columnas: '))
    lista = matriz(filas,columnas)
    impresion(lista)            #Imprime la matriz original
    min,max,rows1,cols1,rows2,cols2 = busqueda(lista)
    print(f'El maximo es {max}\nPosicion: [{rows1}][{cols1}]'
          f'\nEl minimo es {min}\nPosicion: [{rows2}][{cols2}]')
    
if __name__ == "__main__":
    main()