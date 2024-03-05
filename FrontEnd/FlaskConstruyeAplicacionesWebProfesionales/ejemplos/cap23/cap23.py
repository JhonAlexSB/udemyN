from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# Register usuario
# metodo "GET" necesario para renderizar plantilla
# metodo "POST" necesario para resivir formulario
@app.route('/auth/register', methods = ['GET', 'POST'])
def register():
  # print(request.form) # muestra los datos por consola
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    return f"Nombre de usuario: {username}, Contraseña: {password}"
  return render_template('auth/register.html')
