import numpy as np
import scan
import TrainingReversi as tr
chessboard = np.zeros((8, 8), dtype=float)
player = 1
p1 = list()
p2 = list()


def start():
    global chessboard
    chessboard = np.zeros((8, 8), dtype=float)
    chessboard[3][3] = 1
    chessboard[3][4] = -1
    chessboard[4][3] = -1
    chessboard[4][4] = 1
    return chessboard


def end(chessboard):
    amount = np.count_nonzero(chessboard)
    if amount < 64:
        return True
    else:
        return False


def check(player):
    global chessboard
    chessboard_index = list()
    for i in range(8):
        for j in range(8):
            chessboard_index.append([i, j])
    # print(chessboard)
    canDown = np.array([[False]*8]*8)
    result = list()
    for x, y in chessboard_index:
        if chessboard[x][y] == player:
            result.extend(scan.check(chessboard, x, y))
    # print(result)
    # print(len(result))
    for x, y, value in result:
        canDown[x][y] = value
    # print(canDown)
    if len(result):
        player = player*-1
    return canDown, player


start()
while end(chessboard):
    input_data = list()
    expect_data = list()
    out = tr.out(chessboard).reshape((8, 8))
    # print(np.argmax(tr.out(chessboard)))
    # chessboard[chessboard == np.amax(out[check()])] = player
    cnaDown, next_player = check(player)
    out[cnaDown == False] = -1
    # print(chessboard)
    # print("-------------------------------------------------------------")
    # print(out)
    chessboard[out == np.amax(out)] = player
    position = np.argmax(out.reshape((64,)))
    scan.update(chessboard, position // 8, position % 8, player)
    # print(out)
    if player == 1:
        p1.append([np.array(chessboard.reshape((64,))),
                   np.array(out.reshape((64,)))])
    else:
        p2.append([np.array(chessboard.reshape((64,))),
                   np.array(out.reshape((64,)))])
    player = next_player
for out in p1:
    if np.size(chessboard[chessboard == 1]) > np.size(chessboard[chessboard == -1]):
        out[1][out[1] == np.amax(out[1])] = 1
        # print(out[1])
        input_data.append(out[0])
        expect_data.append(out[1])
    else:
        out[1][out[1] == np.amax(out[1])] = 0
        # print(out[1].reshape((64,)))
        input_data.append(out[0])
        expect_data.append(out[1])
for out in p2:
    if np.size(chessboard[chessboard == 1]) < np.size(chessboard[chessboard == -1]):
        out[1][out[1] == np.amax(out[1])] = 1
        input_data.append(out[0].reshape((64,)))
        expect_data.append(out[1].reshape((64,)))
    else:
        out[1][out[1] == np.amax(out[1])] = 0
        input_data.append(out[0].reshape((64,)))
        expect_data.append(out[1].reshape((64,)))
batch = len(p1) + len(p2)

tr.train(input_data, expect_data, batch)

# print("..................................................")
# for i in p1:
#     print(i[0])
#     print(i[1])
#     print("..................................................")
# for i in p2:
#     print(i[1])
#     print("..................................................")
# print(np.size(chessboard[chessboard == 1]),
#       np.size(chessboard[chessboard == -1]))


# out=tr.out(chessboard)
# playX, playY = input("請輸入位置：")
# playX=ord(playX.upper())-65
# chessboard[playX][playY]=1
# # 呼叫類神經網路計算輸出
# # 將類神經網路的輸出更新到棋盤
# print(chessboard, end='\n\n')
# print(scan.update(chessboard, 3, 3, 1))
# print()
