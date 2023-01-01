def main():
    web = open('web.html','rb')
    inicio = '<li>'
    final = '</li>'
    for linea in web.readlines():
        linea = str(linea)
        # Encuentra todas las lineas con coincidencia de variable inicio
        if inicio in linea:
            if not 'href=' in linea:
                # es para buscar el numero de posicion del string
                x = linea.find(inicio)
                # Se le suma el valor anterior mas el de len para englozar el inicio
                # del texto y del li
                x = x + len(inicio)
                y = linea.find(final)

                print(linea[x:y])
    

if __name__ == '__main__':
    main()

