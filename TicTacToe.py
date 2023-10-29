# https://www.youtube.com/watch?v=E8fmDDtaHLU
def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")


def Sum(a, b, c):
    return a+b+c


def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in wins:
        if Sum(xState[i[0]], xState[i[1]], xState[i[2]]) == 3:
            # print("X won the match !!!")
            return 1
        if Sum(zState[i[0]], zState[i[1]], zState[i[2]]) == 3:
            # print("O won the match !!!")
            return 0
    return -1


if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1=>X and 0=>O
    print("Welcome to Tic Tac Toe")
    print("Let's play...")

    temp_ct = 9
    while True:
        print("")
        printBoard(xState, zState)
        if turn == 1:
            print("----X's chance----")
            value = int(input("Please enter X's value : "))
            xState[value] = 1
        else:
            print("----O's chance----")
            value = int(input("Please enter O's value : "))
            zState[value] = 1
        cwin = checkWin(xState,zState)
        if cwin == 1:
            printBoard(xState, zState)
            print("X won the match !!!")
            print("Match over..")
            break
        if cwin == 0:
            printBoard(xState, zState)
            print("O won the match !!!")
            print("Match over..")
            break
        turn = 1 - turn
        temp_ct = temp_ct - 1
        if temp_ct == 0:
            print("Well played...")
            print("Match Draw !!!")
            break

