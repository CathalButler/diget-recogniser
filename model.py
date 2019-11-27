import matplotlib.pyplot as plt
from keras.utils import np_utils

import keras
from keras.datasets import mnist
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

# NOTES Originally I was trying to predict numbers from the trained model that I saved inside the jupyter notebook.
# Doing so was causing me errors with elements that that had saved from the notebook that I didnt need in the saved
# model. To overcome this issue I did a copy of a lot of the code from the notebook into this class were the model
# can run and train the data without adding elements that are not needed. Running a save within the notebook and then
# loading the model in my flask webapp was causing a lot of issues that I did fix with the help of
# https://towardsdatascience.com/deploying-keras-deep-learning-models-with-flask-5da4181436a2
#   with sess.as_default():
#       with graph.as_default():
#           prediction = np.array(model.predict(image)[0])
#


# The number of training examples in one forward/backward pass.
# The higher the batch size, the more memory space you'll need.
batch_size = 128
num_classes = 10
# Setting the number of forward passes and backward passes of all the training examples
epochs = 10
# input image dimensions : IMPORTANT
img_rows, img_cols = 28, 28

# The MINST dataset is loaded from keras:
# TRAIN & TEST
(x_train, y_train), (X_test, y_test) = mnist.load_data()
# Print the original X & Y train shape:
print("Original X shape", x_train.shape)
print("Original Y shape", y_train.shape)

# Reshape data.
if K.image_data_format() == 'channels_first':
    # resizing the train data and storing it inside a NumPy Array:
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    # resizing the test data and storing it inside a NumPy Array:
    x_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
    # Define the input shapes for the keras model of the images
    input_shape = (1, img_rows, img_cols)
else:
    # resizing the train data and storing it inside a NumPy Array:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    # resizing the test data and storing it inside a NumPy Array:
    x_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
    # Define the input shapes for the keras model of the images
    input_shape = (img_rows, img_cols, 1)

# It is common to use 32-bit when training a neural network, regarding the division by 255, this is the max value of a
# type(the inputs type before conversion to float32), so this will ensure that the inputs are scaled between 0.0 & 1.0.
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Print the training and testing X matrix shape
print("Training X matrix shape", x_train.shape)
print("Testing X matrix shape", X_test.shape)
print(y_train[0])

# Represent the targets as one-hot vectors: e.g. 2 -> [0, 0, 1, 0, 0, 0, 0, 0, 0].
nb_classes = 10

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
# Printing out the Y training and testing matrix shape
print("Training Y matrix shape", y_train.shape)
print("Testing Y matrix shape", y_test.shape)

# Keras Model
model = Sequential()
# Convolution Layer:
# Input images with 3 channels:
# this applies 32 convolution filters of size 3x3 each.
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
# Unflattened data
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

# Keras Summary
model.summary()

# Compile the model
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

# try load model from pre
# try:
#     print("Model loaded successfully")
#     model = load_model("model.h5")
#
#     list(model)
#
# except:
# Training the model
history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))

# Save the model in h5 format
model.save("modelWithOutNotebook.h5")
print("Saved model to disk")

# finally:
#     print("Model loaded from save file")
#     score = model.evaluate(x_test, y_test, verbose=0)
#     print('Test cross-entropy loss: %0.5f' % score[0])
#     print('Test accuracy: %.2f%%' % (score[1] * 100))
