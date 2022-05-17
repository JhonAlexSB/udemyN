def saludo():
    while (True):
        print('hola')

saludo()

# No muestra error cuando se interrumpo por un ctrl + c la ejecucion
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

