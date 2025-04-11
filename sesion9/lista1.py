from random import randint as r
#import random as r      => r.randint

def aleatorio(n):
    listaNumeros = []
    for i in range(10):
        numero = validarNumero()
        listaNumeros.append(numero)
        if numero == n:
            print('Felicidades, encontró el numero secreto')
            return
        else:
            print('Lo lamento, sigue intentando...')
    print(listaNumeros)    

def validarNumero():
    while 1:
        numero = int(input('¿Cual es el numero secreto? '))
        if 0<numero<9:
            return numero
        print('El numero debe ser entre 0 y 9')
    
def main():
    n = r(0,9)
    aleatorio(n)

if __name__=="__main__":
    main()