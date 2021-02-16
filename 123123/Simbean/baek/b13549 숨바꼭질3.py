#https://www.acmicpc.net/problem/13549
import sys
def Mul2(X):
    for j in X:
        index = j
        while 0 < index <= 100000:
            if L[index] == 100000:
                L[index] = ans
                M.append(index)
            index *= 2


if __name__ == "__main__":
    global ans,clone
    L = [100000 for i in range(0 , 100001)]
    M = []
    ans = 0
    N = list(map(int,sys.stdin.readline().split()))
    M.append(N[0])
    while True:
        clone = []
        if L[N[1]] != 100000 or M == []:
            break
        Mul2(M)
        ans += 1
        for i in M:
            if i+1 <= 100000 and L[i+1] == 100000:
                L[i+1] = ans
                clone.append(i+1)
            if i-1 >= 0 and L[i-1] == 100000:
                L[i-1] = ans
                clone.append(i - 1)
        M = clone[:]
    print(L[N[1]])