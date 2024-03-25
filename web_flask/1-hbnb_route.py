#!/usr/bin/python3
"""This script will start a flask web app"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Print web"""
    return 'Hello HBNB!'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
