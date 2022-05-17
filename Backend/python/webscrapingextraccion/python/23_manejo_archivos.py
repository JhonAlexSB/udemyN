from os import remove

nombre = input('Ingresa el nombre que se almacenar: ')
print(nombre)

# con w 'write' escribe pero sobreescribe tambien
# file = open('nombres.txt','w')

# con a 'append' agrega
file = open('nombres.txt','a')
file.write(nombre+'\n')
file.close()

# Eliminar archivo
# remove('nombres.txt')

print(' === abrir archivo')

# Es un modo como el siguiente para abrir un archivo
# archivo = open('1_hellowworld.py')
# archivo = archivo.read()
# print(archivo)

with open('1_hellowworld.py') as archivo:
    arc = archivo.read()
    print(arc)

