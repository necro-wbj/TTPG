import tensorflow as tf
from tensorflow import keras
import numpy as np
import os


def create_model():
    print("正在建立類神經網路模型...")
    model = keras.Sequential()
    model.add(keras.layers.Dense(1000, activation='softmax'))
    model.add(keras.layers.Dense(1000, activation='softmax'))
    model.add(keras.layers.Dense(1000, activation='softmax'))
    model.add(keras.layers.Dense(1000, activation='softmax'))
    model.add(keras.layers.Dense(1000, activation='softmax'))
    model.add(keras.layers.Dense(1000, activation='softmax'))
    model.add(keras.layers.Dense(64, activation='softmax'))
    adam = keras.optimizers.Adam()
    print("正在編譯類神經網路...")
    model.compile(optimizer=adam, loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model


main_checkpoint_path = './Main_Reversi.ckpt'
checkpoint_path = './Reversi.ckpt'
checkpoint_dir = os.path.dirname(main_checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    main_checkpoint_path, save_weights_only=True, verbose=1, period=1000)
model = create_model()
print("讀取已保存的權值...")
try:
    model.load_weights(main_checkpoint_path)
except Exception as e:
    print("讀檔錯誤,略過讀取已保存的權值")


def predict_opt(chessboard):
    chessboard = np.array(chessboard).reshape(1, 64)
    output = model.predict(chessboard).reshape(8, 8)
    return output


def update_weights(input_data, expect_data, batch):
    try:
        model.load_weights(checkpoint_path)
    except Exception as e:
        print(e)
    input_data = np.array(input_data)
    expect_data = np.array(expect_data)
    print("主要網路更新權重...")
    model.fit(input_data, expect_data,
              batch_size=batch, callbacks=[cp_callback])
