tupla = ('Pedro','Pablo','Jasinto')
lista = ['Pedro','Pablo','Jasinto']

print(tupla)
print(lista)

# se lee igual agregando el numero del indice
# pero la tupla da error si se intenta modificar el valor

# tupla[0] = 'Jhon'
# print(tupla[0])

print(tupla.count('Pedro'))
print(tupla.index('Pedro'))


for i in range(len(tupla)):
    print(tupla[i])

# la tupla y la lista se recorre igual
# for nombre in tupla:
    # print(nombre)

