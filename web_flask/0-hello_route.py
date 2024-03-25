#!/usr/bin/python3
"""This script starts a flask web app"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False
@app.route('/')
def hello_hbnb():
    """Print webpage content"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
