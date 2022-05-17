# 13 a mas A
# 11 a 12  C
# 10 a menos B

nombre = input("Ingrese su nombre: \n")
sexo = input("Ingrese su sexo: \n[M] Masculino \n[F] Femenino \n")
sexo = sexo.upper()
resultado = ''

if (sexo != 'F' and sexo != 'M'):
    print("Sexo no valido !!!!")
else:    
    nota = int(input("digite la nota: \n"))
    if (nota > 20 or nota < 0):
        print("Su nota no esta dentro de los valores validos 20 a 0")
    else:
        if(nota >= 13):
            resultado = 'Usted Aprobo'
        elif(nota == 12 or nota == 11):
            resultado = 'Usted debe ir a vacacional'
        elif(nota <= 10):
            resultado = 'Usted Reprobo'
            
if(resultado != ''):
    if (sexo == 'M'):
        print(f"Senor {nombre} "+resultado)
    else:
        print(f"Senorita {nombre} "+resultado)
