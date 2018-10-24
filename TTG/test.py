import csv

import numpy as np
import tensorflow as tf
from tensorflow import keras

import game

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
    print("讀檔錯誤")
print("完成初始化!")
out = [0, 0, 0, 0, 0, 0, 0, 0, 0]
game.p(out)
print("*******************************")
while(out.count(0)):
    ipt=int(input("請輸入位置："))
    out[ipt] =1
    # test = np.array([out])
    # out[model.predict(test).argmax()]=1
    game.over(out)
    test = np.array([out])
    out[model.predict(test).argmax()]=-1
    game.over(out)
