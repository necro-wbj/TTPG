import numpy as np


def UpperLeft(chessboard, x, y, player):
    if x > 0 and y > 0:
        if chessboard[x-1][y-1] == 0:
            return player*-1
        if chessboard[x-1][y-1] == player:
            return player
        chessboard[x-1][y-1] = UpperLeft(chessboard, x-1, y-1, player)
    else:
        return chessboard[x][y]
    return UpperLeft(chessboard, x-1, y-1, player)


def Left(chessboard, x, y, player):
    if x > 0:
        if chessboard[x-1][y] == 0:
            return player*-1
        if chessboard[x-1][y] == player:
            return player
        chessboard[x-1][y] = Left(chessboard, x-1, y, player)
    else:
        return chessboard[x][y]
    return Left(chessboard, x-1, y, player)


def BottomLeft(chessboard, x, y, player):
    if x > 0 and y < 7:
        if chessboard[x-1][y+1] == 0:
            return player*-1
        if chessboard[x-1][y+1] == player:
            return player
        chessboard[x-1][y+1] = BottomLeft(chessboard, x-1, y+1, player)
    else:
        return chessboard[x][y]
    return BottomLeft(chessboard, x-1, y+1, player)


def Down(chessboard, x, y, player):
    if y < 7:
        if chessboard[x][y+1] == 0:
            return player*-1
        if chessboard[x][y+1] == player:
            return player
        chessboard[x][y+1] = Down(chessboard, x, y+1, player)
    else:
        return chessboard[x][y]
    return Down(chessboard, x, y+1, player)


def BottomRight(chessboard, x, y, player):
    if x < 7 and y < 7:
        if chessboard[x+1][y+1] == 0:
            return player*-1
        if chessboard[x+1][y+1] == player:
            return player
        chessboard[x+1][y+1] = BottomRight(chessboard, x+1, y+1, player)
    else:
        return chessboard[x][y]
    return BottomRight(chessboard, x+1, y+1, player)


def Right(chessboard, x, y, player):
    if x < 7:
        if chessboard[x+1][y] == 0:
            return player*-1
        if chessboard[x+1][y] == player:
            return player
        chessboard[x+1][y] = Right(chessboard, x+1, y, player)
    else:
        return chessboard[x][y]
    return Right(chessboard, x+1, y, player)


def UpperRight(chessboard, x, y, player):
    if x < 7 and y > 0:
        if chessboard[x+1][y-1] == 0:
            return player*-1
        if chessboard[x+1][y-1] == player:
            return player
        chessboard[x+1][y-1] = UpperRight(chessboard, x+1, y-1, player)
    else:
        return chessboard[x][y]
    return UpperRight(chessboard, x+1, y-1, player)


def Top(chessboard, x, y, player):
    if y > 0:
        if chessboard[x][y-1] == 0:
            return player*-1
        if chessboard[x][y-1] == player:
            return player
        chessboard[x][y-1] = Top(chessboard, x, y-1, player)
    else:
        return chessboard[x][y]
    return Top(chessboard, x, y-1, player)


def update(chessboard, x, y, player):
    print('棋盤已更新')
    for px, py in [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]:
        for i in range(1, 8):
            if x+px*i < 0 or y+py*i < 0 or x+px*i >= 8 or y+py*i >= 8:
                break
            elif chessboard[x+px*i][y+py*i] == player:
                for j in range(1, i):
                    chessboard[x+px*j][y+py*j] = player
                break
            elif chessboard[x+px*i][y+py*i] == 0:
                break
            elif chessboard[x+px*i][y+py*i] == player*-1:
                continue
            else:
                input(f'棋盤更新錯誤!!val: {chessboard[x+px*i][y+py*i]}')
    return chessboard
    # UpperLeft(chessboard, x, y, player)
    # Left(chessboard, x, y, player)
    # BottomLeft(chessboard, x, y, player)
    # Down(chessboard, x, y, player)
    # BottomRight(chessboard, x, y, player)
    # Right(chessboard, x, y, player)
    # UpperRight(chessboard, x, y, player)
    # Top(chessboard, x, y, player)
    # return chessboard


def check(chessboard, x, y):
    result = list()
    for px, py in [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]:
        mid = list()
        for i in range(1, 8):
            if x+px*i < 0 or y+py*i < 0 or x+px*i >= 8 or y+py*i >= 8:
                break
            if chessboard[x+px*i][y+py*i] == 0:
                if len(mid) and np.all([mid == chessboard[x][y]*-1]):
                    result.append([x+px*i, y+py*i])
                break
            else:
                mid.append(chessboard[x+px*i][y+py*i])
    return result
