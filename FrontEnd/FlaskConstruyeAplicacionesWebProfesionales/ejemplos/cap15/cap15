from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  name = None
  friends = ["Alexander", "Roel", "Juan", "Pedro"]

  return render_template('index.html', name = name, friends = friends)
