
def factorial(n):
    res = 1 
    for i in range(1,n+1):
        res*=i
    return res

def main():
    n = int(input('Ingrese el numero de muestras sin orden: '))
    m = int(input('Ingrese el numero de grupos a formar: '))
    resultado = (factorial(n))/(factorial(m)*factorial(n-m))
    print(f'El numero de grupos que puede formas es: {int(resultado)}')

if __name__ == "__main__":
    main()