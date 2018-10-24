#! python
import random
# a = [random.randint(-1, 1) for _ in range(9)]
player = -1
output = [0 for _ in range(9)]
temp = [0 for x in output]
a = [0 for _ in range(9)]
h = [0 for _ in range(10)]
# weight = [[random.random() for _ in range(len(a))] + [1]for _ in range(len(h))]
# weight2 = [[random.random()for _ in range(len(h))]for _ in range(len(output))]
weight = []
weight2 = []
with open("weight.txt", "r") as f:
    L = []
    for line in f:
        L = L + [float(line.strip())]
        if len(L) == len(h):
            weight.append(L)
            L = []
with open("weight2.txt", "r") as f:
    L = []
    for line in f:
        L = L + [float(line.strip())]
        if len(L) == len(h):
            weight2.append(L)
            L = []


def ox(a):  # 判斷要顯示O還X
    if a == 0:
        return " "
    elif a == -1:
        return "X"
    elif a == 1:
        return "O"


def p():  # 將結果列印至螢幕
    global a
    print(ox(a[0]) + '|' + ox(a[1]) + '|' + ox(a[2]))
    print("_", "_", "_")
    print(ox(a[3]) + "|" + ox(a[4]) + "|" + ox(a[5]))
    print("_", "_", "_")
    print(ox(a[6]) + "|" + ox(a[7]) + "|" + ox(a[8]))


def u(temp):  # 將答案更新到棋盤
    global a, player
    if 1 in temp:
        a[temp.index(1)] = player
    else:
        print("temp錯誤!", temp)
        a[temp.index(1)] = player

    # if a[d] != 0:

    # elif a[temp.index(1)]:
    # pass


def win():  # 判斷是誰獲勝
    global a, player, test
    if a[0] != 0 and a[0] == a[1] and a[1] == a[2]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a[3] != 0 and a[3] == a[4] and a[4] == a[5]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a[6] != 0 and a[6] == a[7] and a[7] == a[8]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a[0] != 0 and a[0] == a[3] and a[3] == a[6]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a[1] != 0 and a[1] == a[4] and a[4] == a[7]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a[2] != 0 and a[2] == a[5] and a[5] == a[8]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a[0] != 0 and a[0] == a[4] and a[4] == a[8]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a[2] != 0 and a[2] == a[4] and a[4] == a[6]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a.count(0) == 0:
        print("平手!!!")
        return False
    else:
        return True


def ai():
    global a, temp, player
    if a[0] != 0 and a[1] == 0 and a[0] == a[2]:
        temp[1] = 1
        print("偵錯1")
    elif a[2] != 0 and a[5] == 0 and a[2] == a[8]:
        temp[5] = 1
        print("偵錯2")
    elif a[6] != 0 and a[7] == 0 and a[6] == a[8]:
        temp[7] = 1
        print("偵錯3")
    elif a[0] != 0 and a[3] == 0 and a[0] == a[6]:
        temp[3] = 1
        print("偵錯4")

    elif a[0] != 0 and a[0] != player and a[1] != 0 and a[1] != player and a[2] == 0:
        temp[2] = 1
        print("偵錯5")
    elif a[0] != 0 and a[0] != player and a[3] != 0 and a[3] != player and a[6] == 0:
        temp[6] = 1
        print("偵錯6")
    elif a[2] != 0 and a[2] != player and a[1] != 0 and a[1] != player and a[0] == 0:
        temp[0] = 1
        print("偵錯7")
    elif a[2] != 0 and a[2] != player and a[5] != 0 and a[5] != player and a[8] == 0:
        temp[8] = 1
        print("偵錯8")
    elif a[6] != 0 and a[6] != player and a[3] != 0 and a[3] != player and a[0] == 0:
        temp[0] = 1
        print("偵錯9")
    elif a[6] != 0 and a[6] != player and a[7] != 0 and a[7] != player and a[8] == 0:
        temp[8] = 1
        print("偵錯10")
    elif a[8] != 0 and a[8] != player and a[5] != 0 and a[5] != player and a[2] == 0:
        temp[2] = 1
        print("偵錯11")
    elif a[8] != 0 and a[8] != player and a[7] != 0 and a[7] != player and a[6] == 0:
        temp[6] = 1
        print("偵錯12")

    elif a[7] == 0 and a[1] != 0 and a[1] != player and a[4] != 0 and a[4] != player:
        temp[7] = 1
        print("偵錯13")
    elif a[5] == 0 and a[3] != 0 and a[3] != player and a[4] != 0 and a[4] != player:
        temp[5] = 1
        print("偵錯14")
    elif a[3] == 0 and a[5] != 0 and a[5] != player and a[4] != 0 and a[4] != player:
        temp[3] = 1
        print("偵錯15")
    elif a[1] == 0 and a[7] != 0 and a[7] != player and a[4] != 0 and a[4] != player:
        temp[1] = 1
        print("偵錯16")
    elif a[0] != 0 and a[0] == a[8] and a[0] != player:
        if a[1] == 0:
            temp[1] = 1
        elif a[3] == 0:
            temp[3] = 1
        elif a[5] == 0:
            temp[5] = 1
        elif a[7] == 0:
            temp[7] = 1
        else:
            temp[a.index(0)] = 1
        print("偵錯17")
    elif a[2] != 0 and a[2] == a[6] and a[2] != player:
        if a[1] == 0:
            temp[1] = 1
        elif a[3] == 0:
            temp[3] = 1
        elif a[5] == 0:
            temp[5] = 1
        elif a[7] == 0:
            temp[7] = 1
        else:
            temp[a.index(0)] = 1
        print("偵錯18")
    elif a[4] == 0:
        temp[4] = 1
        print("偵錯19")

    elif a[4] == player and a[0] == player and a[2] == 0:
        temp[2] = 1
        print("偵錯20")
    elif a[4] == player and a[0] == player and a[6] == 0:
        temp[6] = 1
        print("偵錯21")
    elif a[4] == player and a[2] == player and a[0] == 0:
        temp[0] = 1
        print("偵錯22")
    elif a[4] == player and a[2] == player and a[8] == 0:
        temp[8] = 1
        print("偵錯23")
    elif a[4] == player and a[6] == player and a[0] == 0:
        temp[0] = 1
        print("偵錯24")
    elif a[4] == player and a[6] == player and a[8] == 0:
        temp[8] = 1
        print("偵錯25")
    elif a[4] == player and a[8] == player and a[2] == 0:
        temp[2] = 1
        print("偵錯26")
    elif a[4] == player and a[8] == player and a[6] == 0:
        temp[6] = 1
        print("偵錯27")

    elif a[0] == 0 and a[8] == 0:
        temp[0] = 1
        print("偵錯28")
    elif a[2] == 0 and a[6] == 0:
        temp[2] = 1
        print("偵錯29")

    elif a[6] == 0 and a[4] == a[2]:
        temp[6] = 1
        print("偵錯30")
    elif a[8] == 0 and a[4] == a[0]:
        temp[8] = 1
        print("偵錯31")
    elif a[2] == 0 and a[4] == a[6]:
        temp[2] = 1
        print("偵錯32")
    elif a[0] == 0 and a[4] == a[8]:
        temp[0] = 1
        print("偵錯33")
    else:
        temp[a.index(0)] = 1
        print("偵錯34")


def act(arr):
    import math
    for i in range(len(arr)):
        arr[i] = 1 / (1 + math.exp(-arr[i]))


def oact(arr):
    global a
    for i in range(len(arr)):
        if arr[i] >= 0.5:
            arr[i] = 1
        else:
            arr[i] = 0
    if 1 in arr:
        pass
    else:
        arr[a.index(0)] = 1
    return arr


def train(temp, weight, output, weight2, a, h):
    E = []
    for j in range(len(output)):
        E.append((temp[j] - output[j]) * output[j] * (1 - output[j]))
        for i in range(len(h)):
            weight2[j][i] += 0.1 * E[j] * h[i]
    E2 = []
    for j in range(len(h)):
        ei = 0
        for k in range(len(E)):
            ei += E[k] * weight2[k][j]
        E2.append(h[j] * (1 - h[j]) * ei)
        for i in range(len(a)):
            weight[j][i] += 0.1 * E2[j] * a[i]
        weight[j][2] += 0.1 * E2[j]


def ai2(a):
    global temp, weight, output, weight2
    output = [0 for _ in output]
    h = [0] * 10
    for j in range(len(h)):
        for i in range(len(a)):
            h[j] += weight[j][i] * a[i]
        h[j] += weight[j][i + 1]
    act(h)
    print("隱藏層:", h)
    print("輸出層權重:", weight2)
    for j in range(len(output)):
        for i in range(len(h)):
            output[j] += weight2[j][i] * h[i]
    act(output)
    # 正確答案
    ai()
    train(temp, weight, output, weight2, a, h)
    print("輸出:", output)
    print("正確", temp.index(1))
    temp = oact(output)


def human():
    global temp, a
    x = input('請輸入格位：')
    while a[int(x)] != 0 or a[int(x)] > 8:
        x = input('輸入錯誤!請重新輸入：')
    temp[int(x)] = 1


for x in range(10000):
    a = [0] * 9
    while win():
        temp = [0 for x in output]
        if player == 1:
            player = -1
        else:
            player = 1
        if player == 1:
            ai2(a)
            print("輸出(轉換):", temp.index(1))
        else:
            ai()
        u(temp)
        p()
        print("-----------------------------")
    print(a)
    print("-----------------------------")
# with open("weight.txt", "w") as f:
#     for i in weight:
#         for s in i:
#             f.write(str(s) + "\n")
# with open("weight2.txt", "w") as f:
#     for i in weight2:
#         for s in i:
#             f.write(str(s) + "\n")
