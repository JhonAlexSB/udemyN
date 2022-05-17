from time import sleep

def h1(title):
    title = title.upper()
    title = '<h1>'+title+'<h1>'
    return title

def h2(subtitle):
    subtitulo = subtitle.title()
    subtitulo = '<h2>'+subtitulo+'<h2>'
    return subtitulo

def p(parrafo):
    texto = parrafo.lower()
    texto = '<p>'+texto+'<p>'
    return texto

def main():
    index = open('file/index.html','a')
    index.write('<html><head></head><body>')
    while True:
        titulo = input('Ingrese un titulo \n>>')
        index.write(h1(titulo))
        for sub in range(2):
            subtitulo = input("Ingrese el subtitulo \n>>")
            index.write(h2(subtitulo))
            parrafo = input("Ingrese un parrafo \n>>")
            index.write(p(parrafo))

        continuar = input('?Desea continuar? Y/N').upper()
        if continuar == 'Y':
            pass
        else:
            break
    index.write('</body></html>')
    index.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo...')
        sleep(1)
        exit()


