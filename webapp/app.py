import base64

import cv2 as cv2
import numpy as np
from flask import Flask, render_template, request, jsonify
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

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Function with route '/' to 'GET' the home page : index.html
@app.route('/predict', methods=['POST', 'GET'])
def post_predict():
    # ensure an image was properly uploaded to our endpoint
    if request.method == 'POST':
        # read data from request
        data_url = request.values['data_url_string']

        print(data_url)
        # remove unneeded data from the start of the data URL and convert the bytes into an image
        convert_to_image(data_url)

        # read image into memory
        image = cv2.imread('input_digit.png')
        # convert the image to gray scale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # make it the right size of 28x28
        image = prepare_image(image, size=(28, 28))
        # reshape the array
        image = np.array(image).reshape((1, 28, 28, 1))

        # Load the trained model
        model = load_model('model.h5')

        # Make a predication with of the image agents tbe trained model
        # Use np.argmax to return the highest number from the array. In theory it should be the number drawn in the
        prediction_number = np.array(np.argmax(model.predict(image)))

        # prediction = model.predict(image/255, batch_size=8, verbose=0)
        # prediction = model.predict(image)
        # print(prediction_number)
        # print(prediction)

        # canvas
        # predicted_number = str(np.argmax(prediction_number))
        # print(predicted_number)

        response_data = {}
        try:
            response_data['prediction'] = str(prediction_number)
            response_data['result'] = 'Success'
        except:
            response_data['result'] = 'Failed'
            response_data['message'] = 'Script has not ran correctly'

        # Return the number to the webpack
        return jsonify(response_data)


# Function to resize and flatten the image received int he POST request
def prepare_image(img, size=(28, 28)):
    return cv2.resize(img, size).flatten()


# Function to convert the data sent in the /predict post request to an image
def convert_to_image(image_data):
    # https://stackoverflow.com/questions/30963705/python-regex-attributeerror-nonetype-object-has-no-attribute-group/30964049
    print(image_data[22:])
    # Decode the image & save the image
    with open('input_digit.png', 'wb') as f:
        # data_url[24:] using everything in the array after 24
        f.write(base64.b64decode(image_data[22:]))


# Running application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
