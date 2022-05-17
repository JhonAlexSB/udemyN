# numero mayor a 100
numero = int(input("Digite un numero: "))

if numero > 50:
    print("numero mayor a 50")
    if numero > 100:
        print("numero mayor a 100")
        if numero > 150:
            print("numero mayor a 150")
else:
    print("numero menor a 50")

# Otra manera de condicionales
print("\n Otra manera de condicionales \n")

if numero > 50:
    print("numero mayor a 50")
    if numero > 100:
        print("numero mayor a 100")
    if numero > 150:
        print("numero mayor a 150")
else:
    print("numero menor a 50?")
