#https://www.acmicpc.net/problem/1149
#https://www.acmicpc.net/problem/1149
import sys

def b1149(map):
    #print(map)
    ans = [[0 for _ in range(3)] for i in range(N)]
    ans[0][0] = map[0][0]
    ans[0][1] = map[0][1]
    ans[0][2] = map[0][2]
    for i in range(1,N):
        ans[i][0] = min(ans[i - 1][1] + map[i][0], ans[i - 1][2] + map[i][0])
        ans[i][1] = min(ans[i - 1][0] + map[i][1], ans[i - 1][2] + map[i][1])
        ans[i][2] = min(ans[i - 1][1] + map[i][2], ans[i - 1][0] + map[i][2])
    #print(ans)
    print(min(ans[N-1]))
if __name__ == "__main__":
    #print(p)
    N = int(sys.stdin.readline())
    M = []
    for i in range(N):
        M.append(list(map(int,sys.stdin.readline().split())))
    b1149(M)
