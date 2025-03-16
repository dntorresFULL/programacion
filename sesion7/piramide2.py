n = int(input('Ingrese la altura del triangulo: '))

txt=''
numero = 1
for i in range(n):
    txt = str(numero)+ ' ' + txt
    print(txt)
    numero+=2