nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))
sexo = input('Ingrese su sexo: \n[H]. Hombre \n[M]. Mujer').upper()
carrera = input('Ingrese su carrera: ')

archivos = open('file/mis_datos.txt','w')
saludo = ''


while (sexo != 'H' and sexo != 'M'):
    sexo = input('Ingrese su sexo: \n[H]. Hombre \n[M]. Mujer').upper()
    
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
            
archivos.write(f'Hola {saludo} {nombre} {apellido}\n')
archivos.write(f'Su edad es :{edad} \n')
archivos.write(f'Su carrera es :{carrera} ')


archivos.close()
