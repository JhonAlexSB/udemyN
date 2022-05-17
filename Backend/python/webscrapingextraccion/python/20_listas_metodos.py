nombres = ['Pedro','Jorge','Maria','Ana']

# print(len(nombres))
print(nombres[0])
print(nombres[-1])

print(' --- Metodo append y count')
nombres.append('Rodrigo')
nombres.append('Rodrigo')
print(nombres.count('Rodrigo'))

print(' --- Metodo insert y remove')
nombres.insert(2,'Rodrigo')
nombres.remove('Rodrigo')

print(' --- Metodo index y pop')
print(nombres.index('Rodrigo'))
print(nombres.pop())

# Recorre por objeto de listas
# for nombre in nombres:
    # print(nombre)

print(' --- impresion de la lista nombres')

# Recorre por numeros
for i in range(len(nombres)):
    print(nombres[i])

print(' ---- uso de reverse y impresion de lista otro modo')
nombres.reverse()

for i in nombres:
    print(nombres[nombres.index(i)])

