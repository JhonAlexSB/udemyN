def main():
    web = open('web.html','rb')
    inicio = '<title>'
    final = '</title>'
    for linea in web.readlines():
        linea = str(linea)
        if inicio in linea:
            x = linea.find(inicio)
            x += len(inicio)
            y = linea.find(final)
            print(linea[x:y])


if __name__ == '__main__':
    main()

