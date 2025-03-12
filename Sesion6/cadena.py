#cadena='Hola Mundo!'
#print(cadena[3])

#-------------for _ in range------------
# for i in range(len(cadena)):
#     print(cadena[i])

# for i in range(-1,-len(cadena)-1,-1):
#     print(cadena[i])

#-------------for-each---------------
# for i in cadena:
#     print(i)    

#-------------for enumerate----------
# for idx,val in enumerate(cadena):
#     print(f'indice:{idx} , valor: {val}')

#-------------while-----------------
cadena = input('Ingrese una frase:\n').capitalize()
n=0
while n<len(cadena):
    print(cadena[n])
    n+=1