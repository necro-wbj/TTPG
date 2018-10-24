# -*- coding: utf-8 -*-
import cupy as cp
import matplotlib.pyplot as plt
import csv
# N is batch size(sample size); D_in is icput dimension;
# H is hidden dimension; D_out is output dimension.
N, D_in, H, D_out = 4520, 9, 9, 9

# Create random icput and output data
x = list()
with open('qtrain_data.txt', newline='') as csvfile:
    f = csv.reader(csvfile)
    for row in f:
        x.append(list(map(int, row)))
y = list()
with open('atrain_data.txt', newline='') as csvfile:
    f = csv.reader(csvfile)
    for row in f:
        y.append(list(map(int, row)))
x = cp.array(x, cp.float)
y = cp.asarray(y, cp.float)
# Randomly initialize weights
w1 = cp.random.randn(D_in, H)
w2 = cp.random.randn(H, D_out)

learning_rate = 0.00002
loss_col = []
t = 0
k = 0
while k < N:
    k = 0
    # Forward pass: compute predicted y
    h = x.dot(w1)
    h_relu = cp.maximum(h, 0)  # using ReLU as activate function
    y_pred = h_relu.dot(w2)

    # Compute and print loss
    loss = cp.square(y_pred - y).sum()  # loss function
    loss_col.append(loss)
    print("第%d次訓練\n誤差:%f\n輸出:" % (t, loss))
    print(y_pred)
    # Backprop to compute gradients of w1 and w2 with respect to loss
    grad_y_pred = 2.0 * (y_pred - y)  # the last layer's error
    grad_w2 = h_relu.T.dot(grad_y_pred)
    grad_h_relu = grad_y_pred.dot(w2.T)  # the second laye's error
    grad_h = grad_h_relu.copy()
    grad_h[h < 0] = 0  # the derivate of ReLU
    grad_w1 = x.T.dot(grad_h)

    # Update weights
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2
    result = cp.equal(cp.argmax(y, 1), cp.argmax(y_pred, 1))
    for i in result:
        if i:
            k += 1
    t = t + 1
    print("答對筆數/總筆數: %d/%d" % (k, N))
    print()
    if t % 100 == 0:
        plt.plot(loss_col)
        plt.show()
