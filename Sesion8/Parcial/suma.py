n = int(input('Cuantos numeros naturales quiere sumar: '))

suma=0
for i in range(1,n+1):
    if i % 2==0:
        suma+=i
    else:
        suma+=(2*i)-1

print(suma)   