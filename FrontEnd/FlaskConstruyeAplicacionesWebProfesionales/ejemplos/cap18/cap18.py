from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<string:name>')
@app.route('/hello/<string:name>/<int:age>')
@app.route('/hello/<string:name>/<int:age>/<email>')
def hello(name = None, age = None, email = None):
  my_data = {
    'name': name,
    'age': age,
    'email': email
  }
  return render_template('hello.html', data = my_data)
