#! python
import csv
import cupy as cp
import matplotlib.pyplot as plt
import train
cp.cuda.Memory(6553600000)
Annealing = [1, 2]
# AND
# input_data = [[0, 0], [1, 1], [0, 1], [1, 1], [1, 0], [1, 1]]  # AND閘輸入
# expect_data = [[0], [1], [0], [1], [0], [1]]  # AND閘答案
player = -1
train_datas = 0
L = 0.00001
hidden_nodes = 9
print("載入資料集...")
with open('qtrain_data.txt', newline='') as csvfile:
    f = csv.reader(csvfile)
    input_data = list()
    for row in f:
        input_data.append(list(map(float, row)))
        train_datas += 1
    input_data = cp.array(input_data, cp.float)
with open('atrain_data.txt', newline='') as csvfile:
    f = csv.reader(csvfile)
    expect_data = list()
    for row in f:
        expect_data.append(list(map(float, row)))
    expect_data = cp.asarray(expect_data, cp.float)
print("隨機產生權重...")
# with open('weight_%f.txt' % L, newline='') as csvfile:
#     f = csv.reader(csvfile)
#     weight = list()
#     for row in f:
#         weight.append(list(map(float, row)))
#     weight = cp.asarray(weight, cp.float)
# with open('weight2_%f.txt' % L, newline='') as csvfile:
#     f = csv.reader(csvfile)
#     weight2 = list()
#     for row in f:
#         weight2.append(list(map(float, row)))
#     weight2 = cp.asarray(weight2, cp.float)
# with open('baise_%f.txt' % L, newline='') as csvfile:
#     f = csv.reader(csvfile)
#     baise = list()
#     for row in f:
#         baise.append(list(map(float, row)))
#     baise = cp.asarray(baise, cp.float)
# with open('baise2_%f.txt' % L, newline='') as csvfile:
#     f = csv.reader(csvfile)
#     baise2 = list()
#     for row in f:
#         baise2.append(list(map(float, row)))
#     baise2 = cp.asarray(baise2, cp.float)
train_datas = len(input_data)
inputs_nodes = len(input_data[0])
output_nodes = len(expect_data[0])
weight = cp.random.uniform(0, 1, (inputs_nodes, hidden_nodes))
weight2 = cp.random.uniform(0, 1, (hidden_nodes, hidden_nodes))
weight3 = cp.random.uniform(0, 1, (hidden_nodes, hidden_nodes))
weight4 = cp.random.uniform(0, 1, (hidden_nodes, output_nodes))
baise = cp.random.rand(hidden_nodes)
baise2 = cp.random.rand(hidden_nodes)
baise3 = cp.random.rand(hidden_nodes)
baise4 = cp.random.rand(output_nodes)


def ox(x):
    if cp.sum(x):
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


k = 0
times = 0
idx = cp.arange(train_datas)
x = list()
y = list()
print("開始訓練...")
while cp.less(k, train_datas):
    times = cp.add(times, 1)
    output = train.TTTG_Network(
        input_data, weight, baise, weight2, baise2, weight3, baise3, weight4, baise4, L, expect_data, True, True)
    if times % 10000 == 0:
        error = cp.sum(output[0])
        result = expect_data[idx, output[1]]
        k = cp.count_nonzero(result)
        # result = cp.equal(expect_data, cp.asarray(output[1]))  # AND閘
        expect_idx = list()
        for i in map(cp.nonzero, expect_data[result == 0]):
            expect_idx.append(i[0].tolist())
        print("輸入棋盤,輸出位置,預計輸出,實際輸出:", *list(zip(input_data[result == 0].tolist(
        ), output[1][result == 0].tolist(), expect_idx, output[2][result == 0].tolist())), sep='\n')
        print("第%d次訓練(學習率:%f):" % (times, L))
        print("總誤差:", error)
        print("答對筆數/總筆數: %d/%d" % (k, train_datas))
        # x.append(L)
        # y.append(output[0])
        # L = L * 10
        # if L >= 1:
        #     plt.plot([5, 4, 3, 2, 1, 0], y)
        #     plt.show()
        #     exit()
        # if times % 1000000 * Annealing[0] * Annealing[1] == 0:
        #     L = L / Annealing[1]
        #     Annealing[0] += 1
        #     if L < 0.000001:
        #         plt.show()
        print()
print("第%d次訓練(學習率:%f):" % (times, L))
print("output:\n", output[2])
print("總誤差:", error)
print(expect_data.shape)
print("輸出位置:", output[1])
print("輸出位置對應答案的值", result)
print("答對筆數/總筆數: %d/%d" % (k, train_datas))
# plt.plot(x, y)
# plt.show()
cp.savez("weight_%f.npz" % (L), weight, weight2,
         weight3, weight4, baise, baise2, baise3, baise4)
# with open("weight_%f.txt" % (L), 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile)
#     for i in weight:
#         spamwriter.writerow(map(str, i))
# with open("weight2_%f.txt" % (L), 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile)
#     for i in weight2:
#         spamwriter.writerow(map(str, i))
# with open("baise_%f.txt" % (L), 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile)
#     for i in baise:
#         spamwriter.writerow(map(str, i))
# with open("baise2_%f.txt" % (L), 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile)
#     for i in baise2:
#         spamwriter.writerow(map(str, i))
