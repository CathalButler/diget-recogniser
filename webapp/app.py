from __future__ import print_function

import base64
import os
import re
import cv2 as cv2
import flask
import numpy as np
import tensorflow as tf
from flask import Flask, render_template
from keras import backend as k
from keras.engine.saving import load_model

# Cathal Butler | G00346889
# Class that allows API requests from a client to to a prediction check on a number they draw on the canvas that is
# displayed to them.

# Reference:
# https://www.jitsejan.com/python-and-javascript-in-flask.html
# https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html
# https://stackoverflow.com/questions/45408496/getting-error-cannot-reshape-array-of-size-122304-into-shape-52-28-28
# https://github.com/tensorflow/tensorflow/issues/28287#issuecomment-495005162
# http://yangyang.blog/2019/03/it-works-an-epic-debugging-thesis-week-8/
# https://stackoverflow.com/questions/53653303/where-is-the-tensorflow-session-in-keras


# initialize Flask application and the Keras model:
app = Flask(__name__, )
app.debug = True
app.secret_key = 'development'
# Define static folder location
app._static_folder = os.path.abspath("webapp/templates/static/")
# load trained keras model:
model = load_model('model.h5')
graph = tf.get_default_graph()
sess = k.get_session()


def load_keras_model():
    # load trained keras model:
    global model, graph, sess


# Function to resize and flatten the image received int he POST request
def prepare_image(image, size=(28, 28)):
    return cv2.resize(image, size).flatten()


# Function to convert the data sent in the /predict post request to an image
def convert_to_image(imageData):
    imgstr = re.search(r'base64,(.*)', str(imageData)).group(1)
    with open('output.png', 'wb') as output:
        output.write(base64.b64decode(imgstr))


# Function to make a post request with the data from the canvas:
@app.route('/predict', methods=['POST'])
def post_predict():
    # global vars
    global model, graph, sess, image
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        # app.logger.info("got in side the function " + image)
        # read data from request
        # TODO: Implemented handling for different input types as I believe currently its casing issues
        filestr = flask.request.get_data()
        # convert string data to numpy array
        npimg = np.fromstring(filestr, np.uint8)
        # convert numpy array to image
        image = cv2.imdecode(npimg, cv2.IMREAD_GRAYSCALE)
        # make it the right size and flatten data
        image = np.array(prepare_image(image, size=(28, 28)))
        # reshape the array
        # TODO: Fix why im getting an  error: (-215:Assertion failed) !ssize.empty() in function 'resize'
        image = image.reshape(1, 28, 28, 1)
        app.logger.info(image)
        # set a session - note please see links above for why this is needed.
        with sess.as_default():
            with graph.as_default():
                data["prediction"] = str(model.predict_classes(image))
                data["success"] = True

    # TODO: tidy response that display on index.html
    # Return the predicted number that the model returned
    return flask.jsonify(data)


# Function with route '/' to 'GET' the home page : index.html
@app.route('/', methods=['GET'])
def index():
    title = 'Create the input'
    return render_template('layouts/index.html',
                           title=title)


# Running application
if __name__ == '__main__':
    load_keras_model()
    app.run(host='0.0.0.0', port=5000, debug=True)
