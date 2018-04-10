import random
h = [0] * 3
weight = [[random.triangular(-5, 5), random.triangular(-5, 5), 1]
          for _ in range(len(h))]
output = [0]
weight2 = [[random.triangular(-5, 5)for _ in range(len(h))]
           for _ in range(len(output))]
temp = [0]
train = [[0, 0], [0, 1], [1, 0], [1, 1]]
# with open("xor_weight.txt", "r") as f:
#     for line in f:
#         for i in range(2):
#             weight[f][i] = line.strip()


def act(arr):
    import math
    for i in range(len(arr)):
        arr[i] = 1 / (1 + math.exp(-arr[i]))


def oact(arr):
    return(round(arr))


def ai2(a):
    global temp, h, weight, output, weight2

    for j in range(len(h)):
        for i in range(len(a)):
            h[j] += weight[j][i] * a[i]
#            h=[h[j] + weight[j][a.index(i)] *i for i in a  for j in range(len (h))]
        h[j] += weight[j][2]
    act(h)
    for j in range(len(output)):
        for i in range(len(h)):
            output[j] += weight2[j][i] * h[i]
    act(output)
    # 正確答案
    if a == [1, 1]:
        temp[0] = 1
    else:
        temp[0] = 0
    # 倒傳遞:
    E = []
    for j in range(len(output)):
        E.append((temp[j] - output[j]) * output[j] * (1 - output[j]))
        for i in range(len(h)):
            weight2[j][i] = weight2[j][i] * 1 * E[j] * h[i]
    E2 = []
    for j in range(len(h)):
        ei = 0
        for k in range(len(E)):
            ei += E[k] * weight2[k][j]
        E2.append(h[j] * (1 - h[j]) * ei)
        for i in range(len(a)):
            weight[j][i] = weight[j][i] + 0.01 * E2[j] * a[i]
        weight[j][i] = weight[j][2] + 0.01 * E2[j]
    print("輸出:", output[0])
    print("輸出(轉換):", oact(output[0]))
    print("正確", temp[0])


step = 1
S = 0
W = 1
# while W > S:
for i in range(1000):
    for j in range(len(train)):
        a = train[j]
        print("X=", a)
        ai2(a)
        print("")
# with open("xor_weight.txt", "w") as f:
#     for s in range(2):
#         for k in range(2):
#             f.write(str(weight[s][k]) + "\n")
