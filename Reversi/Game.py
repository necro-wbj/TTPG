import numpy as np
import scan
import TrainingReversi as tr
import random
chessboard = np.zeros((8, 8), dtype=float)
player = -1
next_player = player
p1 = list()
p2 = list()
first = True


def start():
    global chessboard, player, p1, p2, first
    first = True
    chessboard = np.zeros((8, 8), dtype=float)
    player = -1
    p1 = list()
    p2 = list()
    chessboard[3][3] = 1
    chessboard[3][4] = -1
    chessboard[4][3] = -1
    chessboard[4][4] = 1
    dissplay(chessboard)
    print('..................................................')
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
    if len(result) > 0:
        for x, y in result:
            canDown[x][y] = True
    return canDown


def opposite(chessboard):
    train_chessboard = np.array(list(map(lambda x: x*-1, chessboard)))
    return train_chessboard


def dissplay(chessboard):
    row = 0
    print('  | A | B | C | D | E | F | G | H |')
    print("-----------------------------------")
    for i in chessboard:
        first = True
        for j in i:
            if first:
                print(row, '|', end='')
                first = False
                row += 1
            if j == 0:
                print('   ', end='|')
            elif j == -1:
                print(' ○ ', end='|')
            else:
                print(' ● ', end='|')
        print("\n-------------------------------------------------")


input_data = list()
expect_data = list()
clean = 0
# for _ in range(1000):
while True:
    start()
    while end(chessboard):
        player = next_player
        if player == -1:
            predict_opt = tr.predict_opt(opposite(chessboard)).reshape((8, 8))
        else:
            predict_opt = tr.predict_opt(chessboard).reshape((8, 8))
        cnaDown = check(player)
        predict_opt[cnaDown == False] = -1
        # if player == -1:
        #     playX, playY = input("請輸入位置：")
        #     playX = ord(playX.upper())-65
        #     playY = int(playY)
        #     chessboard[playY][playX] = -1
        #     predict_opt[predict_opt != -1] = 0
        #     predict_opt[playY][playX] = 1
        # else:
        #     chessboard[predict_opt == np.amax(predict_opt)] = 1
        if first:
            first = False
            ranlist = [[3, 2], [2, 3], [5, 4], [4, 5]]
            r = random.randint(0, 3)
            chessboard[ranlist[r][0]][ranlist[r][1]] = -1
            predict_opt[predict_opt != -1] = 0
            predict_opt[ranlist[r][0]][ranlist[r][1]] = 1
        else:
            chessboard[predict_opt == np.amax(predict_opt)] = player
        position = np.argmax(predict_opt.reshape((64,)))
        scan.update(chessboard, position // 8, position % 8, player)
        if player == -1:
            p1.append([np.array(opposite(chessboard).reshape((64,))),
                       np.array(predict_opt.reshape((64,)))])
        else:
            p2.append([np.array(chessboard.reshape((64,))),
                       np.array(predict_opt.reshape((64,)))])
        if np.any(check(player*-1)):
            next_player = player*-1
        print(f'此局為: {player} 下 ， 下局為: {next_player} 下')
        dissplay(chessboard)
        print('..................................................')
    player_black = np.size(chessboard[chessboard == -1])
    player_white = np.size(chessboard[chessboard == 1])
    if player_black > player_white:
        print("-1獲勝")
        for predict_opt in p1:
            predict_opt[1][predict_opt[1] == np.amax(predict_opt[1])] = 1
            input_data.append(predict_opt[0])
            expect_data.append(predict_opt[1])
        for predict_opt in p2:
            predict_opt[1][predict_opt[1] == np.amax(predict_opt[1])] = 0
            input_data.append(predict_opt[0].reshape((64,)))
            expect_data.append(predict_opt[1].reshape((64,)))
    elif player_black < player_white:
        print("1獲勝")
        for predict_opt in p1:
            predict_opt[1][predict_opt[1] == np.amax(predict_opt[1])] = 1
            input_data.append(predict_opt[0])
            expect_data.append(predict_opt[1])
        for predict_opt in p2:
            predict_opt[1][predict_opt[1] == np.amax(predict_opt[1])] = 0
            input_data.append(predict_opt[0].reshape((64,)))
            expect_data.append(predict_opt[1].reshape((64,)))
    else:
        print("平手!!")
        for predict_opt in p1:
            input_data.append(predict_opt[0])
            expect_data.append(predict_opt[1])
        for predict_opt in p2:
            input_data.append(predict_opt[0].reshape((64,)))
            expect_data.append(predict_opt[1].reshape((64,)))
    train_data = list()
    train_data.append(input_data)
    train_data.append(expect_data)
    batch = len(input_data)
    tr.train(input_data, expect_data, batch)
    if clean == 0:
        input_data = list()
        expect_data = list()
        clean = 5
    clean -= 1
