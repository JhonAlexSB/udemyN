from flask import Flask, render_template

app = Flask(__name__)

def today(date):
  return date.strftime('%d-%m-%Y')

app.add_template_filter(today, 'today')

## Funcion personalizada

## Agregando funcion decoradora se puede llamar a la funcion de manera global
# "linea 15" no seria necesaria la "linea 34" invocando a funcion repeat
# es lo mismo que se hace con la funcion today, y esa es otra manera de crear una funcion decorada
# @app.add_template_global
def repeat(palabras, numeros):
  return palabras * numeros

from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
  name = 'jhon'
  friends = ["Alexander", "Roel", "Juan", "Pedro"]
  date = datetime.now()

  return render_template(
    'index.html', 
    name = name, 
    friends = friends, 
    date = date,
    repeat = repeat
    )

