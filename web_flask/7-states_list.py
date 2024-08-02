#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)

"""
print("DEBUGGING")

print("storage.all()", storage.all())
print("type storage.all()", type(storage.all()))
print("=" * 50)
print("storage.all('State')", storage.all("State"))
print("type storage.all('State')", type(storage.all("State")))
print("=" * 50)
print("storage.all('State').values()", storage.all("State").values())
print("type storage.all('State').values()", type(storage.all("State").values()))

sts = sorted(list(storage.all("State").values()), key=lambda x: x.name)
print("sts: ", sts)
print("=" * 50)
print("name", sts.name)
print("id", sts.id)
print("=" * 50)
print(type(sorted(list(storage.all("State").values()), key=lambda x: x.name)))
"""
@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)
 

@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
