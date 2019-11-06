from __future__ import print_function

import os

from flask import Flask, render_template, request, jsonify
# load and evaluate a saved model
from numpy import loadtxt
from keras.models import load_model

# https://www.jitsejan.com/python-and-javascript-in-flask.html


app = Flask(__name__, )
app.debug = True
app._static_folder = os.path.abspath("webapp/templates/static/")


# Function with route '/' to 'GET' the home page : index.html
@app.route('/', methods=['GET'])
def index():
    title = 'Create the input'
    return render_template('layouts/index.html',
                           title=title)


# Function to get the result back from the model:
@app.route('/results/', methods=['GET'])
def results():
    title = 'Result'
    return render_template('layouts/results.html',
                           title=title)


# Function to make a post request with the data from the canvas:
@app.route('/post', methods=['POST'])
def post_javascript_data():
    # Store canvas_data in jsdata
    jsdata = request.form['canvas_data']
    # return jsdata
    return jsonify(jsdata)


def load_keras_model():
    # load model from file
    model = load_model('model.h5')
    return model


# Running application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

