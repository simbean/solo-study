#https://www.acmicpc.net/problem/17070
#https://www.acmicpc.net/problem/17069
import sys
import collections
#파이프 옮기기 1, 파이프 옮기기 2
def b17070(space):
    global m,deq
    m = [[[0,0,0] for i in range(N)] for j in range(N)]
    m[0][1][0] = 1

    for i in range(N):
        for j in range(1,N):
            flag = 0
            if i == 0 and j == 1:
                continue
            if space[i][j] == 1:
                continue
            if space[i][j-1] != 1:
                m[i][j][0] += m[i][j-1][0] + m[i][j-1][2]
                flag += 1
            if space[i-1][j] != 1:
                m[i][j][1] += m[i-1][j][1] + m[i-1][j][2]
                flag += 2
            if space[i - 1][j- 1] != 1 and flag == 3:
                m[i][j][2] += m[i - 1][j - 1][2] + m[i-1][j-1][0] + m[i-1][j-1][1]
    '''for i in range(N):
        print(m[i])'''
    print(sum(m[i][j]))
if __name__ == "__main__":
    #print(p)
    N = int(sys.stdin.readline())
    M = []
    for i in range(N):
        M.append(list(map(int,sys.stdin.readline().split())))
    b17070(M)