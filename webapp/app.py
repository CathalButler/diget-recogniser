from __future__ import print_function

import os
import cv2 as cv2
import flask
import numpy as np
import tensorflow as tf
from flask import Flask, render_template
from keras import backend as k
from keras.engine.saving import load_model

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


# Function to make a post request with the data from the canvas:
@app.route('/predict', methods=['POST'])
def post_predict():
    # global vars
    global model, graph, sess, image
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.files.get("image"):

            # read image file string data
            filestr = flask.request.files['image'].read()
            # convert string data to numpy array
            npimg = np.fromstring(filestr, np.uint8)
            # convert numpy array to image
            image = cv2.imdecode(npimg, cv2.IMREAD_GRAYSCALE)

            app.logger.info("got in side the function " + image)

            # convert the image to an array 
            image = np.array(prepare_image(image, size=(28, 28)))
            # reshape the array to be the correct size for the model
            image = image.reshape(1, 28, 28, 1)
            # set a session - note please see links above for why this is needed.
            with sess.as_default():
                with graph.as_default():
                    data["prediction"] = str(model.predict_classes(image))
                    data["success"] = True

    # Return the predicted number that the model returned
    return flask.jsonify(data)


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


# Running application
if __name__ == '__main__':
    load_keras_model()
    app.run(host='0.0.0.0', port=5000, debug=True)
