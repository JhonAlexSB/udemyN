from time import sleep

def salida():
    print('Saliendo...')
    sleep(1)
    exit()

try:
    # nombre
    # print(5/0)
    # print('hola' + 1)
        saludo = 'hola'
        print(int(saludo))
except KeyboardInterrupt:
    salida()
except NameError:
    salida()
except ZeroDivisionError:
    salida()
except TypeError:
    salida()
except ValueError:
    salida()
