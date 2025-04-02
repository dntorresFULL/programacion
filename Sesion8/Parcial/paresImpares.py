while 1:
    n = input('Ingrese un numero de 4 cifras: ')
    if len(n)==4:
        break
    else:
        print('Debe ingresar un numero de 4 cifras')

pares=0
impares=0
for i in n:
    if int(i) % 2==0:
        pares+=int(i)
    else:
        impares+=int(i)

if pares>impares:
    print('La diferencia de pares es mayor')
elif impares>pares:
    print('La diferencia de impares es mayor')
else:
    print('La diferencia entre pares e impares es igual')