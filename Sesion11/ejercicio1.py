

def matriz(rows,cols):
    lista = []
    for i in range(rows):
        lista.append([])
        for j in range(cols):
            if i == j:
                x=1
            elif i>j:
                x=2
            else:
                x=0
            lista[i].append(x)
    return lista

def impresion(lista):
    for fila in lista:
        print(fila)

def main():
    filas = int(input('Ingrese el numero de filas: '))
    columnas = int(input('Ingrese el numero de columnas: '))
    lista=matriz(filas,columnas)
    impresion(lista)



if __name__ == "__main__":
    main()