import Main_TrainingReversi as mtr
import TrainingReversi as tr
import numpy as np
import random
import scan
next_player = -1
p1 = list()
p2 = list()
first = True


def start():
    global next_player, p1, p2, first
    first = True
    chessboard = np.array([[0]*8]*8)
    next_player = -1
    p1 = list()
    p2 = list()
    input_temp = list()
    chessboard[3][4] = -1
    chessboard[3][3] = 1
    chessboard[4][3] = -1
    chessboard[4][4] = 1
    dissplay(chessboard)
    print('..................................................')
    return chessboard, input_temp


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
batch = 0
# for _ in range(10):
while True:
    chessboard, input_temp = start()
    while end(chessboard):
        player = next_player
        if player == -1:
            input_temp = opposite(list(chessboard))
            predict_opt = tr.predict_opt(input_temp)
        else:
            input_temp = list(chessboard)
            predict_opt = mtr.predict_opt(input_temp)
        cnaDown = check(player)
        predict_opt[cnaDown == False] = -1
        if not np.all(cnaDown):
            print(f'下的位置: {np.nonzero(predict_opt == np.amax(predict_opt))}')
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
            chessboard = scan.update(
                chessboard, position // 8, position % 8, player)
            if player == -1:
                p1.append([np.array(input_temp).reshape(64,),
                           np.array(predict_opt.reshape((64,)))])
            else:
                p2.append([np.array(input_temp).reshape(64,),
                           np.array(predict_opt.reshape((64,)))])
            print(f'此局為: {player} 下 ， 下局為: {next_player} 下')
            dissplay(chessboard)
            print('..................................................')
        if np.any(check(player*-1)):
            next_player = player*-1
    player_black = np.size(chessboard[chessboard == -1])
    player_white = np.size(chessboard[chessboard == 1])
    if batch >= 600:
        if player_black > player_white:
            print(f"主要網路獲勝 => 重新訓練")
            tr.update_weights(input_data, expect_data, batch)
        elif player_black < player_white:
            print("主要網路敗北 => 更新強度為敵對網路")
            mtr.update_weights(input_data, expect_data, batch)
        else:
            print("平手!! => 重新訓練敵對網路")
            tr.update_weights(input_data, expect_data, batch)
        batch = 0
        input_data = list()
        expect_data = list()
    else:
        if player_black > player_white:
            print(
                f"黑棋獲勝\t黑棋數量: {player_black}\t白旗數量: {player_white}", end='\t')
            for dataset in p1:
                input_data.append(dataset[0])
                dataset[1][dataset[1] == np.amax(dataset[1])] = 1
                expect_data.append(dataset[1])
            for dataset in p2:
                input_data.append(dataset[0].reshape((64,)))
                dataset[1][dataset[1] == np.amax(dataset[1])] = 0
                expect_data.append(dataset[1].reshape((64,)))
        elif player_black < player_white:
            print(
                f"白棋獲勝\t黑棋數量: {player_black}\t白旗數量: {player_white}", end='\t')
            for dataset in p1:
                dataset[1][dataset[1] == np.amax(dataset[1])] = 1
                input_data.append(dataset[0])
                expect_data.append(dataset[1])
            for dataset in p2:
                input_data.append(dataset[0].reshape((64,)))
                dataset[1][dataset[1] == np.amax(dataset[1])] = 0
                expect_data.append(dataset[1].reshape((64,)))
        else:
            print(
                f"平手!!\t黑棋數量: {player_black}\t白旗數量: {player_white}", end='\t')
            for dataset in p1:
                input_data.append(dataset[0])
                dataset[1][dataset[1] == np.amax(dataset[1])] = 0.5
                expect_data.append(dataset[1])
            for dataset in p2:
                input_data.append(dataset[0].reshape((64,)))
                dataset[1][dataset[1] == np.amax(dataset[1])] = 0.5
                expect_data.append(dataset[1].reshape((64,)))
        train_data = list()
        train_data.append(input_data)
        train_data.append(expect_data)
        batch = len(input_data)
        print(f'累計棋盤數: {batch}')
        tr.train(input_data, expect_data, batch)
