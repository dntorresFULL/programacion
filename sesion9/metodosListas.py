

def agregar(lista):
    numero = int(input('Cual numero desea agregar: '))
    lista.append(numero)

def insertar(lista):
    numero = int(input('Cual numero desea agregar: '))
    idx = int(input('En que indice desea poner el numero: '))
    lista.insert(idx,numero)

def limpiar(lista):
    lista.clear()

def remover(lista):
    numero = int(input('Cual numero desea remover: '))
    lista.remove(numero)

def menu():
    lista=[]
    while 1:
        print('Bienvenido al sistema de uso de metodos en listas\n'
            '1. Insertar un numero al final de la lista\n'
            '2. Insertar un numero en una posicion especifica de la lista\n'
            '3. Borrar toda la lista\n'
            '4. Remover un numero especifico de la lista\n'
            's. Salir')
        
        opc =input('Seleccione una opción del menu: ')

        fcns = ['s',agregar,insertar,limpiar,remover]
        if opc != 's':
            fcns[int(opc)](lista)
        else:
            return
        print(lista)

if __name__ == "__main__":
    menu()