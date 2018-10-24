#! python
import csv
import numpy as np
import math

player = -1
inputs_nodes = 9
hidden_nodes = 11
output_nodes = 9
weight = np.random.rand(hidden_nodes, inputs_nodes)
weight2 = np.random.rand(output_nodes, hidden_nodes)
baise = np.ones(hidden_nodes)
# weight2 = np.array(np.size([[random.random()for _ in range(h,0))]
#                     for _ in range(np.size(output,0))])
L = 0.1


def activation(n):
    num = 1 / (1 + math.exp(1) ** (-1 * n))
    return num


def output_activation(array):
    List = list()
    max = array == np.amax(array)
    for i in max:
        if not i:
            List.append(0)
        else:
            List.append(1)
    return np.asarray(List)


def ai2(inputs, answers, train, print_result=False):
    global weight, weight2, baise
    hidden = map(lambda w, b: np.sum(inputs * w) + b, weight, baise)
    hidden = np.asarray(list(map(activation, hidden)))
    output = map(lambda w: np.sum(hidden * w), weight2)
    output = np.asarray(list(map(activation, output)))
    if train:
        weight2, weight, baise = training(
            answers, weight, output, weight2, inputs, hidden, baise)
    # if print_result:

    Error = np.sum((answers - output) ** 2)
    return Error


def BP(delta, inputs):
    global L
    delta_w = map(lambda delt: L * delt * inputs, delta)
    return np.asarray(list(delta_w))


def training(answers, weight, output, weight2, inputs, hidden, baise):
    global L, output_nodes, hidden_nodes
    E = np.dot(np.dot((answers - output), output), 1 - output)
    weight2 += BP(E, hidden)
    E2 = np.array([])
    delta = np.array([])
    for j in range(hidden_nodes):
        for k in range(output_nodes):
            E2 = np.sum(np.dot(E[k], weight2[k][j]))
        delta = np.append(delta, hidden[j] * (1 - hidden[j]) * E2)
    weight += BP(delta, inputs)
    baise += BP(delta, 1)
    return weight2, weight, baise


def ox(x):
    if np.sum(x):
        return -1
    else:
        return 1


def print_result(a):
    for i in range(9):
        if i % 3 == 0:
            print("\n", "_ ", "_ ", "_ ")
        else:
            print('|', end="")
        if a[i] == 0:
            print("  ", end="")
        elif a[i] == 1:
            print(" O", end="")
        elif a[i] == -1:
            print(" X", end="")
    print()


ans = []
with open('atrain_data.txt', newline='') as csvfile:
    f = csv.reader(csvfile)
    for row in f:
        ans.append(list(map(int, row)))
ans = np.asarray(ans)
b = []
with open('qtrain_data.txt', newline='') as csvfile:
    f = csv.reader(csvfile)
    for row in f:
        b.append(list(map(int, row)))
b = np.asarray(b)
train_datas = np.size(b)
e = 0
with open("learning_rate%f.txt" % (L), 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for times in range(100000):
        e = map(ai2, b, ans, np.ones(train_datas), np.ones(train_datas))
        print("第%d次訓練誤差:" % (times + 1))
        print(np.sum(list(e)))
        print()
        spamwriter.writerow(map(str, e))
for i in map(ai2, b, ans, np.zeros(train_datas), np.ones(train_datas)):
    print()
with open("weight.txt", 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for i in weight:
        spamwriter.writerow(map(str, i))
with open("weight2.txt", 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for i in weight2:
        spamwriter.writerow(map(str, i))

# 4749.841486659332
