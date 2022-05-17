nombres = ["Pedro","Pablo","Jasinto","Jose"]
print(nombres)

edades = [24,12,22]
# print(type(edades))

booleano = [True,False]
lista = [['Pedro','Pablo','Jasinto'],[24,12,22]]
mix = ['Jorge',24,True,3.5,['Adios','Hola']]
print(mix)

# for edad in edades:
    # print(type(edad))

# for i in booleano:
    # print(type(i))

# for i in lista:
    # for j in i:
        # print(j)
    # print(i)

print('---- lista 2d ----')

# lista_2d = [
    # [
        # 'Jorge',24
    # ],
    # [
        # 'Daniel',25
    # ],
    # [
        # 'Maria',21
    # ]
# ]

# for i in lista_2d:
    # for j in i:
        # print(j)


print('---- isinstance ----')

# Este bucle con sentencia isinstance soluciona el error del ciclo for anterior de imprimir cada valor

for valor in mix:
    if isinstance(valor, list):
        for j in valor:
            print(j)
    else:
        print(valor)

