import urllib.request
# Si la libreria no esta usar pip install

# se usa wb write, y binario
# web = open('web.html','wb')
web = open('prueba.html','wb')
# consulta = urllib.request.urlopen('https://lorem2.com')
consulta = urllib.request.urlopen('https://imdb')
consulta = consulta.read()
web.write(consulta)
web.close


