#https://www.acmicpc.net/problem/14501
#https://www.acmicpc.net/problem/14501
import sys
def b14501(N,M):
    day = [M[i][0] for i in range(N)]
    pay = [M[i][1] for i in range(N)]
    ans = [0 for i in range(N+1)]
    for i in range(N-1,-1,-1):
        try:
            ans[i] = max(ans[i+day[i]] + pay[i], ans[i+1])
        except IndexError:
            try:
                ans[i] = ans[i+1]
            except IndexError:
                pass
    print(ans[0])
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = []
    for i in range(N):
        M.append(list(map(int,sys.stdin.readline().split())))
    b14501(N,M)