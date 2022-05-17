archivos = open('file/mis_datos2.txt','a')
cantidad = int(input("?Cuantas personas registraras?: \n"))

for i in range(cantidad):
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    edad = int(input('Ingrese su edad: '))
    sexo = input('Ingrese su sexo: \n[H]. Hombre \n[M]. Mujer').upper()
    carrera = input('Ingrese su carrera: ')

    saludo = ''
    while (sexo != 'H' and sexo != 'M'):
        sexo = input('Ingrese su sexo: \n[H]. Hombre \n[M]. Mujer\n>>').upper()
        
    if (edad >= 30):
        if(sexo == 'H'):
            saludo = 'Senor'
        else:
            saludo = 'Senora'
    else:
        if (sexo == 'H'):
            saludo = 'Joven'
        else:
            saludo = 'Jovencita'
                
    archivos.write(f'Hola {saludo}: {nombre} {apellido}\n')
    archivos.write(f'Su edad es: {edad} \n')
    archivos.write(f'Su carrera: {carrera} \n')

    archivos.write('*'*10)
    archivos.write('\n')
archivos.close()
