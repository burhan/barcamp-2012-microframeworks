from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def index():
    return 'Barcamp 2012! I want KOO KEEZ'

@app.route('/hello/<name>')
def hello(name):
    return 'Hello {0}'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
