import json

file = open('ejemplo.json','r')
file = json.loads(file.read())

print('-'*10)
print(f'Son {len(file)} personas')
print('-'*10)

for dato in file:
    print('Nombre:',dato['nombre'])
    print('Apellido:',dato['apellido'])
    print('Edad:',dato['edad'])
    print('Pais:',dato['pais'])
    print('-'*20)
