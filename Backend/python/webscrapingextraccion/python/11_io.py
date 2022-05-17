# El valor por defecto es un string
# nombre = input("Por favor ingrese su nombre: \n>> ")
# print(nombre)

# Se necesita castear la entrada a un numero para operaciones aritmeticas
# numero = int(input("Digite un numero para sumarlo a 5 \n>> "))
# print(5 + numero)


# Ingresar dos valores y sumarlos
print("Bienvenido a la suma")
num1 = int(input("Digite el primer numero a sumar \n>> "))
num2 = int(input("Digite el segundo numero a sumar \n>> "))
suma = num1 + num2


print("\n 4 outputs diferentes \n")
# 4 formas de concatenar
print("La suma de",num1," con",num2," es :",suma)
print("La suma de "+str(num1)+" con "+str(num2)+" es : "+str(suma))
print("La suma de {} con {} es : {}".format(num1,num2,suma))
print(f"La suma de {num1} con {num2} es : {suma}")
