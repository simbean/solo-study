#https://www.acmicpc.net/problem/16235
#==============python 시간초과 pypy3 1068ms==================
import sys
import collections as C
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]
def b16235():
    global appear
    index = 0
    while True:
        index += 1
        #spring====
        cell = 0
        grow = []
        for i in range(N[0]):
            for j in range(N[0]):
                eat = C.deque([])
                while len(status[i][j]) != 0:
                    tree = status[i][j].popleft()
                    if tree > ground[i][j]:
                        cell += int(tree/2)
                    else:
                        ground[i][j] -= tree
                        eat.append(tree+1)
                        if (tree+1) % 5== 0:
                            grow.append([i,j])
                ground[i][j] += cell
                cell = 0
                status[i][j] = eat.copy()
                ground[i][j] += growing[i][j]
        #summer======
        #fall========
        while grow != []:
            xy = grow.pop()
            for l in range(8):
                i = xy[0] + dx[l]
                j = xy[1] + dy[l]
                if 0<=i<N[0] and 0<=j<N[0]:
                    status[i][j].appendleft(1)
        if index == N[2]:
            break
if __name__ == '__main__':
    global status, ground, appear, growing,N
    N = list(map(int,sys.stdin.readline().split()))
    ground = [[5 for _ in range(N[0])] for _ in range(N[0])]
    growing = []
    for i in range(0, N[0]):
        a = list(map(int, sys.stdin.readline().split()))
        growing.append(a)
    status = [[C.deque([]) for i in range(N[0])]for i in range(N[0])]
    for i in range(0, N[1]):
        a = list(map(int, sys.stdin.readline().split()))
        status[a[0]-1][a[1]-1].append(a[2])
    b16235()
    ans = 0
    for i in range(N[0]):
        for j in range(N[0]):
            ans += len(status[i][j])
    print(ans)