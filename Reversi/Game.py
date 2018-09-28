import numpy as np
import scan
import TrainingReversi as tr
chessboard = np.zeros((8, 8), dtype=float)
player = -1
p1 = list()
p2 = list()


def start():
    global chessboard, player, p1, p2
    chessboard = np.zeros((8, 8), dtype=float)
    player = -1
    p1 = list()
    p2 = list()
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
    result = list()
    canDown = np.array([[False]*8]*8)
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == player:
                result.extend(scan.check(chessboard, i, j))
    if len(result):
        player=player*-1
        for x,y in result:
            canDown[x][y] = True
    return canDown, player


for _ in range(100000):
    start()
    while end(chessboard):
        input_data=list()
        expect_data=list()
        out=tr.out(chessboard).reshape((8, 8))
        print(chessboard)
        cnaDown, next_player=check(player)
        out[cnaDown == False]=-1
        if player == -1:
            playX, playY=input("請輸入位置：")
            playX=ord(playX.upper())-65
            playY=int(playY)
            chessboard[playY][playX]=-1
            out[out != -1]=0
            out[playY][playX]=1
        else:
            chessboard[out == np.amax(out)]=1
        position=np.argmax(out.reshape((64,)))
        scan.update(chessboard, position // 8, position % 8, player)
        if player == -1:
            p1.append([np.array(chessboard.reshape((64,))),
                       np.array(out.reshape((64,)))])
        else:
            p2.append([np.array(chessboard.reshape((64,))),
                       np.array(out.reshape((64,)))])
        player=next_player
    for out in p1:
        if np.size(chessboard[chessboard == -1]) > np.size(chessboard[chessboard == 1]):
            out[1][out[1] == np.amax(out[1])]=1
            input_data.append(out[0])
            expect_data.append(out[1])
        else:
            out[1][out[1] == np.amax(out[1])]=0
            input_data.append(out[0])
            expect_data.append(out[1])
    for out in p2:
        if np.size(chessboard[chessboard == 1]) > np.size(chessboard[chessboard == -1]):
            out[1][out[1] == np.amax(out[1])]=1
            input_data.append(out[0].reshape((64,)))
            expect_data.append(out[1].reshape((64,)))
        else:
            out[1][out[1] == np.amax(out[1])]=0
            input_data.append(out[0].reshape((64,)))
            expect_data.append(out[1].reshape((64,)))
    batch=len(p1) + len(p2)
    tr.train(input_data, expect_data, batch)