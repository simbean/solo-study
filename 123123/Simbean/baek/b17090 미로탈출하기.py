#https://www.acmicpc.net/problem/17090
import collections as d
import sys
def cul(map,q, integer):
    while len(q) != 0:
        xy = q.pop()
        map[xy[0]][xy[1]] = integer
def b17090(map,n,m):
    clone = [[0 for i in range(m)]for i in range(n)]
    deq = d.deque([])
    for i in range(n):
        for j in range(m):
            if clone[i][j] != 0:
                continue
            else:
                a = i
                b = j
                while True:
                    #print([a,b,i,j])
                    if 0<= a < n and 0 <= b < m:
                        if clone[a][b] == 1:
                            cul(clone,deq,1)
                            break
                        elif clone[a][b] == -1:
                            cul(clone,deq,-1)
                            break
                        if map[a][b] == 'D':
                            deq.append([a, b])
                            clone[a][b] = -1
                            a += 1
                        elif map[a][b] == 'U':
                            deq.append([a, b])
                            clone[a][b] = -1
                            a -= 1
                        elif map[a][b] == 'R':
                            deq.append([a, b])
                            clone[a][b] = -1
                            b += 1
                        elif map[a][b] == 'L':
                            deq.append([a, b])
                            clone[a][b] = -1
                            b -= 1
                        else:
                            break
                    else:
                        #print(deq)
                        cul(clone,deq,1)
                        break
    ans = 0
    for i in range(n):
        for j in range(m):
            if clone[i][j] == 1:
               ans += 1
    print(ans)
if __name__ == "__main__":
    N = list(map(int,sys.stdin.readline().split()))
    Map = []
    for i in range(N[0]):
        Map.append(list(sys.stdin.readline()[:-1]))

    b17090(Map,N[0],N[1])