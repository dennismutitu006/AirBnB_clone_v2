#!/usr/bin/python3
"""script that starts a flask webapp"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """print web"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hBNB():
    """display"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """print c with the specified text in cli"""
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_baby(text='is cool'):
    """Print python with the specified text"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
