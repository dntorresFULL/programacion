texto = input('Ingrese una frase: \n')

txt='Invertido: '
for i in range(-1,-len(texto)-1,-1):      #(inicio,fin,paso)
    txt+=texto[i]
print(txt)

