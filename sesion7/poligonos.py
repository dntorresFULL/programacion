
while 1:
    print('Seleccione una de las siguientes opciones: \n'+
      '1. Calcular el area del TRIANGULO\n'+
      '2. Calcular el area del CUADRADO\n'+
      '3. Calcular el area del RECTANGULO\n'+
      '4. Calcular el area del Circulo\n'+
      '5. Salir')
    
    opc = input('Seleccione la opcion que desea calcular: ')

    if opc == '1':
        base = float(input('Ingrese el valor de la base: '))
        altura = float(input('Ingrese el valor de la altura: '))
        area = (base*altura)/2
    elif opc=='2':
        lado = float(input('Ingrese el valor del lado: '))
        area = lado**2
    elif opc == '3':
        base = float(input('Ingrese el valor de la base: '))
        altura = float(input('Ingrese el valor de la altura: '))
        area = base*altura
    elif opc =='4':
        pi=3.1416
        radio = float(input('Ingrese el valor del radio: '))
        area = pi*radio**2
    else:
        print('Seleccion errada.')
        break
    print(f'el area es: {area:.2f}\n\n')