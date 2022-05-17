informacion = {'Nombre':'Pedro','Edad':24,'Especialiad':['Programacion','Ciberseguridad']}

informacion['Edad'] = 23

# print(informacion['Nombre'])

# for info in informacion:
    # # print(info)
    # # print(informacion[info])
    # if isinstance(informacion[info],list):
        # for i in informacion[info]:
            # print(f'{info}: {i}')
    # else:
        # print(f'{info}:{informacion[info]}')


# informacion.clear()
print(informacion.items())
print(informacion.keys())
print(informacion.values())

if 'Edad' in informacion:
    print('Edad si se encuentra')


if 'Pedro' in informacion.values():
    print('Pedro si se encuentra')
