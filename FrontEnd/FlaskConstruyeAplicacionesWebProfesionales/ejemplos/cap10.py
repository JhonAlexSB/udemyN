from flask import Flask

app = Flask(__name__)

# string
# int
# float
# path   | no resive valores como /   "caracteres especiales"
# uuid
@app.route('/hello/')
@app.route('/hello/<string:name>/')
@app.route('/hello/<string:name>/<int:age>')
def hello(name = None, age = None):
  if name == None and age == None:
    return f'<h1>Hola mundo</h1>'
  elif age == None:
    return f'<h2>Hola, {name}! </h2>'
  else:
    return f'<h2>Hola, {name}! y tu edad es {age} </h2>'

