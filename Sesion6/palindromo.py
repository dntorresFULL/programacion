<<<<<<< HEAD
texto = input('Ingrese una frase\n').lower()

txt=''                  #Quitar los espacios
for i in texto:
    if i != ' ':
        txt+=i
print(txt)

longitud=len(txt)//2    #Evaluar si es palindromo
flag=True
for i in range(longitud):
    if txt[i]!=txt[len(txt)-1-i]:
        flag=False
        break

if flag:                #Respuesta con flag booleano
    print('Si es palindromo')
else:
=======
texto = input('Ingrese una frase\n').lower()

txt=''                  #Quitar los espacios
for i in texto:
    if i != ' ':
        txt+=i
print(txt)

longitud=len(txt)//2    #Evaluar si es palindromo
flag=True
for i in range(longitud):
    if txt[i]!=txt[len(txt)-1-i]:
        flag=False
        break

if flag:                #Respuesta con flag booleano
    print('Si es palindromo')
else:
>>>>>>> 30ccaa3c3d1957400d183868833640e532ee258f
    print('No es palidromo')