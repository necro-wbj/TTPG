import tensorflow as tf
from tensorflow import keras
import numpy as np

model = keras.Sequential([
    keras.layers.Dense(64, activation='sigmoid'),
    keras.layers.Dense(1000, activation='sigmoid'),
    keras.layers.Dense(1000, activation='sigmoid'),
    keras.layers.Dense(1000, activation='sigmoid'),
    keras.layers.Dense(64, activation='sigmoid')
])
adam = keras.optimizers.Adam()
model.compile(optimizer=adam, loss='categorical_crossentropy',
              metrics=['accuracy'])

def out(chessboard):
    chessboard=chessboard.reshape((1,64))
    output=model.predict(chessboard)
    return output
