def win(a, team):
    if a[0] != 0 and a[0] == a[1] and a[0] == a[2]:
        return a[0]
    else:
        if a[3] != 0 and a[3] == a[4] and a[3] == a[5]:
            return a[3]
        else:
            if a[6] != 0 and a[6] == a[7] and a[6] == a[8]:
                return a[6]
            else:
                if a[0] != 0 and a[0] == a[3] and a[0] == a[6]:
                    return a[0]
                else:
                    if a[1] != 0 and a[1] == a[4] and a[1] == a[7]:
                        return a[1]
                    else:
                        if a[2] != 0 and a[2] == a[5] and a[2] == a[8]:
                            return a[2]
                        else:
                            if a[4] != 0 and a[4] == a[0] and a[4] == a[8]:
                                return a[4]
                            else:
                                if a[4] != 0 and a[4] == a[2] and a[4] == a[6]:
                                    return a[4]
    return 0


def ox(a):  # 判斷要顯示O還X
    if a == 0:
        return " "
    elif a == -1:
        return "X"
    elif a == 1:
        return "O"


def p(a):  # 將結果列印至螢幕
    print(ox(a[0]) + '|' + ox(a[1]) + '|' + ox(a[2]))
    print("_", "_", "_")
    print(ox(a[3]) + "|" + ox(a[4]) + "|" + ox(a[5]))
    print("_", "_", "_")
    print(ox(a[6]) + "|" + ox(a[7]) + "|" + ox(a[8]))

def over(out):
    if win(out, 1):
        p(out)
        print("玩家獲勝!")
        exit()
    elif win(out,1):
       p(out)
       print("*******************************")
       print("電腦獲勝!")
       exit()
    elif not out.count(0):
        p(out)
        print("*******************************")
        print("平手!")
        exit()
    else:
        p(out)
        print("*******************************")
