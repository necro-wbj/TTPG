import csv
import numpy as np
import tensorflow as tf
from tensorflow import keras

print("正在載入資料集...")
train_datas = 0
with open('qtrain_data.txt', newline='') as csvfile:
    f = csv.reader(csvfile)
    input_data = list()
    for row in f:
        input_data.append(list(map(float, row)))
        train_datas += 1
    input_data = np.array(input_data, np.float)
with open('atrain_data.txt', newline='') as csvfile:
    f = csv.reader(csvfile)
    expect_data = list()
    for row in f:
        expect_data.append(list(map(float, row)))
expect_data = np.asarray(expect_data, np.float)
print("正在建立類神經網路模型...")
model = keras.Sequential([
    keras.layers.Dense(9, activation='sigmoid'),
    keras.layers.Dense(100, activation='sigmoid'),
    keras.layers.Dense(100, activation='sigmoid'),
    keras.layers.Dense(100, activation='sigmoid'),
    keras.layers.Dense(9, activation='sigmoid')
])
adam = keras.optimizers.Adam()
print("正在編譯類神經網路...")
model.compile(optimizer=adam, loss='categorical_crossentropy',
              metrics=['accuracy'])
print("正在初始化...")
model.fit(input_data, expect_data, epochs=1, batch_size=4520, verbose=0)
print("正在讀取已保存的權值...")
try:
    model.load_weights('TTTG.h5')
except Exception as e:
    print("讀檔錯誤,略過讀取已保存的權值")
print("開始訓練...")
callback = [keras.callbacks.TensorBoard(log_dir='./logs')]
model.fit(input_data, expect_data, epochs=10000,
          batch_size=4520, callbacks=callback, verbose=1)
model.save_weights('./TTTG.h5', save_format='h5')
loss, accuracy = model.evaluate(
    input_data, expect_data, batch_size=4520, verbose=0)
output = model.predict(input_data, batch_size=4520, verbose=0)
# test = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0]])
# print(model.predict(test).argmax())
# if accuracy >= 0.85:
print("-------------尚未訓練出來的資料---------------")
for i in range(4520):
    if expect_data[i][np.argmax(output[i])] != 1:
        t = []
        for j in range(9):
            if expect_data[i][j] == 1:
                t.append(j)
        print(input_data[i], t, output[i])
print("--------------------------------------------------")
# times = 0
# print("第%i次訓練:\n    誤差: %f, 準確率: %f%%" %
#       (times * 1000, loss, accuracy * 100))
