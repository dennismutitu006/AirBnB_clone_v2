#!/usr/bin/python3
"""a script that starts a flask web application"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """print webcontent"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hBNB():
    """print webcontet"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """display c then with the def text"""
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_baby(text='is cool'):
    """Display Python folowd by the value of txt var"""
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """num route"""
    return '{:d} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
