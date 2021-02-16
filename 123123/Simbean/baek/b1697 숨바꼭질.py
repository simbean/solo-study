#https://www.acmicpc.net/problem/1697
import sys
if __name__ == "__main__":
    global ans,clone
    L = [100001 for i in range(0 , 100001)]
    M = []
    ans = 0
    N = list(map(int,sys.stdin.readline().split()))
    L[N[0]] = 0
    M.append(N[0])
    while True:
        clone = []
        if L[N[1]] != 100001:
            break
        ans += 1
        for i in M:
            if i+1 <= 100000 and L[i+1] == 100001:
                L[i+1] = ans
                clone.append(i+1)
            if i-1 >= 0 and L[i-1] == 100001:
                L[i-1] = ans
                clone.append(i - 1)
            if i*2 <= 100000 and L[i*2] == 100001:
                L[i*2] = ans
                clone.append(2 * i)
        M = clone[:]
    print(L[N[1]])