from flask import Flask

app = Flask(__name__)

@app.route('/codebad/<path:code>')
def codenosafe(code):
  return f'<code>{code}</code>'

from markupsafe import escape
@app.route('/code/<path:code>')
def codesafe(code):
  return f'<code>{escape(code)}</code>'
