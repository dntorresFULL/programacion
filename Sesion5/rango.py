min = 10
max = 20
numero = int(input('Ingrese un numero: '))
if numero>=min:
    if numero<=max:
        if numero%2==1:
            print('Numero dentro del rango y es impar')
        else:
            print('Numero dentro del rango y es par')
    else:
        print('Numero muy alto')
else:
    print('Numero muy bajo')
        
            