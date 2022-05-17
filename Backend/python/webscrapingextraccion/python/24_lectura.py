import time

file_users = open('file/users.txt','r',encoding='latin-1')
usuarios = file_users.read().split('\n')
usuarios.pop()

# si lo imprimo asi sin asignar me muestra informacion de la lectura
# file_user.read()

file_pass = open('file/pass.txt','r',encoding='utf-8')
passwords = file_pass.read().split('\n')
passwords.pop()

for usuario in usuarios:
    for password in passwords:
        if usuario == 'root' and password == 'root':
            print(f'Se encontraron las credenciales {usuario}:{password}')
        else:
            print(f'Intento fallido: {usuario}:{password}...')
            time.sleep(1)

# print(type(passwords))
# print(usuarios)
# print(passwords)

file_users.close()
file_pass.close()

# si hay errores de encode con utf-8 se puede probar con latin-1
