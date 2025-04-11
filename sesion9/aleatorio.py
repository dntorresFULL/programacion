import random as r

for i in range(5):
    n = r.randint(1,100)
    print(n)
    u = r.uniform(1,100)
    #print(round(u,2))
    print(f'{u:.2f}')
    letra = r.choice('zapato') 
    print(letra)