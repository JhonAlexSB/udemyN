# nombres = ['Pedro', 'Pablo', 'Jasinto', 'Jose']

# for nombre in nombres:
    # print(f"Hola : ", nombre)

oracion = 'Bienvenidos al himalayan'
sin_letras = ''

for letra in oracion:
    if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
        print(letra)
        pass
    else:
        sin_letras += letra

print('sin letras : ',sin_letras)
