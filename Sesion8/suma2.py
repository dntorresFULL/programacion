
from fcnext import suma

def app():
    a = int(input('Ingrese un numero: '))
    b = int(input('Ingrese un numero: '))
    print(suma(a,b))
    print(__name__)

if __name__ == "__main__":
    app()