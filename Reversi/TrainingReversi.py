import tensorflow as tf
from tensorflow import keras
import numpy as np

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
print("正在讀取已保存的權值...")
# model.load_weights('Reversi.h5')
# try:
#     model.load_weights('Reversi.h5')
# except Exception as e:
#     print("讀檔錯誤,略過讀取已保存的權值")


def out(chessboard):
    chessboard = chessboard.reshape((1, 64))
    output = model.predict(chessboard)
    return output


def train(input_data, expect_data, batch):
    print("開始訓練...")
    input_data = np.array(input_data)
    expect_data = np.array(expect_data)
    model.fit(input_data, expect_data, epochs=1000,
              batch_size=batch, verbose=1)
    model.save_weights('./Reversi.h5', save_format='h5')
