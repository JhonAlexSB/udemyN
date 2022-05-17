# Contrasena = xyz 3 intentos
i = 0
contra = 'xyz'
contra2 = ""

while (contra2 != 'xyz' and i < 3): 
    i += 1
    contra2 = input("Digite la contrasena : ")

if (contra == contra2):
    print("Contrasena correcta")
else:
    print("Contrasena incorrecta")

