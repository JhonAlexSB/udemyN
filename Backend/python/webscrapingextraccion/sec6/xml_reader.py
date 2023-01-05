import urllib.request
import xml.etree.ElementTree as xml

url='https://www.w3schools.com/xml/simple.xml'
info=urllib.request.urlopen(url).read()

# info=urllib.request.urlopen(url)
# Sin el .read() solo aparece la consulta    

archivo = xml.fromstring(info.decode())
query = archivo.findall('food')

print('*'*10)
print('Cantidad de registros: ',len(query))
print('*'*10)

for line in query:
    print('Nombre:', line.find('name').text)
    print('Precio:', line.find('price').text)
    print('Descripcion:', line.find('description').text)
    print('Calorias:', line.find('calories').text)
    print('-'*20)
