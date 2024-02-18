from flask import Flask

app = Flask(__name__)

  # Si se repiten las rutas solo tomara la primera


@app.route('/')
@app.route('/index')
def index():
  return '<h1>Página de inicio</h1>'

  # para acceder a esta vista hay dos rutas
  # localhost:5000/
  # localhost:5000/index

@app.route('/hello')
def hello():
  return '<h2>Hola Mundo</h2>'

  # para acceder a esta vista hay una ruta
  #  localhost:5000/hello
