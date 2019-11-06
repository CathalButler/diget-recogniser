from __future__ import print_function

import os

from flask import Flask, render_template

# https://www.jitsejan.com/python-and-javascript-in-flask.html


app = Flask(__name__,)
app.secret_key = 's3cr3t'
app.debug = True
app._static_folder = os.path.abspath("webapp/templates/static/")


# Function with route '/' to 'GET' the home page : index.html
@app.route('/', methods=['GET'])
def index():
    title = 'Create the input'
    return render_template('layouts/index.html',
                           title=title)


@app.route('/results/<uuid>', methods=['GET'])
def results(uuid):
    title = 'Result'
    return render_template('layouts/results.html',
                           title=title)


# Running application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
