#!/usr/bin/python3
"""
Hello HBNB
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python/<text>', strict_slashes=False)
def py(text):
    if text:
        return f"Python {text.replace('_', ' ')}"
    else:
        return "Python is cool"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
