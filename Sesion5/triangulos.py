a=float(input('Ingrese el 1er lado del triangulo: '))
b=float(input('Ingrese el 2do lado del triangulo: '))
c=float(input('Ingrese el 3er lado del triangulo: '))

if a+b>c and b+c>a and a+c>b:
    if a==b and b==c:
        print('El triangulo es Equilatero')
    elif a==b or a==c or b==c:
        print('El triangulo es Isosceles')
    else:
        print('El triangulo es escaleno')
else:
    print('Con los datos ingresados no se puede formar un triangulo')

