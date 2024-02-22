from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  name = 'jhon'
  friends = ["Alexander", "Roel", "Juan", "Pedro"]

  return render_template('index.html', name = name, friends = friends)
