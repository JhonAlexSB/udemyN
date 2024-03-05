from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
  print(url_for('index'))
  # print(url_for('hello', name = "Alex"))
  # print(url_for('hello'))
  # print(url_for('code',code = 'print("hola")'))
  name = 'jhon'
  friends = ["Alexander", "Roel", "Juan", "Pedro"]

  return render_template(
    'index.html', 
    name = name, 
    friends = friends, 
    )
