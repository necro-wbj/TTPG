import tensorflow as tf
from tensorflow import keras
import numpy as np
import os


def create_model():
    print("正在建立類神經網路模型...")
    model = keras.Sequential([
        keras.layers.Dense(64, activation='sigmoid'),
        keras.layers.Dense(1000, activation='sigmoid'),
        keras.layers.Dense(1000, activation='sigmoid'),
        keras.layers.Dense(1000, activation='sigmoid'),
        keras.layers.Dense(64, activation='sigmoid')
    ])
    adam = keras.optimizers.Adam()
    print("正在編譯類神經網路...")
    model.compile(optimizer=adam, loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model


checkpoint_path = './Reversi.ckpt'
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    checkpoint_path, save_weights_only=True, verbose=1, period=1000)
model = create_model()
print("讀取已保存的權值...")
try:
    model.load_weights(checkpoint_path)
except Exception as e:
    print("讀檔錯誤,略過讀取已保存的權值")


def predict_opt(chessboard):
    chessboard = chessboard.reshape((1, 64))
    output = model.predict(chessboard)
    return output


def train(input_data, expect_data, batch):
    input_data = np.array(input_data)
    expect_data = np.array(expect_data)
    print("開始訓練...")
    model.fit(input_data, expect_data, epochs=1000,
              batch_size=batch, verbose=0, callbacks=[cp_callback])
