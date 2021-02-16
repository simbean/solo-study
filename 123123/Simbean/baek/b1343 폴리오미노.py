import math
#https://www.acmicpc.net/problem/1343
board = str(input())
boardlist = []
dotlist = []
sum = 0
dotsum = 0
output = ""
point = 0
if len(board)<501:
    for i in range(0, len(board)):
        if board[i] == 'X':
            if dotsum != 0:
                boardlist.append(str(dotsum))
                dotsum = 0
            sum += 1
        elif board[i] == '.':
            if sum != 0:
                boardlist.append(int(sum))
                sum = 0
            dotsum += 1

    boardlist.append(int(sum))
    boardlist.append(str(dotsum))

    for i in range(0, len(boardlist)):
        if str(type(boardlist[i])) == "<class 'int'>":
            if boardlist[i] % 4 == 0:
                for j in range(0, int(boardlist[i] / 4)):
                    output += 'AAAA'
            elif boardlist[i] % 4 == 2:
                index = math.floor(boardlist[i]/4)
                Bindex = int((int(boardlist[i])-(4*index))/2)
                for j in range(0, index):
                    output += 'AAAA'
                for j in range(0, Bindex):
                    output += 'BB'
            elif boardlist[i] % 2 == 0:
                for i in range(0,boardlist[i] % 2):
                    output += 'BB'
            else:
                print(-1)
                point = 1
                break
        else:
            for i in range(0, int(boardlist[i])):
                output += '.'

if point == 0:
    print(output)